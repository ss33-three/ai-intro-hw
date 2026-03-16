import requests
import os
from dotenv import load_dotenv

# 加载.env文件中的API密钥（避免硬编码）
load_dotenv()

def deepseek_chat(question):
    """调用DeepSeek API实现对话"""
    # 获取API Key
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        print("❌ 错误：请先在.env文件中配置DEEPSEEK_API_KEY")
        return None

    # API请求配置
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": question}],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    try:
        # 发送请求并获取回复
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"❌ 调用失败：{str(e)}")
        return None

if __name__ == "__main__":
    print("🎉 DeepSeek Chatbot 启动（输入'退出'结束）")
    while True:
        user_input = input("\n你：")
        if user_input.strip() == "退出":
            print("👋 对话结束！")
            break
        reply = deepseek_chat(user_input)
        if reply:
            print(f"AI：{reply}")