#!/usr/bin/env python3
"""
Simple test to isolate the issue
"""
import asyncio
import json
from datetime import datetime
import random

# Mock the AgentResponse class
class MockAgentResponse:
    def __init__(self, agent_id, content, sender, avatar):
        self.id = f"{agent_id}_{int(datetime.now().timestamp() * 1000)}"
        self.content = content
        self.timestamp = datetime.now().isoformat()
        self.sender = sender
        self.agentId = agent_id
        self.avatar = avatar
        self.confidence = random.uniform(0.8, 0.95)

# Mock agent responses
def generate_mock_response(agent_id: str, message: str) -> MockAgentResponse:
    """Generate a mock response from an agent"""
    responses = {
        "pm": f"As a Product Manager, I'll help break down '{message}' into actionable components. Let me analyze the requirements and create a structured plan with clear milestones and user stories.",
        "tech": f"From a technical perspective, I recommend we start with a solid architecture for '{message}'. I'll outline the tech stack, design patterns, and scalability considerations.",
        "market": f"I'll research the competitive landscape for '{message}'. Let me analyze market opportunities, competitor strategies, and identify potential differentiators.",
        "pitch": f"I can help create compelling content for '{message}'. Let me draft a narrative that resonates with your target audience and highlights key value propositions.",
        "sprint": f"For '{message}', I'll create a sprint plan with clear timelines, task allocation, and resource management to ensure efficient delivery."
    }
    
    agent_names = {
        "pm": "Product Manager",
        "tech": "Tech Architect", 
        "market": "Market Analyst",
        "pitch": "Pitch Writer",
        "sprint": "Sprint Planner"
    }
    
    agent_avatars = {
        "pm": "👨‍💼",
        "tech": "👨‍💻",
        "market": "📊",
        "pitch": "✍️",
        "sprint": "📋"
    }
    
    content = responses.get(agent_id, f"I'm {agent_names[agent_id]} and I'll help with your request.")
    
    return MockAgentResponse(
        agent_id=agent_id,
        content=content,
        sender=agent_names[agent_id],
        avatar=agent_avatars[agent_id]
    )

async def mock_process_user_message(message: str, active_agent_ids: list) -> list:
    """Mock the process_user_message function"""
    print(f"Processing message: '{message}' with agents: {active_agent_ids}")
    
    responses = []
    
    # Generate responses from each agent
    tasks = []
    for agent_id in active_agent_ids:
        print(f"Creating task for agent: {agent_id}")
        # Simulate async processing
        task = asyncio.create_task(mock_agent_response(agent_id, message))
        tasks.append(task)
    
    print(f"Created {len(tasks)} tasks")
    
    # Execute all agent responses concurrently
    if tasks:
        print("Starting asyncio.gather")
        agent_responses = await asyncio.gather(*tasks, return_exceptions=True)
        print(f"Received {len(agent_responses)} responses from asyncio.gather")
        
        for i, response in enumerate(agent_responses):
            if isinstance(response, Exception):
                print(f"Error from agent {active_agent_ids[i]}: {response}")
            elif response:
                print(f"Adding response from agent {active_agent_ids[i]}")
                responses.append(response)
            else:
                print(f"Empty response from agent {active_agent_ids[i]}")
    
    print(f"Returning {len(responses)} total responses")
    return responses

async def mock_agent_response(agent_id: str, message: str):
    """Mock individual agent response"""
    print(f"Starting mock_agent_response for agent {agent_id}")
    try:
        # Simulate some processing time
        await asyncio.sleep(0.1)
        
        response = generate_mock_response(agent_id, message)
        print(f"Created response for agent {agent_id}")
        return response
        
    except Exception as e:
        print(f"Error in mock_agent_response for agent {agent_id}: {e}")
        return None

async def test_mock_agents():
    """Test the mock agent functionality"""
    print("Testing mock agent functionality...")
    
    test_message = "hi"
    test_agents = ['pm', 'tech', 'market', 'pitch', 'sprint']
    
    try:
        responses = await mock_process_user_message(test_message, test_agents)
        print(f"\nReceived {len(responses)} responses:")
        
        for i, response in enumerate(responses):
            print(f"\nResponse {i+1}:")
            print(f"  Agent: {response.agentId}")
            print(f"  Sender: {response.sender}")
            print(f"  Content: {response.content[:100]}...")
            print(f"  Timestamp: {response.timestamp}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_mock_agents())