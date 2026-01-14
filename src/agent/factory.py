"""
Agent Factory Module

Creates and configures browser automation agent instances.
Uses browser-use library with Groq LLM.
"""

from typing import Optional

from browser_use import Agent, Browser

from src.config import Settings, settings
from src.agent.instructions import AGENT_INSTRUCTIONS, AGENT_NAME


def create_llm(config: Settings):
    """
    Create the LLM model instance for browser-use.
    
    Args:
        config: Application settings
        
    Returns:
        Configured ChatGroq model for browser-use
    """
    from browser_use import ChatGroq
    
    return ChatGroq(
        model=config.groq_model,
        api_key=config.groq_api_key,
    )


async def create_browser_agent(
    task: str,
    config: Optional[Settings] = None,
    instructions: Optional[str] = None,
) -> Agent:
    """
    Factory function to create a configured browser automation Agent.
    
    Args:
        task: The task description for the agent to execute
        config: Settings instance (uses global settings if not provided)
        instructions: Additional instructions (combines with default if provided)
        
    Returns:
        Configured browser-use Agent instance ready to run
    """
    config = config or settings
    
    # Create LLM
    llm = create_llm(config)
    
    # Create browser
    browser = Browser(
        headless=config.headless_mode,
    )
    
    # Combine instructions
    full_instructions = AGENT_INSTRUCTIONS
    if instructions:
        full_instructions = f"{AGENT_INSTRUCTIONS}\n\n## Additional Context\n{instructions}"
    
    # Create and return the agent
    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
        max_actions_per_step=10,
    )
    
    return agent


