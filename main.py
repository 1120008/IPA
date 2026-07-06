import os
import json
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import requests
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# ================= CONFIGURATION SECURITY LABELS =================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_KEY")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID", "YOUR_SPREADSHEET_ID")
# =================================================================

class ChatInput(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Mengarahkan halaman utama ke template HTML
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/v1/discussion/filter")
async def filter_discussion(data: ChatInput):
    """Menyaring konten diskusi 24/7 menggunakan kecerdasan buatan AI Guardrails"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o",
        "response_format": { "type": "json_object" },
        "messages": [
            {
                "role": "system", 
                "content": "Kamu sistem moderasi otomatis sains IPA. Balas hanya dengan JSON: {'status': 'APPROVED'} atau {'status': 'REJECTED', 'reason': '...'}. REJECTED jika ada unsur dogma/opini agama, kekerasan, atau asusila."
            },
            {"role": "user", "content": data.text}
        ]
    }
    res = requests.post(url, json=payload, headers=headers).json()
    result = json.loads(res['choices'][0]['message']['content'])
    
    if result["status"] == "REJECTED":
        return {"status": "REJECTED", "message": f"Diblokir AI: {result['reason']}"}
    return {"status": "APPROVED", "message": data.text}

@app.post("/api/v1/chatbot/socratic")
async def socratic_bot(data: ChatInput):
    """Memicu interaksi bimbingan sokratik tanpa memberikan jawaban langsung"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system", 
                "content": "Kamu adalah Chatbot Sokratik IPA. Siswa menganalisis Virus, Gunung, dan Makhluk Hidup. JANGAN PERNAH memberikan kesimpulan jawaban langsung. Berikan pertanyaan pemantik logika!"
            },
            {"role": "user", "content": data.text}
        ]
    }
    res = requests.post(url, json=payload, headers=headers).json()
    return {"reply": res['choices'][0]['message']['content']}
