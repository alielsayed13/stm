from pyrogram import Client, filters
import requests
import json

app = Client(
    "Bot",
    api_id=10823881,
    api_hash="339886e2109eb67203ce12022b32e035",
    bot_token="5995522924:AAGLnoWxgPz3ovkfd5yphG6OJaYskHjCN80"
)

url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'

def gpt(text) -> str:
    headers = {
        'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
        'Connection': 'keep-alive',
        'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
        'Accept': '*/*',
        'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
        'Content-Type': 'application/json',
        'Accept-Language': 'en-GB,en;q=0.9'
    }

    data = {
        'data': {
            'message':text,
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        result = response.json()["result"]["choices"][0]["text"]
        return result
    except:
        return None

def reply_gpt(client, message):
    text = message.text.split("/gpt ")[1]
    reply_text = gpt(text)
    chat_id = message.chat.id
    message_id = message.message_id
    client.send_message(chat_id=chat_id, text=reply_text + "\n\n\n **تم استخدام أحدث إصدار من الذكاء الاصطناعي 3.5 turbo**\n ** شكرا للمطور علي** @G5_7B", reply_to_message_id=message_id)

@app.on_message(filters.command("gpt"))
def reply(client, message):
    message.reply_text("تم استلام سؤالك، يرجى الانتظار حتى يتم الرد عليك...")
    reply_gpt(client, message)

print("bot start now♥")
app.run()
