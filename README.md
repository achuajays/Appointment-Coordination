# 🤖 Appointment Coordination Agent

A web automation agent using [browser-use](https://github.com/browser-use/browser-use) and FastAPI for automated website login and appointment scheduling.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)
![browser-use](https://img.shields.io/badge/browser--use-latest-orange)

## ✨ Features

- **🔐 Automated Login** - Log into websites automatically
- **📅 Appointment Scheduling** - Schedule appointments with provided details
- **🎯 Generic Task Execution** - Run any browser automation task
- **🚀 REST API** - FastAPI-powered endpoints with Swagger docs
- **🧠 AI-Powered** - Uses Google Gemini for intelligent automation

## 🏗️ Architecture

```
Appointment-Coordination/
├── main.py                 # FastAPI entry point
├── requirements.txt        # Dependencies
├── .env.example           # Environment template
└── src/
    ├── config.py          # Configuration management
    ├── agent/
    │   ├── factory.py     # Agent creation factory
    │   └── instructions.py # Agent system prompts
    └── api/
        ├── models.py      # Pydantic request/response models
        └── routes.py      # API endpoints
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment
pip install uv
uv venv --python 3.12

# Activate (Windows)
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Install browser-use chromium
uvx browser-use install
```

### 2. Configure Environment

```bash
# Copy example environment file
copy .env.example .env

# Edit .env and add your Google API key
```

Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 3. Run the Server

```bash
python main.py
```

The API will be available at `http://localhost:8000`.

## 📚 API Documentation

Access the interactive API docs at: **http://localhost:8000/docs**

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/task` | Run generic browser task |
| POST | `/login` | Perform website login |
| POST | `/schedule-appointment` | Schedule an appointment |

### Example: Generic Task

```bash
curl -X POST http://localhost:8000/task \
  -H "Content-Type: application/json" \
  -d '{
    "task": "Search for Python tutorials",
    "url": "https://google.com"
  }'
```

### Example: Login

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/login",
    "username": "user@example.com",
    "password": "yourpassword"
  }'
```

### Example: Schedule Appointment

```bash
curl -X POST http://localhost:8000/schedule-appointment \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/appointments",
    "username": "user@example.com",
    "password": "yourpassword",
    "appointment": {
      "appointment_type": "Consultation",
      "preferred_date": "2024-02-15",
      "preferred_time": "10:00 AM",
      "contact_name": "John Doe",
      "contact_email": "john@example.com"
    }
  }'
```

## ⚙️ Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `GOOGLE_API_KEY` | Google Gemini API key | Required |
| `DEBUG_MODE` | Enable debug logging | `false` |
| `DEFAULT_TIMEOUT` | Browser timeout (seconds) | `60` |
| `HEADLESS_MODE` | Run browser headless | `false` |

## 🔒 Security Notes

- **Never commit `.env` files** with real credentials
- For production, implement proper credential storage
- Use HTTPS in production environments
- Configure CORS appropriately for your use case

## 📄 License

MIT License
