import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_review_module():
    module_path = REPO_ROOT / "scripts" / "post-github-review.py"
    spec = importlib.util.spec_from_file_location("post_github_review", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DetectTargetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.repo_dir_context = tempfile.TemporaryDirectory()
        cls.repo_dir = Path(cls.repo_dir_context.name)
        cls.current_repo = "cogine-ai/local-ultra-review"
        owner, repo = cls.current_repo.split("/", 1)
        cls.other_repo = f"{owner}/{repo}-other"
        subprocess.run(["git", "init"], cwd=cls.repo_dir, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        subprocess.run(
            ["git", "remote", "add", "origin", f"https://github.com/{cls.current_repo}.git"],
            cwd=cls.repo_dir,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )

    @classmethod
    def tearDownClass(cls):
        cls.repo_dir_context.cleanup()

    def run_detect_target(self, *args):
        proc = subprocess.run(
            ["bash", str(REPO_ROOT / "scripts" / "detect-target.sh"), *args],
            cwd=self.repo_dir,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return json.loads(proc.stdout)

    def test_current_repo_pr_url_defaults_to_review_post_mode(self):
        result = self.run_detect_target(f"https://github.com/{self.current_repo}/pull/12")

        self.assertEqual(result["target_type"], "pr")
        self.assertEqual(result["target"], "12")
        self.assertEqual(result["repo"], self.current_repo)
        self.assertEqual(result["post_mode"], "review")
        self.assertTrue(result["auto_post"])

    def test_non_current_repo_pr_url_does_not_auto_post(self):
        result = self.run_detect_target(f"https://github.com/{self.other_repo}/pull/12")

        self.assertEqual(result["target_type"], "pr")
        self.assertEqual(result["post_mode"], "none")
        self.assertFalse(result["auto_post"])

    def test_explicit_post_none_overrides_current_repo_url_auto_post(self):
        result = self.run_detect_target(
            f"https://github.com/{self.current_repo}/pull/12",
            "--post",
            "none",
        )

        self.assertEqual(result["post_mode"], "none")
        self.assertFalse(result["auto_post"])

    def test_keep_worktree_option_is_accepted(self):
        result = self.run_detect_target(f"https://github.com/{self.current_repo}/pull/12", "--keep-worktree")

        self.assertTrue(result["ok"])
        self.assertTrue(result["keep_worktree"])


class ReviewPayloadTests(unittest.TestCase):
    def setUp(self):
        self.mod = load_review_module()

    def test_build_review_payload_inlines_only_commentable_findings(self):
        pr_context = {
            "repo": "cogine-ai/local-ultra-review",
            "number": 12,
            "commit_sha": "abc123",
            "head_sha": "abc123",
            "short_commit_sha": "abc123",
        }
        findings = {
            "important": [
                {
                    "title": "Missing tenant filter exposes reports",
                    "severity": "Important",
                    "category": "security",
                    "file": "src/reports.py",
                    "line": 42,
                    "failure_scenario": "A user can request another tenant's report.",
                    "verification": {"summary": "The changed query no longer filters by tenant_id."},
                    "suggested_fix_direction": "Restore the tenant_id predicate.",
                }
            ],
            "nits": [
                {
                    "title": "Error path returns stale status",
                    "severity": "Nit",
                    "category": "correctness",
                    "file": "src/reports.py",
                    "line": 99,
                    "failure_scenario": "A failed export can still appear successful.",
                    "verification": {"summary": "The line is outside the PR diff."},
                }
            ],
            "pre_existing": [],
            "needs_manual_review": [],
        }
        pr_files = [
            {
                "filename": "src/reports.py",
                "patch": "@@ -38,3 +40,5 @@ def load_report():\n context\n+    report = query.get(id)\n+    return report\n",
            }
        ]

        payload, skipped = self.mod.build_review_payload(pr_context, findings, pr_files, "deep", "session-1")

        self.assertEqual(payload["event"], "COMMENT")
        self.assertEqual(payload["commit_id"], "abc123")
        self.assertEqual(len(payload["comments"]), 1)
        self.assertEqual(payload["comments"][0]["path"], "src/reports.py")
        self.assertEqual(payload["comments"][0]["line"], 42)
        self.assertEqual(payload["comments"][0]["side"], "RIGHT")
        self.assertIn("Missing tenant filter exposes reports", payload["comments"][0]["body"])
        self.assertEqual(skipped[0]["line"], 99)
        self.assertIn("1 inline comment", payload["body"])
        self.assertIn("Could not place inline", payload["body"])

    def test_cli_dry_run_writes_payload_without_calling_github(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmpdir = Path(tmp)
            pr_context = tmpdir / "pr-context.json"
            findings = tmpdir / "findings.json"
            pr_files = tmpdir / "pr-files.json"
            out = tmpdir / "payload.json"

            pr_context.write_text(
                json.dumps({"repo": "cogine-ai/local-ultra-review", "number": 12, "commit_sha": "abc123"}),
                encoding="utf-8",
            )
            findings.write_text(
                json.dumps(
                    {
                        "important": [
                            {
                                "title": "Inline issue",
                                "severity": "Important",
                                "category": "correctness",
                                "file": "app.py",
                                "line": 7,
                                "failure_scenario": "The new path crashes.",
                                "verification": {"summary": "Confirmed by static check."},
                            }
                        ],
                        "nits": [],
                    }
                ),
                encoding="utf-8",
            )
            pr_files.write_text(
                json.dumps([[{"filename": "app.py", "patch": "@@ -5,1 +7,2 @@\n+boom()\n"}]]),
                encoding="utf-8",
            )

            proc = subprocess.run(
                [
                    "python3",
                    "scripts/post-github-review.py",
                    "--pr-context",
                    str(pr_context),
                    "--findings",
                    str(findings),
                    "--pr-files",
                    str(pr_files),
                    "--mode",
                    "deep",
                    "--session-id",
                    "session-1",
                    "--dry-run",
                    "--out",
                    str(out),
                ],
                cwd=REPO_ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )

            result = json.loads(proc.stdout)
            payload = json.loads(out.read_text(encoding="utf-8"))
            self.assertTrue(result["ok"])
            self.assertEqual(result["posted"], False)
            self.assertEqual(payload["comments"][0]["path"], "app.py")


if __name__ == "__main__":
    unittest.main()
