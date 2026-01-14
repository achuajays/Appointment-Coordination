#!/usr/bin/env python3
"""
Appointment Coordination Agent - FastAPI Server

A FastAPI backend for browser automation using browser-use.
Enables automated website login and appointment scheduling.

Usage:
    python main.py

Endpoints:
    GET  /health              - Health check
    POST /task                - Run generic browser automation task
    POST /login               - Perform website login
    POST /schedule-appointment - Schedule an appointment

Environment Variables Required:
    GOOGLE_API_KEY - Your Google API key for Gemini

See .env.example for all configuration options.
"""

import sys
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Verify configuration on import
try:
    from src.config import settings
except Exception as e:
    print(f"❌ Configuration Error: {e}", file=sys.stderr)
    sys.exit(1)

from src.api import router


# Create FastAPI application
app = FastAPI(
    title="Appointment Coordination Agent API",
    description="Browser automation for login and appointment scheduling",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Appointment Coordination Agent API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
        "endpoints": {
            "task": "POST /task - Run generic browser task",
            "login": "POST /login - Perform website login",
            "appointment": "POST /schedule-appointment - Schedule appointment",
        }
    }


def main() -> int:
    """Run the FastAPI server."""
    print("\n" + "=" * 60)
    print("🤖 Appointment Coordination Agent API")
    print("=" * 60)
    print(f"\n📍 Server: http://localhost:8000")
    print(f"📖 Docs:   http://localhost:8000/docs")
    print(f"💚 Health: http://localhost:8000/health")
    print("\nPress Ctrl+C to stop.\n")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug_mode,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
