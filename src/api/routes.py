"""
API Routes Module

FastAPI route handlers for appointment booking.
Simplified - only accepts patient_id and department.
URL and credentials come from .env file.
"""

import uuid
from datetime import datetime

from fastapi import APIRouter, HTTPException

from src.api.models import (
    HealthResponse,
    AppointmentRequest,
    AgentResponse,
)
from src.agent import create_browser_agent
from src.config import settings


# Create router
router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check() -> HealthResponse:
    """
    Health check endpoint.
    
    Returns the service health status, timestamp, and version.
    """
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now(),
        version="1.0.0"
    )


@router.post("/book-appointment", response_model=AgentResponse, tags=["Agent"])
async def book_appointment(request: AppointmentRequest) -> AgentResponse:
    """
    Book an appointment.
    
    Only requires patient_id and department.
    URL and login credentials are read from environment variables.
    """
    try:
        # Build the task prompt using settings from .env
        task_prompt = f"""
        STEP 1 - LOGIN:
        1. Go to {settings.website_url}
        2. Find the email/username input field and enter: {settings.login_email}
        3. Find the password input field and enter: {settings.login_password}
        4. Click the Sign In / Login button
        5. Wait for the page to load after login
        
        STEP 2 - FILL APPOINTMENT FORM:
        After successfully logging in:
        1. Find the patient ID input field and enter: {request.patient_id}
        2. Find the department dropdown and select: {request.department}
        3. Click the Submit button
        4. Wait for confirmation
        
        Report any errors encountered during the process.
        Confirm when the appointment form has been submitted successfully.
        """
        
        # Create and run the agent
        agent = await create_browser_agent(task=task_prompt)
        result = await agent.run()
        
        # Extract content from result
        content = str(result.final_result()) if hasattr(result, 'final_result') else str(result)
        
        return AgentResponse(
            success=True,
            content=content,
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Appointment booking failed: {str(e)}"
        )
