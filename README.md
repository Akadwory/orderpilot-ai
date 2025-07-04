OrderPilot AI
OrderPilot AI is a modular, AI-powered voice assistant platform built for fast food and quick-service restaurants.

It replaces phone operators with a real-time AI assistant that transcribes customer speech, parses structured orders, and pushes them into popular POS systems like Square or Clover.
Built for scalability, maintainability, and multi-store operations.

Project Status
Phase

Description

Status

1

Twilio → Whisper Transcription

Completed

2

Order Parsing + POS Integration

In Progress

3

SMS Confirmation Pipeline

Planned

4

Admin Dashboard UI

Planned

5

Loyalty/Upselling AI

Future

6

Multilingual Voice Input

Future

7

Predictive Analytics Dashboard

Future

Core Features
Feature

Description

AI Voice Assistant

Handles phone calls and processes orders via voice

Whisper Integration

Transcribes customer speech using OpenAI Whisper (API or local)

Order Parser Engine

Converts transcribed text into structured menu orders

POS Integration

Pushes orders into Square or Clover using authenticated REST APIs

SMS Notifications

Sends confirmation codes and order summaries using Twilio SMS

Admin Dashboard

Manage menu, track call logs, configure API keys (React frontend)

Modular Microservices

Separated layers for speech, parsing, POS, and messaging for scalability

Tech Stack
Layer

Technology

Backend API

Python 3.11, FastAPI, Uvicorn

Speech-to-Text

Whisper (local or OpenAI API)

NLP Parsing

Custom logic, LangChain (optional)

Voice Input

Twilio Programmable Voice

SMS Delivery

Twilio Programmable Messaging

POS Integration

Square API, Clover API

Frontend Dashboard

React.js, Vite, Tailwind CSS

DevOps

Docker, Railway, GitHub Actions, AWS

Testing

Pytest (backend), Jest (frontend), Postman

Folder Structure
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

Getting Started
1. Clone the Repository
git clone https://github.com/yourname/orderpilot-ai.git
cd orderpilot-ai

2. Setup Environment Variables
cp .env.template .env
# Fill in:
# - TWILIO_ACCOUNT_SID
# - TWILIO_AUTH_TOKEN
# - OPENAI_API_KEY
# - SQUARE_ACCESS_TOKEN / CLOVER_API_KEY

3. Start Backend (FastAPI)
cd backend
uvicorn app.main:app --reload

4. Start Frontend (React)
cd frontend
npm install
npm start

API Endpoints (MVP)
Transcription
POST /call-transcribe

Accepts: audio file (.wav, .mp3)
Returns: JSON with transcription text

POS Order Push
POST /send-order

Accepts: structured JSON
Sends order to Square/Clover
Returns: status + order ID

Menu Management
GET /menu
POST /menu
PUT /menu/:item_id

Used by admin dashboard to manage the menu

Testing
Run Backend Tests
cd backend
pytest

Run Frontend Tests
cd frontend
npm test

Optional API Testing
Use Postman to test:

POST /call-transcribe

POST /send-order

Security & Compliance
All secrets are managed via .env and environment variables

HTTPS enforced in cloud deployments

Minimal logging for GDPR compliance

Twilio call verification to block spoofing

Modular security layers (HIPAA-aligned structure)

Deployment Strategy
Phase 1: MVP
Run via Docker or Railway (for demo)

Manual deploy for backend/frontend

Phase 2: Production
CI/CD via GitHub Actions

Deploy to AWS/GCP

Enable database + encrypted volume backup

Roadmap
This section details the planned development phases for OrderPilot AI, providing a clearer picture of our future direction.

✅ Phase 1: Twilio → Whisper Transcription (Completed)
Objective: Establish a robust pipeline for real-time voice input transcription.

Key Deliverables:

Twilio Programmable Voice integration for call handling.

OpenAI Whisper API integration for accurate speech-to-text conversion.

Basic API endpoint for audio submission and transcription retrieval.

⏳ Phase 2: Order Parsing & POS Integration (In Progress)
Objective: Develop the core logic for translating transcribed speech into structured orders and pushing them to POS systems.

Key Deliverables:

Order Parser Engine: Custom NLP logic to identify menu items, quantities, and modifiers from transcribed text.

POS Adapters: Integration with Square API for pushing new orders.

Error Handling: Mechanisms for managing invalid orders or POS communication failures.

⏳ Phase 3: SMS Confirmation Pipeline (Planned)
Objective: Implement a system for sending order confirmations and updates to customers via SMS.

Key Deliverables:

Twilio Programmable Messaging integration for sending SMS.

Automated SMS dispatch upon successful order placement.

Option for customers to receive order summaries and confirmation codes.

⏳ Phase 4: Admin Dashboard (Menu + Logs) (Planned)
Objective: Create a user-friendly web interface for restaurant owners to manage their menu and monitor system activity.

Key Deliverables:

React Frontend: Intuitive UI for menu item creation, editing, and deletion.

Call Logs: Display of transcribed calls and order statuses for troubleshooting and analysis.

Configuration Management: Ability to manage API keys and system settings.

🔜 Phase 5: Loyalty & Upselling Engine (Future)
Objective: Enhance the AI with capabilities to recognize customer loyalty and suggest upsells.

Key Deliverables:

Integration with loyalty programs.

AI logic for personalized upsell recommendations based on order history or current trends.

🔜 Phase 6: Multilingual Voice Input (Arabic, Spanish) (Future)
Objective: Expand the AI's language capabilities to cater to a broader customer base.

Key Deliverables:

Support for transcribing and understanding orders in Arabic and Spanish.

Potential integration with other language models.

🔜 Phase 7: Inventory Analytics + Forecasting (Future)
Objective: Provide valuable insights to restaurant owners regarding inventory and demand.

Key Deliverables:

Dashboard displaying real-time inventory levels.

Predictive analytics for forecasting popular items and demand fluctuations.

Learn & Contribute
OrderPilot AI is being built to teach real-world AI voice systems using:

Voice + NLP + POS integration

Full-stack architecture with frontend/backend split

Modular service-based logic (production-ready patterns)

If you're a restaurant owner, ML developer, or engineer — you’re welcome to explore and contribute.

License
MIT License

© 2025 Adam Kadwory / Sumer Medical Technology Inc.