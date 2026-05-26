import json
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class SessionLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        self.run_git("init")
        self.run_git("config", "user.email", "test@example.com")
        self.run_git("config", "user.name", "Test User")
        (self.repo / "app.py").write_text("print('hello')\n", encoding="utf-8")
        self.run_git("add", "app.py")
        self.run_git("commit", "-m", "initial")

    def tearDown(self):
        self.remove_registered_worktrees()
        self.tmp.cleanup()

    def run_git(self, *args, check=True):
        return subprocess.run(
            ["git", *args],
            cwd=self.repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=check,
        )

    def run_script(self, name, *args, check=True):
        return subprocess.run(
            ["bash", str(REPO_ROOT / "scripts" / name), *args],
            cwd=self.repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=check,
        )

    def remove_registered_worktrees(self):
        proc = self.run_git("worktree", "list", "--porcelain", check=False)
        lines = proc.stdout.splitlines()
        for line in lines:
            if not line.startswith("worktree "):
                continue
            path = Path(line.split(" ", 1)[1])
            if path != self.repo and str(path).startswith(str(self.repo)):
                subprocess.run(["git", "worktree", "remove", "--force", str(path)], cwd=self.repo, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def exclude_file(self):
        proc = self.run_git("rev-parse", "--git-path", "info/exclude")
        return self.repo / proc.stdout.strip()

    def prepare_session(self, session_id):
        proc = self.run_script("prepare-worktree.sh", "--session-id", session_id)
        payload = json.loads(proc.stdout)
        session_dir = self.repo / ".local-ultra-review" / session_id
        worktree = Path(payload["worktree"])
        return session_dir, worktree

    def test_prepare_worktree_adds_local_artifact_dir_to_git_exclude_once(self):
        self.prepare_session("session-exclude-1")
        self.prepare_session("session-exclude-2")

        exclude = self.exclude_file().read_text(encoding="utf-8")
        self.assertEqual(exclude.splitlines().count(".local-ultra-review/"), 1)

    def test_finalize_session_removes_worktree_by_default_and_keeps_report(self):
        session_dir, worktree = self.prepare_session("session-clean")
        (session_dir / "report.md").write_text("# Report\n", encoding="utf-8")

        proc = self.run_script("finalize-session.sh", "--session-dir", str(session_dir), "--status", "success")
        payload = json.loads(proc.stdout)

        self.assertTrue(payload["removed"])
        self.assertFalse(worktree.exists())
        self.assertTrue((session_dir / "report.md").exists())
        self.assertNotIn(str(worktree), self.run_git("worktree", "list", "--porcelain").stdout)

    def test_finalize_session_keeps_worktree_on_failure(self):
        session_dir, worktree = self.prepare_session("session-failed")

        proc = self.run_script("finalize-session.sh", "--session-dir", str(session_dir), "--status", "failure")
        payload = json.loads(proc.stdout)

        self.assertTrue(payload["kept"])
        self.assertTrue(worktree.exists())


if __name__ == "__main__":
    unittest.main()
