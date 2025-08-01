#!/usr/bin/env python3
"""
Test to verify the AgentResponse fix
"""
import sys
import os
from datetime import datetime
import random
import json

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.schemas import AgentResponse

def test_agent_response_access():
    """Test accessing AgentResponse attributes and converting to dict"""
    print("Testing AgentResponse access and conversion...")
    
    try:
        # Create an AgentResponse object
        response = AgentResponse(
            id="pm_1234567890",
            content="This is a test response from the Product Manager",
            timestamp=datetime.now().isoformat(),
            sender="Product Manager",
            agentId="pm",
            avatar="👨‍💼",
            confidence=0.95
        )
        
        # Test direct attribute access
        print(f"✓ Direct attribute access:")
        print(f"  agentId: {response.agentId}")
        print(f"  sender: {response.sender}")
        print(f"  content: {response.content[:50]}...")
        
        # Test model_dump() method
        response_dict = response.model_dump()
        print(f"✓ model_dump() successful:")
        print(f"  Dict keys: {list(response_dict.keys())}")
        print(f"  agentId from dict: {response_dict['agentId']}")
        
        # Test JSON serialization
        json_str = json.dumps({
            "type": "agent_response",
            **response_dict
        })
        print(f"✓ JSON serialization successful:")
        print(f"  JSON length: {len(json_str)}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_websocket_message_format():
    """Test the exact format used in the WebSocket endpoint"""
    print("\nTesting WebSocket message format...")
    
    try:
        # Create an AgentResponse object
        response = AgentResponse(
            id="pm_1234567890",
            content="This is a test response from the Product Manager",
            timestamp=datetime.now().isoformat(),
            sender="Product Manager",
            agentId="pm",
            avatar="👨‍💼",
            confidence=0.95
        )
        
        # Simulate the WebSocket message format
        message = {
            "type": "agent_response",
            **response.model_dump()
        }
        
        # Convert to JSON (like in the WebSocket)
        json_message = json.dumps(message)
        
        print(f"✓ WebSocket message format successful:")
        print(f"  Message type: {message['type']}")
        print(f"  Agent ID: {message['agentId']}")
        print(f"  Sender: {message['sender']}")
        print(f"  JSON length: {len(json_message)}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing AgentResponse fix...")
    
    success1 = test_agent_response_access()
    success2 = test_websocket_message_format()
    
    if success1 and success2:
        print("\n✓ All tests passed! The fix should work correctly.")
    else:
        print("\n✗ Some tests failed!")
        sys.exit(1)