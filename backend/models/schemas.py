from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "inprogress"
    REVIEW = "review"
    DONE = "done"

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class AgentRole(str, Enum):
    PM = "pm"
    TECH = "tech"
    MARKET = "market"
    PITCH = "pitch"
    SPRINT = "sprint"

class Agent(BaseModel):
    id: str
    name: str
    role: str
    active: bool = True
    avatar: str
    description: Optional[str] = None
    capabilities: List[str] = Field(default_factory=list)
    expertise: Optional[str] = None

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    priority: TaskPriority = TaskPriority.MEDIUM
    assignedTo: str
    dueDate: Optional[str] = None
    sprint: str = "current"
    tags: List[str] = Field(default_factory=list)
    
    class Config:
        use_enum_values = True

class TaskResponse(Task):
    id: str
    status: TaskStatus = TaskStatus.TODO
    assignedAgent: Optional[str] = None
    createdBy: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class UserMessage(BaseModel):
    content: str
    agents: List[str] = Field(default_factory=list)
    timestamp: Optional[datetime] = None

class AgentResponse(BaseModel):
    id: str
    type: str = "agent"
    content: str
    timestamp: str
    sender: str
    agentId: str
    avatar: str
    confidence: Optional[float] = None
    suggestions: List[str] = Field(default_factory=list)

class ProjectAnalysis(BaseModel):
    summary: str
    recommendations: List[str]
    tech_stack: List[str]
    timeline: Dict[str, Any]
    risks: List[str]
    opportunities: List[str]

class MarketResearch(BaseModel):
    query: str
    competitors: List[Dict[str, Any]]
    market_size: Optional[str] = None
    trends: List[str]
    pricing_insights: List[Dict[str, Any]]
    opportunities: List[str]

class SprintPlan(BaseModel):
    sprint_name: str
    duration: int  # in weeks
    goals: List[str]
    tasks: List[TaskResponse]
    capacity: Dict[str, int]  # agent_id -> hours
    estimated_completion: str

class PitchDeck(BaseModel):
    title: str
    slides: List[Dict[str, Any]]
    key_points: List[str]
    target_audience: str
    call_to_action: str

class ChatSession(BaseModel):
    session_id: str
    user_id: Optional[str] = None
    messages: List[Dict[str, Any]] = Field(default_factory=list)
    active_agents: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class WebSocketMessage(BaseModel):
    type: str
    payload: Dict[str, Any]
    timestamp: datetime = Field(default_factory=datetime.now)