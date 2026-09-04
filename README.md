# 🤖 AI Chatbot

FastAPI 백엔드와 React(Vite) 프론트엔드로 구성된 AI 챗봇 애플리케이션입니다.  
Hugging Face Inference API를 활용하여 사용자의 질문에 한국어로 친절하게 답변합니다.

---

## 🛠️ 기술 스택 (Tech Stack)

### Backend
- **Python 3.14+**
- **FastAPI**
- **Uvicorn**
- **Hugging Face Inference API** (Qwen/Qwen3-4B-Instruct)

### Frontend
- **React 19**
- **Vite**
- **CSS3**

---

## 📁 프로젝트 구조 (Directory Structure)

```
chatbot/
├── backend/
│   ├── .env.example
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
└── README.md
```

---

## 🚀 시작하기 (Getting Started)

### 1. Backend 실행 방법

```bash
cd backend

# 가상환경 생성 및 활성화 (Windows)
python -m venv .venv
.venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# .env 파일 생성 및 Hugging Face 토큰 설정
# .env.example 파일을 참고하여 .env 파일을 생성하세요.
# HF_TOKEN=your_huggingface_token_here

# 서버 실행
uvicorn main:app --reload --port 8000
```

### 2. Frontend 실행 방법

```bash
cd frontend

# 의존성 설치
npm install

# 개발 서버 실행
npm run dev
```

브라우저에서 `http://localhost:5173`으로 접속하여 챗봇을 사용할 수 있습니다.
