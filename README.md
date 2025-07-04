## OrderPilot AI

OrderPilot AI is a modular, AI-powered voice assistant platform built for fast food and quick-service restaurants.

It replaces phone operators with a real-time AI assistant that transcribes customer speech, parses structured orders, and pushes them into popular POS systems like Square or Clover.  
Built for scalability, maintainability, and multi-store operations.

---

## Project Status

| Phase | Description                       | Status       |
|-------|-----------------------------------|--------------|
| 1     | Twilio → Whisper Transcription    | In Progress  |
| 2     | Order Parsing + POS Integration   | Planned      |
| 3     | SMS Confirmation Pipeline         | Planned      |
| 4     | Admin Dashboard UI                | Planned      |
| 5     | Loyalty/Upselling AI              | Future       |
| 6     | Multilingual Voice Input          | Future       |
| 7     | Predictive Analytics Dashboard    | Future       |

---

## Core Features

| Feature               | Description                                                              |
|-----------------------|--------------------------------------------------------------------------|
| AI Voice Assistant    | Handles phone calls and processes orders via voice                       |
| Whisper Integration   | Transcribes customer speech using OpenAI Whisper (API or local)          |
| Order Parser Engine   | Converts transcribed text into structured menu orders                    |
| POS Integration       | Pushes orders into Square or Clover using authenticated REST APIs        |
| SMS Notifications     | Sends confirmation codes and order summaries using Twilio SMS            |
| Admin Dashboard       | Manage menu, track call logs, configure API keys (React frontend)        |
| Modular Microservices | Separated layers for speech, parsing, POS, and messaging for scalability |

---

## Tech Stack

| Layer               | Technology                                |
|---------------------|--------------------------------------------|
| Backend API         | Python 3.11, FastAPI, Uvicorn              |
| Speech-to-Text      | Whisper (local or OpenAI API)              |
| NLP Parsing         | Custom logic, LangChain (optional)         |
| Voice Input         | Twilio Programmable Voice                  |
| SMS Delivery        | Twilio Programmable Messaging              |
| POS Integration     | Square API, Clover API                     |
| Frontend Dashboard  | React.js, Vite, Tailwind CSS               |
| DevOps              | Docker, Railway, GitHub Actions, AWS       |
| Testing             | Pytest (backend), Jest (frontend), Postman |

---

## Folder Structure

```text
orderpilot-ai/
├── README.md
├── .env.template
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   └── routes.py
│   │   ├── services/
│   │   │   ├── voice_agent.py
│   │   │   ├── order_parser.py
│   │   │   └── sms_sender.py
│   │   ├── pos/
│   │   │   └── square_api.py
│   │   └── db/
│   │       ├── models.py
│   │       └── menu_store.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   ├── .env
│   └── package.json
├── scripts/
│   └── init_menu_upload.py
├── tests/
│   └── test_order_parser.py
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/orderpilot-ai.git
cd orderpilot-ai
```

### 2. Setup Environment Variables

```bash
cp .env.template .env
# Fill in:
# - TWILIO_ACCOUNT_SID
# - TWILIO_AUTH_TOKEN
# - OPENAI_API_KEY
# - SQUARE_ACCESS_TOKEN / CLOVER_API_KEY
```

### 3. Start the Backend (FastAPI)

```bash
cd backend
uvicorn app.main:app --reload
```

### 4. Start the Frontend (React)

```bash
cd frontend
npm install
npm start
```

---

## API Endpoints

### Transcription

```http
POST /call-transcribe
```

- Input: audio file (.wav or .mp3)
- Output: JSON with transcription text

### POS Order Push

```http
POST /send-order
```

- Input: JSON with structured order
- Output: order status and ID

### Menu API

```http
GET /menu
POST /menu
PUT /menu/:item_id
```

Used by the admin dashboard for menu management.

---

## Testing

### Run Backend Tests

```bash
cd backend
pytest
```

### Run Frontend Tests

```bash
cd frontend
npm test
```

### Test API Locally

Use Postman or curl to test endpoints:

```http
POST /call-transcribe
POST /send-order
```

---

## Deployment Strategy

- Phase 1: Run locally with Docker or Railway
- Phase 2: Setup CI/CD with GitHub Actions
- Phase 3: Deploy to AWS or GCP with HTTPS and backups

---

## Security & Compliance

- Secrets stored in `.env` and excluded from Git
- HTTPS enforced for all external communication
- Twilio call verification to prevent spoofing
- Minimal logging for GDPR safety
- HIPAA-ready modular architecture

---

## License

MIT License  
© 2025 Adam Kadwory / Sumer Medical Technology Inc.
