from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import asyncio
import logging
from datetime import datetime
from typing import List, Dict, Any
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Team Strategy Agent API",
    description="AI-powered team strategy and planning platform",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple agent data
agents_data = [
    {"id": "pm", "name": "Product Manager", "role": "PM Agent", "active": True, "avatar": "👨‍💼"},
    {"id": "tech", "name": "Tech Architect", "role": "Technical Architect", "active": True, "avatar": "👨‍💻"},
    {"id": "market", "name": "Market Analyst", "role": "Market Analyst", "active": True, "avatar": "📊"},
    {"id": "pitch", "name": "Pitch Writer", "role": "Pitch Writer", "active": True, "avatar": "✍️"},
    {"id": "sprint", "name": "Sprint Planner", "role": "Sprint Planner", "active": True, "avatar": "📋"}
]

# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"Client connected. Total connections: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        logger.info(f"Client disconnected. Total connections: {len(self.active_connections)}")

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

manager = ConnectionManager()

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Team Strategy Agent API is running", "status": "healthy"}

@app.get("/api/agents")
async def get_agents():
    """Get all available agents"""
    return {"agents": agents_data}

@app.post("/api/agents/{agent_id}/toggle")
async def toggle_agent(agent_id: str):
    """Toggle agent active status"""
    for agent in agents_data:
        if agent["id"] == agent_id:
            agent["active"] = not agent["active"]
            return {"success": True, "agent": agent}
    raise HTTPException(status_code=404, detail="Agent not found")

# Simple message models
class UserMessage(BaseModel):
    content: str
    agents: List[str] = []

def generate_agent_response(agent_id: str, message: str) -> dict:
    """Generate a simple response from an agent"""
    agent = next((a for a in agents_data if a["id"] == agent_id), None)
    if not agent:
        return None
        
    responses = {
        "pm": f"As a Product Manager, I'll help break down '{message}' into actionable components. Let me analyze the requirements and create a structured plan with clear milestones and user stories.",
        "tech": f"From a technical perspective, I recommend we start with a solid architecture for '{message}'. I'll outline the tech stack, design patterns, and scalability considerations.",
        "market": f"I'll research the competitive landscape for '{message}'. Let me analyze market opportunities, competitor strategies, and identify potential differentiators.",
        "pitch": f"I can help create compelling content for '{message}'. Let me draft a narrative that resonates with your target audience and highlights key value propositions.",
        "sprint": f"For '{message}', I'll create a sprint plan with clear timelines, task allocation, and resource management to ensure efficient delivery."
    }
    
    return {
        "id": f"{agent_id}_{int(datetime.now().timestamp() * 1000)}",
        "type": "agent",
        "content": responses.get(agent_id, f"I'm {agent['name']} and I'll help with your request."),
        "timestamp": datetime.now().isoformat(),
        "sender": agent["name"],
        "agentId": agent_id,
        "avatar": agent["avatar"]
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time communication"""
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            logger.info(f"Received message: {message_data}")
            
            if message_data.get("type") == "user_message":
                user_message = message_data.get("message", "")
                active_agents = message_data.get("agents", [])
                
                # Generate agent responses
                for agent_id in active_agents:
                    if any(a["id"] == agent_id and a["active"] for a in agents_data):
                        await asyncio.sleep(1.5)  # Simulate thinking time
                        response = generate_agent_response(agent_id, user_message)
                        if response:
                            await manager.send_personal_message(
                                json.dumps(response),
                                websocket
                            )
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
        manager.disconnect(websocket)

@app.post("/api/chat/message")
async def send_message(message: UserMessage):
    """Send a message to agents (HTTP endpoint alternative to WebSocket)"""
    responses = []
    for agent_id in message.agents:
        if any(a["id"] == agent_id and a["active"] for a in agents_data):
            response = generate_agent_response(agent_id, message.content)
            if response:
                responses.append(response)
    return {"responses": responses}

if __name__ == "__main__":
    uvicorn.run(
        "simple_main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )