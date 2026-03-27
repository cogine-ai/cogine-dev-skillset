from typing import Dict, List, Optional
import time
from xianyu_api_client_skill import XianYuAPIClient

class XianYuProductManager:
    """闲鱼商品管理器"""
    
    def __init__(self, api_client: Optional[XianYuAPIClient] = None):
        """
        初始化商品管理器
        
        Args:
            api_client: API客户端实例，如果为None则自动创建
        """
        self.api_client = api_client or XianYuAPIClient()
        
        # AI服务商品模板库
        self.templates = {
            'basic': {
                'price': 29900,
                'original_price': 39900,
                'title': '🔥AI工作流定制｜自动化办公神器｜299元起',
                'content': self._get_basic_description()
            },
            'standard': {
                'price': 69900,
                'original_price': 89900,
                'title': '🚀AI工作流定制专家｜多平台集成｜699元',
                'content': self._get_standard_description()
            },
            'premium': {
                'price': 150000,
                'original_price': 199000,
                'title': '💎AI工作流定制大师｜企业级解决方案｜1500元',
                'content': self._get_premium_description()
            }
        }
    
    def _get_basic_description(self) -> str:
        """基础版服务描述"""
        return """【服务内容】
✅ 简单工作流程自动化
✅ 单平台数据处理  
✅ 基础AI助手搭建
✅ 3天内交付

【服务保障】
⭐ 专业AI开发者
⭐ 100%满意保证
⭐ 免费维护30天
⭐ 支持支付宝担保"""
    
    def _get_standard_description(self) -> str:
        """标准版服务描述"""
        return """【服务内容】
✅ 复杂业务流程自动化
✅ 多平台数据集成（钉钉/飞书/企业微信）
✅ 智能决策支持
✅ 5天内交付

【额外福利】
🎁 免费需求分析
🎁 使用培训文档
🎁 30天免费维护"""
    
    def _get_premium_description(self) -> str:
        """高级版服务描述"""
        return """【服务内容】
✅ 企业级复杂业务逻辑
✅ 定制化AI解决方案
✅ 多系统深度集成
✅ 专属技术支持
✅ 7天内交付

【尊享服务】
🏆 一对一需求分析
🏆 完整技术文档
🏆 90天免费维护
🏆 优先响应支持"""
    
    def generate_product_data(self, service_type: str, price_tier: str, 
                            custom_title: Optional[str] = None,
                            custom_content: Optional[str] = None) -> Dict[str, Any]:
        """
        生成商品数据
        
        Args:
            service_type: 服务类型（如 'workflow', 'chatbot', 'automation'）
            price_tier: 价格档次 ('basic', 'standard', 'premium')
            custom_title: 自定义标题（可选）
            custom_content: 自定义描述（可选）
            
        Returns:
            商品数据字典
        """
        if price_tier not in self.templates:
            raise ValueError(f"Invalid price tier: {price_tier}")
        
        template = self.templates[price_tier]
        
        return {
            "item_biz_type": 2,
            "sp_biz_type": 1,
            "channel_cat_id": "e11455b218c06e7ae10cfa39bf43dc0f",
            "price": template['price'],
            "original_price": template['original_price'],
            "express_fee": 0,
            "stock": 20,
            "outer_id": f"AI-{service_type.upper()}-{price_tier.upper()}-{int(time.time())}",
            "stuff_status": 100,
            "publish_shop": [{
                "title": custom_title or template['title'],
                "content": custom_content or template['content'],
                "service_support": "SDR"
            }]
        }
    
    def create_product(self, service_type: str, price_tier: str, 
                      custom_title: Optional[str] = None,
                      custom_content: Optional[str] = None) -> Dict[str, Any]:
        """
        创建单个商品
        
        Returns:
            API响应结果
        """
        product_data = self.generate_product_data(
            service_type, price_tier, custom_title, custom_content
        )
        return self.api_client.create_product(product_data)
    
    def create_batch_products(self, service_types: List[str], 
                            price_tiers: List[str]) -> List[Dict[str, Any]]:
        """
        批量创建商品
        
        Args:
            service_types: 服务类型列表
            price_tiers: 价格档次列表
            
        Returns:
            创建结果列表
        """
        results = []
        for service_type in service_types:
            for price_tier in price_tiers:
                try:
                    result = self.create_product(service_type, price_tier)
                    results.append({
                        'service_type': service_type,
                        'price_tier': price_tier,
                        'success': True,
                        'result': result
                    })
                except Exception as e:
                    results.append({
                        'service_type': service_type,
                        'price_tier': price_tier,
                        'success': False,
                        'error': str(e)
                    })
        return results