# OrderPilot AI

OrderPilot AI is an enterprise-grade, AI-powered voice assistant system designed for fast food and quick-service restaurants. It replaces traditional phone ordering with a real-time conversational AI that transcribes speech, parses structured orders, and integrates with popular POS systems like Square and Clover.

The platform is designed for scalability, modularity, and real-world restaurant operations. It reduces labor costs, increases order throughput, and unifies multiple order channels into a seamless pipeline.

---

## Project Status

**Current Phase:** MVP – Phase 1: Twilio → Whisper Integration  
**Live Demo Support:** Local Docker-based deployment (in progress)  
**Production Goals:** Secure cloud deployment, CI/CD, and POS-confirmed transactions

---

## Core Features

| Feature               | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| Voice Order Handling  | AI assistant answers calls and processes real-time orders via phone         |
| Whisper Transcription | Converts customer speech to text using Whisper (local or OpenAI API)       |
| Order Parsing         | NLP pipeline extracts items, quantity, modifiers from transcribed input     |
| POS Integration       | Pushes structured orders to Square/Clover using secure APIs                 |
| SMS Confirmation      | Sends order confirmation or pickup code via Twilio                         |
| Admin Dashboard       | React-based UI for managing menu, logs, and configuration                   |
| Call Log Viewer       | Access timestamped logs of AI-handled orders for auditing                   |
| Modular Design        | Microservices structure allows for scalable and testable system evolution   |

---

## Tech Stack

| Layer               | Tools / Technologies                                 |
|---------------------|------------------------------------------------------|
| Backend API         | FastAPI, Python 3.11, Uvicorn                         |
| Speech-to-Text      | Whisper (OpenAI local/API)                           |
| NLP & Parsing       | Custom logic, LangChain (optional)                   |
| Voice Call Handling | Twilio Voice Webhooks                                |
| SMS Delivery        | Twilio Programmable Messaging                        |
| POS Integration     | Square API, Clover API                               |
| Frontend Dashboard  | React.js (Mobile/Desktop Responsive)                 |
| DevOps & Deploy     | Docker, Railway, Render (for MVP), AWS (future)      |
| Testing             | Pytest (backend), Jest (frontend), Postman           |

---

## Folder Structure
orderpilot-ai/
├── README.md
├── .env.template
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── api/
│ │ │ └── routes.py
│ │ ├── services/
│ │ │ ├── voice_agent.py
│ │ │ ├── order_parser.py
│ │ │ └── sms_sender.py
│ │ ├── pos/
│ │ │ └── square_api.py
│ │ └── db/
│ │ ├── models.py
│ │ └── menu_store.py
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ ├── pages/
│ │ └── App.jsx
│ ├── .env
│ └── package.json
├── scripts/
│ └── init_menu_upload.py
├── tests/
│ └── test_order_parser.py
---

## Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/yourname/orderpilot-ai.git
cd orderpilot-ai

2. Setup Environment
Copy and fill in your environment config:

cp .env.template .env
