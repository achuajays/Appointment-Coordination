# 🤖 Appointment Coordination Agent

<p align="center">
  <img src="assets/banner.png" alt="Appointment Coordination Agent Banner" width="100%">
</p>

<p align="center">
  <strong>AI-powered browser automation for website login and appointment scheduling</strong>
</p>

<p align="center">
  <a href="https://github.com/achuajays/Appointment-Coordination">
    <img src="https://img.shields.io/badge/GitHub-Repository-blue?logo=github" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/browser--use-0.11+-orange" alt="browser-use">
</p>

---

## 📖 Overview

The **Appointment Coordination Agent** is an intelligent web automation system that uses AI to navigate websites, log in with credentials, and schedule appointments automatically. Built with [browser-use](https://github.com/browser-use/browser-use) and FastAPI.

---

## 🏗️ Architecture

```mermaid
flowchart TB
    subgraph Client["👤 Client"]
        API[("REST API Request<br/>POST /book-appointment")]
    end

    subgraph FastAPI["⚡ FastAPI Server"]
        Routes["Routes<br/>/health, /book-appointment"]
        Models["Pydantic Models<br/>Request Validation"]
    end

    subgraph Agent["🤖 Browser-Use Agent"]
        Factory["Agent Factory"]
        LLM["LLM Provider<br/>(Groq/OpenAI/Gemini)"]
        Browser["🌐 Chromium Browser"]
    end

    subgraph Target["🏥 Target Website"]
        Login["Login Page"]
        Form["Appointment Form"]
        Confirm["Confirmation"]
    end

    API --> Routes
    Routes --> Models
    Models --> Factory
    Factory --> LLM
    Factory --> Browser
    Browser --> Login
    Login --> Form
    Form --> Confirm
    Confirm --> API

    style Client fill:#e1f5fe
    style FastAPI fill:#fff3e0
    style Agent fill:#f3e5f5
    style Target fill:#e8f5e9
```

---

## 🔄 How It Works

```mermaid
sequenceDiagram
    participant U as 👤 User
    participant A as ⚡ API
    participant F as 🏭 Factory
    participant L as 🧠 LLM
    participant B as 🌐 Browser
    participant W as 🏥 Website

    U->>A: POST /book-appointment<br/>{patient_id, department}
    A->>F: Create Browser Agent
    F->>L: Initialize LLM (Groq)
    F->>B: Launch Chromium
    
    B->>W: Navigate to login URL
    L->>B: "Enter email field"
    B->>W: Fill email & password
    L->>B: "Click login button"
    B->>W: Submit login
    
    W-->>B: Dashboard loaded
    L->>B: "Find patient ID field"
    B->>W: Enter patient ID
    L->>B: "Select department"
    B->>W: Choose from dropdown
    L->>B: "Click submit"
    B->>W: Submit form
    
    W-->>B: Confirmation page
    B-->>A: Task completed
    A-->>U: {success: true, content: "Appointment booked"}
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔐 **Auto Login** | Automatically logs into websites with credentials |
| 📅 **Appointment Booking** | Fills forms and schedules appointments |
| 🧠 **AI-Powered** | Uses LLM to understand and navigate any website |
| 🚀 **REST API** | Simple FastAPI endpoints for integration |
| ⚙️ **Configurable** | All settings via environment variables |

---

## 📁 Project Structure

```
Appointment-Coordination/
├── main.py                 # FastAPI entry point
├── requirements.txt        # Dependencies
├── .env.example           # Environment template
├── assets/
│   └── banner.png         # Project banner
└── src/
    ├── config.py          # Configuration management
    ├── agent/
    │   ├── factory.py     # Agent creation
    │   └── instructions.py # System prompts
    └── api/
        ├── models.py      # Request/Response models
        └── routes.py      # API endpoints
```

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/achuajays/Appointment-Coordination.git
cd Appointment-Coordination

# Create virtual environment
pip install uv
uv venv --python 3.12
.venv\Scripts\activate  # Windows

# Install dependencies
uv pip install -r requirements.txt
uvx browser-use install
```

### 2. Configure Environment

```bash
copy .env.example .env
```

Edit `.env` with your settings:
```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=meta-llama/llama-4-scout-17b-16e-instruct
WEBSITE_URL=https://your-appointment-site.com/login
LOGIN_EMAIL=your_email@example.com
LOGIN_PASSWORD=your_password
```

### 3. Run the Server

```bash
python main.py
```

Server available at: **http://localhost:8000**

---

## 📚 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/book-appointment` | Book an appointment |

### Example Request

```bash
curl -X POST http://localhost:8000/book-appointment \
  -H "Content-Type: application/json" \
  -d '{
    "patient_id": "PAT-12345",
    "department": "Cardiology"
  }'
```

### Example Response

```json
{
  "success": true,
  "content": "Successfully logged in and submitted appointment for patient PAT-12345 in Cardiology department.",
  "error": null
}
```

---

## ⚙️ Configuration

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Groq API key for LLM | ✅ |
| `GROQ_MODEL` | Model ID (must support vision) | ✅ |
| `WEBSITE_URL` | Target website login URL | ✅ |
| `LOGIN_EMAIL` | Login email/username | ✅ |
| `LOGIN_PASSWORD` | Login password | ✅ |
| `DEBUG_MODE` | Enable debug logging | ❌ |
| `HEADLESS_MODE` | Run browser headless | ❌ |

---

## 🔒 Security Notes

> ⚠️ **Important**: Never commit `.env` files with real credentials to version control.

- Credentials are stored in environment variables only
- For production, use secure credential management
- Configure CORS appropriately for your deployment

---

## 📄 License

MIT License

---

<p align="center">
  Built with ❤️ using <a href="https://github.com/browser-use/browser-use">browser-use</a> and <a href="https://fastapi.tiangolo.com/">FastAPI</a>
</p>
