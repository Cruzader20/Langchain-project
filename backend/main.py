from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
import asyncio
import logging
from datetime import datetime
from typing import List, Dict, Any
import uvicorn

from agents.agent_manager import AgentManager
from models.schemas import UserMessage, AgentResponse, Task, Agent
from database.db import init_db

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

# Initialize agent manager
agent_manager = AgentManager()

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

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception as e:
                logger.error(f"Error broadcasting message: {e}")

manager = ConnectionManager()

@app.on_event("startup")
async def startup_event():
    """Initialize database and services on startup"""
    await init_db()
    logger.info("Application started successfully")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Team Strategy Agent API is running", "status": "healthy"}

@app.get("/api/agents")
async def get_agents():
    """Get all available agents"""
    try:
        agents = await agent_manager.get_all_agents()
        return {"agents": agents}
    except Exception as e:
        logger.error(f"Error getting agents: {e}")
        raise HTTPException(status_code=500, detail="Failed to get agents")

@app.post("/api/agents/{agent_id}/toggle")
async def toggle_agent(agent_id: str):
    """Toggle agent active status"""
    try:
        result = await agent_manager.toggle_agent(agent_id)
        return {"success": True, "agent": result}
    except Exception as e:
        logger.error(f"Error toggling agent {agent_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to toggle agent")

@app.get("/api/tasks")
async def get_tasks():
    """Get all tasks"""
    try:
        # This would typically come from a database
        # For now, return sample data
        sample_tasks = [
            {
                "id": "1",
                "title": "Market Research for AI Finance Tool",
                "description": "Research competitors and market opportunities in AI finance space",
                "status": "todo",
                "priority": "high",
                "assignedTo": "market",
                "assignedAgent": "Market Analyst",
                "createdBy": "PM Agent",
                "dueDate": "2024-01-20",
                "sprint": "current",
                "tags": ["research", "finance", "ai"]
            }
        ]
        return {"tasks": sample_tasks}
    except Exception as e:
        logger.error(f"Error getting tasks: {e}")
        raise HTTPException(status_code=500, detail="Failed to get tasks")

@app.post("/api/tasks")
async def create_task(task: Task):
    """Create a new task"""
    try:
        # In a real implementation, this would save to database
        task_dict = task.dict()
        task_dict["id"] = str(datetime.now().timestamp())
        task_dict["createdAt"] = datetime.now().isoformat()
        
        logger.info(f"Created new task: {task_dict['title']}")
        return {"success": True, "task": task_dict}
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        raise HTTPException(status_code=500, detail="Failed to create task")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time communication"""
    await manager.connect(websocket)
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            logger.info(f"Received message: {message_data}")
            
            if message_data.get("type") == "user_message":
                # Process user message and generate agent responses
                user_message = message_data.get("message", "")
                active_agents = message_data.get("agents", [])
                
                # Send user message confirmation
                await manager.send_personal_message(
                    json.dumps({
                        "type": "message_received",
                        "message": "Message received, agents are processing..."
                    }),
                    websocket
                )
                
                # Generate agent responses
                agent_responses = await agent_manager.process_user_message(
                    user_message, 
                    active_agents
                )
                
                # Send each agent response with delay for realistic effect
                for i, response in enumerate(agent_responses):
                    await asyncio.sleep(1.5)  # Simulate thinking time
                    
                    # Convert AgentResponse to dict for JSON serialization
                    if hasattr(response, 'dict'):
                        response_dict = response.dict()
                    else:
                        response_dict = response
                    
                    await manager.send_personal_message(
                        json.dumps({
                            "type": "agent_response",
                            **response_dict
                        }),
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
    try:
        responses = await agent_manager.process_user_message(
            message.content, 
            message.agents
        )
        return {"responses": responses}
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        raise HTTPException(status_code=500, detail="Failed to process message")

@app.get("/api/market/research")
async def get_market_research(query: str):
    """Get market research data"""
    try:
        # This would integrate with market analysis tools
        research_data = await agent_manager.get_market_research(query)
        return {"research": research_data}
    except Exception as e:
        logger.error(f"Error getting market research: {e}")
        raise HTTPException(status_code=500, detail="Failed to get market research")

@app.post("/api/projects/analyze")
async def analyze_project(project_description: str):
    """Analyze a project and generate recommendations"""
    try:
        analysis = await agent_manager.analyze_project(project_description)
        return {"analysis": analysis}
    except Exception as e:
        logger.error(f"Error analyzing project: {e}")
        raise HTTPException(status_code=500, detail="Failed to analyze project")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )