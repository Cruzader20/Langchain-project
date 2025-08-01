#!/usr/bin/env python3
"""
Simple test script to verify agent functionality
"""
import asyncio
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agents.agent_manager import AgentManager

async def test_agents():
    """Test that agents can process messages"""
    print("Initializing AgentManager...")
    agent_manager = AgentManager()
    
    print(f"Available agents: {list(agent_manager.agents.keys())}")
    
    # Test message
    test_message = "hi"
    test_agents = ['pm', 'tech', 'market', 'pitch', 'sprint']
    
    print(f"\nTesting with message: '{test_message}'")
    print(f"Active agents: {test_agents}")
    
    try:
        responses = await agent_manager.process_user_message(test_message, test_agents)
        print(f"\nReceived {len(responses)} responses:")
        
        for i, response in enumerate(responses):
            print(f"\nResponse {i+1}:")
            print(f"  Agent: {response.agentId}")
            print(f"  Sender: {response.sender}")
            print(f"  Content: {response.content[:200]}...")
            print(f"  Timestamp: {response.timestamp}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_agents())