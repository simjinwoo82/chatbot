from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests, os
from dotenv import load_dotenv

load_dotenv()  # .env의 키를 추출하는 함수
app = FastAPI()
print(app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Msg(BaseModel):
    text: str


HF_URL = "https://router.huggingface.co/v1/chat/completions"
HF_MODEL = "Qwen/Qwen3-4B-Instruct-2507"


def ask_ai(q: str) -> str:
    token = os.getenv("HF_TOKEN")
    if not token:
        return "서버 설정 오류: HF_TOKEN이 없습니다. .env 파일을 확인해주세요."

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": HF_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "당신은 한국어로 답하는 친절하고 정확한 챗봇입니다. 답변은 항상 한국어로 하고, 간결하고 자연스럽게 설명하세요.",
            },
            {"role": "user", "content": q},
        ],
        "max_tokens": 300,
        "temperature": 0.7,
    }

    try:
        res = requests.post(HF_URL, headers=headers, json=payload, timeout=60)
        res.raise_for_status()
        data = res.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"AI 응답 중 오류가 발생했습니다: {str(e)}"


@app.post("/chat")
def chat(msg: Msg):
    reply = ask_ai(msg.text)
    return {"reply": reply}
