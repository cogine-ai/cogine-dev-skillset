import os
import json
import time
import hashlib
import http.client
from typing import Dict, Any, Optional

class XianYuAPIClient:
    """闲鱼管家API客户端"""
    
    def __init__(self, app_key: Optional[str] = None, app_secret: Optional[str] = None):
        """
        初始化API客户端
        
        Args:
            app_key: 闲鱼应用Key，如果为None则从环境变量读取
            app_secret: 闲鱼应用密钥，如果为None则从环境变量读取
        """
        self.app_key = app_key or os.getenv('XIAN_YU_APP_KEY')
        self.app_secret = app_secret or os.getenv('XIAN_YU_APP_SECRET')
        self.domain = "https://open.goofish.pro"
        self.api_host = "api.goofish.pro"
        
        if not self.app_key or not self.app_secret:
            raise ValueError("XIAN_YU_APP_KEY and XIAN_YU_APP_SECRET must be provided")
    
    def _generate_sign(self, body_json: str, timestamp: int) -> str:
        """生成API签名"""
        # 对请求体进行MD5
        m = hashlib.md5()
        m.update(body_json.encode('utf-8'))
        body_md5 = m.hexdigest()
        
        # 拼接签名字符串: appKey,bodyMd5,timestamp,appSecret
        sign_string = f"{self.app_key},{body_md5},{timestamp},{self.app_secret}"
        
        # 对拼接字符串进行MD5
        m = hashlib.md5()
        m.update(sign_string.encode('utf-8'))
        return m.hexdigest()
    
    def request(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        发送API请求
        
        Args:
            endpoint: API端点路径，如 "/api/open/product/create"
            data: 请求数据字典
            
        Returns:
            API响应数据字典
        """
        # 将json对象转成json字符串，必须去除空格
        body = json.dumps(data, separators=(',', ':'))
        
        # 时间戳（秒）
        timestamp = int(time.time())
        
        # 生成签名
        sign = self._generate_sign(body, timestamp)
        
        # 构建完整URL
        url = f"{endpoint}?appid={self.app_key}&timestamp={timestamp}&sign={sign}"
        
        # 设置请求头
        headers = {"Content-Type": "application/json"}
        
        try:
            # 发送HTTPS请求
            conn = http.client.HTTPSConnection(self.api_host)
            conn.request("POST", url, body, headers)
            response = conn.getresponse()
            response_data = response.read().decode('utf-8')
            conn.close()
            
            # 解析JSON响应
            return json.loads(response_data)
            
        except Exception as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def create_product(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
        """创建商品的便捷方法"""
        return self.request("/api/open/product/create", product_data)
    
    def get_product_detail(self, product_id: str) -> Dict[str, Any]:
        """获取商品详情的便捷方法"""
        return self.request("/api/open/product/detail", {"product_id": product_id})