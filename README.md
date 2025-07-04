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

---

## Getting Started
### 1. Clone the Repository

```bash
git clone https://github.com/yourname/orderpilot-ai.git
cd orderpilot-ai


2.Setup Environment Variables
cp .env.template .env
# Fill in:
# - TWILIO_ACCOUNT_SID
# - TWILIO_AUTH_TOKEN
# - OPENAI_API_KEY
# - SQUARE_ACCESS_TOKEN / CLOVER_API_KEY

3. Start the Backend (FastAPI)
cd backend
uvicorn app.main:app --reload

4. Start the Frontend (React)
cd frontend
npm install
npm start


API Reference (MVP)
Transcription Endpoint
POST /call-transcribe
Input: Audio file (.wav or .mp3)
Output: JSON with transcribed text

POS Order Push
POST /send-order
Input: JSON with structured order (items, modifiers, quantities)
Output: Order confirmation + status

Menu Management (Admin UI)
GET /menu

POST /menu

PUT /menu/:item_id

 Testing
Run Backend Tests (Pytest)
cd backend
pytest

Run Frontend Tests (Jest)
cd frontend
npm test
API Testing (Optional)
Use Postman to test:

POST /call-transcribe

POST /send-order


Security & Compliance
Environment secrets stored in .env, not committed to GitHub

HTTPS enforced in deployment via Railway, Render, or AWS

Twilio webhook signature validation for call spoof protection

GDPR-friendly minimal log retention

HIPAA-aligned modular structure (for future use cases)


---






