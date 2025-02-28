from datetime import datetime
import requests
from config import DIFY_API_KEY, DIFY_API_URL


# 将时间转化为星期
def get_weekday(date_str: str, date_format: str = "%Y-%m-%d") -> str:
    """
    将日期字符串转换为星期几。

    参数:
    - date_str: 日期字符串，格式为 date_format 指定的格式。
    - date_format: 日期字符串的格式，默认为 "%Y-%m-%d %H:%M:%S"。

    返回:
    - 星期几的字符串，例如 "星期一"、"星期二"等。
    """
    try:
        # 将字符串转换为 datetime 对象
        date_obj = datetime.strptime(date_str, date_format)

        # 获取星期几并转换为中文格式
        weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周天"]

        # 返回对应的星期几
        return weekdays[date_obj.weekday()]
    except ValueError:
        return "无效日期格式"


# 发送到 Dify 接口的函数
def call_dify_api(payload):
    try:
        headers = {
            'Authorization': DIFY_API_KEY,
            'Content-Type': 'application/json'
        }

        # 请求 DIFY API
        response = requests.post(
            DIFY_API_URL,
            headers=headers,
            json=payload
        )

        # 解析 JSON 响应
        response_json = response.json()

        # 提取所需的字段
        answer = response_json.get("answer")
        conversation_id = response_json.get("conversation_id")

        # 返回所需的内容
        return {
            "answer": answer,
            "conversation_id": conversation_id
        }

    except Exception as e:
        print("Error:", str(e))
        return None
