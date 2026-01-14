"""
API Models Module

Pydantic models for request/response validation.
Simplified to only require patient_id and department.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response model."""
    
    status: str = Field(default="healthy", description="Service health status")
    timestamp: datetime = Field(default_factory=datetime.now, description="Current timestamp")
    version: str = Field(default="1.0.0", description="API version")


class AppointmentRequest(BaseModel):
    """Request model for booking appointment - only patient_id and department."""
    
    patient_id: str = Field(
        ...,
        min_length=1,
        description="Patient ID for the appointment"
    )
    department: str = Field(
        ...,
        min_length=1,
        description="Department name to select"
    )


class AgentResponse(BaseModel):
    """Response model for agent operations."""
    
    success: bool = Field(description="Whether the operation was successful")
    content: str = Field(description="Result or output from the agent")
    error: Optional[str] = Field(
        default=None,
        description="Error message if the operation failed"
    )
