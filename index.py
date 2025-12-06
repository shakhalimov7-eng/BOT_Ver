# vercel-python: fastapi
# vercel-python: requests
# vercel-python: uvicorn

import os
import json
from fastapi import FastAPI, Request, Response
import requests

app = FastAPI()

TELEGRAM_BOT_TOKEN = os.environ.get("7087980222:AAFzaZ3aIpwh2O-sIjZUCL5Dgsq9WeNScFw")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

@app.get("/")
async def root():
    return {"status": "Bot ishlayapti"}

@app.post("/api/webhook")
async def webhook(request: Request):
    try:
        data = await request.json()
        
        if "message" in data:
            message = data["message"]
            chat_id = message["chat"]["id"]
            
            if "text" in message:
                user_text = message["text"]
                reply_text = f"Siz yozdingiz: {user_text}"
                
                send_message(chat_id, reply_text)
        
        return Response(status_code=200)
    
    except Exception as e:
        print(f"Xato: {e}")
        return Response(status_code=200)

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

# Vercel uchun handler
handler = app