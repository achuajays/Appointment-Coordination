#!/usr/bin/env python3
"""
Appointment Booking Script

Custom workflow for logging into a website and scheduling an appointment.
Uses browser-use with Google Gemini for intelligent automation.

Usage:
    python book_appointment.py
"""

import asyncio
from dotenv import load_dotenv

load_dotenv()


async def book_appointment():
    """
    Main workflow:
    1. Open URL and login with credentials
    2. Ask user for patient ID and department
    3. Fill in the form and submit
    """
    from browser_use import Agent, Browser
    from browser_use import ChatGoogle
    import os
    
    # Get user input for appointment details
    print("\n" + "=" * 50)
    print("🏥 Appointment Booking System")
    print("=" * 50)
    
    # Get the URL from user
    url = input("\n📍 Enter the website URL: ").strip()
    if not url:
        url = "https://example.com/login"  # Default fallback
    
    # Get patient ID and department
    patient_id = input("🆔 Enter Patient ID: ").strip()
    department = input("🏢 Enter Department name: ").strip()
    
    print("\n⏳ Starting browser automation...")
    print("📧 Logging in with: tilox24103@atinjo.com")
    
    # Build the task prompt
    task = f"""
    STEP 1 - LOGIN:
    1. Go to {url}
    2. Find the email/username input field and enter: tilox24103@atinjo.com
    3. Find the password input field and enter: wedfwerdf
    4. Click the Sign In / Login button
    5. Wait for the page to load after login
    
    STEP 2 - FILL APPOINTMENT FORM:
    After successfully logging in:
    1. Find the patient ID input field and enter: {patient_id}
    2. Find the department dropdown and select: {department}
    3. Click the Submit button
    4. Wait for confirmation
    
    Report any errors encountered during the process.
    Confirm when the appointment form has been submitted successfully.
    """
    
    # Create the LLM
    llm = ChatGoogle(
        model="gemini-2.0-flash",
        api_key=os.getenv("GOOGLE_API_KEY"),
    )
    
    # Create browser (visible mode for debugging)
    browser = Browser(
        headless=False,
    )
    
    # Create and run the agent
    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
        max_actions_per_step=10,
    )
    
    print("\n🤖 Agent is working...")
    print("-" * 50)
    
    try:
        result = await agent.run()
        print("\n" + "=" * 50)
        print("✅ Task Complete!")
        print("=" * 50)
        print(f"\nResult: {result}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        await browser.close()


if __name__ == "__main__":
    asyncio.run(book_appointment())
