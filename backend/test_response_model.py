#!/usr/bin/env python3
"""
Test the AgentResponse model specifically
"""
import sys
import os
from datetime import datetime
import random

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from models.schemas import AgentResponse
    print("Successfully imported AgentResponse")
except Exception as e:
    print(f"Error importing AgentResponse: {e}")
    sys.exit(1)

def test_agent_response_creation():
    """Test creating AgentResponse objects"""
    print("Testing AgentResponse creation...")
    
    try:
        # Test 1: Basic creation
        response = AgentResponse(
            id="pm_1234567890",
            content="This is a test response from the Product Manager",
            timestamp=datetime.now().isoformat(),
            sender="Product Manager",
            agentId="pm",
            avatar="👨‍💼"
        )
        print("✓ Basic AgentResponse creation successful")
        print(f"  ID: {response.id}")
        print(f"  Content: {response.content}")
        print(f"  Sender: {response.sender}")
        print(f"  AgentId: {response.agentId}")
        
        # Test 2: With confidence
        response2 = AgentResponse(
            id="tech_1234567890",
            content="This is a test response from the Tech Architect",
            timestamp=datetime.now().isoformat(),
            sender="Tech Architect",
            agentId="tech",
            avatar="👨‍💻",
            confidence=0.95
        )
        print("✓ AgentResponse with confidence creation successful")
        print(f"  Confidence: {response2.confidence}")
        
        # Test 3: With suggestions
        response3 = AgentResponse(
            id="market_1234567890",
            content="This is a test response from the Market Analyst",
            timestamp=datetime.now().isoformat(),
            sender="Market Analyst",
            agentId="market",
            avatar="📊",
            suggestions=["Suggestion 1", "Suggestion 2"]
        )
        print("✓ AgentResponse with suggestions creation successful")
        print(f"  Suggestions: {response3.suggestions}")
        
        # Test 4: Convert to dict
        response_dict = response.dict()
        print("✓ AgentResponse to dict conversion successful")
        print(f"  Dict keys: {list(response_dict.keys())}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error creating AgentResponse: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_agent_response_from_agent_manager():
    """Test the exact pattern used in agent_manager.py"""
    print("\nTesting AgentResponse creation pattern from agent_manager...")
    
    try:
        agent_id = "pm"
        content = "Test response content"
        config = {
            'name': 'Product Manager',
            'avatar': '👨‍💼'
        }
        
        response = AgentResponse(
            id=f"{agent_id}_{int(datetime.now().timestamp() * 1000)}",
            content=content,
            timestamp=datetime.now().isoformat(),
            sender=config['name'],
            agentId=agent_id,
            avatar=config['avatar'],
            confidence=random.uniform(0.8, 0.95)
        )
        
        print("✓ AgentResponse creation from agent_manager pattern successful")
        print(f"  Response: {response.dict()}")
        return True
        
    except Exception as e:
        print(f"✗ Error in agent_manager pattern: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing AgentResponse model...")
    
    success1 = test_agent_response_creation()
    success2 = test_agent_response_from_agent_manager()
    
    if success1 and success2:
        print("\n✓ All AgentResponse tests passed!")
    else:
        print("\n✗ Some AgentResponse tests failed!")
        sys.exit(1)