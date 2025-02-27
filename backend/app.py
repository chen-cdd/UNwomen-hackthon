from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有域名访问

DIFY_API_URL = 'https://api.dify.ai/v1/chat-messages'
DIFY_API_KEY = 'Bearer app-cdD5bx7mufjIVrCDCyvHsqTJ'  # 替换为你的 API 密钥

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')

    # 调用 Dify API
    response = requests.post(DIFY_API_URL, json={
        "inputs": {},
        "query": user_message,
        "response_mode": "streaming",
        "conversation_id": "",  # 可以根据需要设置
        "user": "abc-123",  # 用户 ID
        "files": []  # 如果有文件可以添加
    }, headers={
        'Authorization': DIFY_API_KEY,
        'Content-Type': 'application/json'
    }, verify=False)  # 禁用 SSL 验证

    # 打印响应状态码和内容
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")

    if response.status_code == 200:
        try:
            response_data = response.json()
            # 提取最后一个 message 事件中的 answer
            messages = response_data.get('data', {}).get('outputs', {}).get('answer', '没有响应')
            return jsonify({"response": messages})
        except ValueError:
            return jsonify({"error": "无法解析响应为 JSON", "details": response.text}), 500
    else:
        return jsonify({"error": "请求失败", "details": response.text}), 500

if __name__ == '__main__':
    app.run(debug=True)
