import asyncio
import json
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
import random

from .product_manager_agent import ProductManagerAgent
from .tech_architect_agent import TechArchitectAgent
from .market_analyst_agent import MarketAnalystAgent
from .pitch_writer_agent import PitchWriterAgent
from .sprint_planner_agent import SprintPlannerAgent
from models.schemas import Agent, AgentResponse, MarketResearch, ProjectAnalysis

logger = logging.getLogger(__name__)

class AgentManager:
    def __init__(self):
        self.agents = {
            'pm': ProductManagerAgent(),
            'tech': TechArchitectAgent(),
            'market': MarketAnalystAgent(),
            'pitch': PitchWriterAgent(),
            'sprint': SprintPlannerAgent()
        }
        
        self.agent_configs = {
            'pm': {
                'id': 'pm',
                'name': 'Product Manager',
                'role': 'PM Agent',
                'active': True,
                'avatar': '👨‍💼',
                'description': 'Breaks down feature ideas into specs and milestones, manages product roadmap',
                'capabilities': [
                    'Feature specification',
                    'Roadmap planning',
                    'User story creation',
                    'Requirements analysis'
                ],
                'expertise': 'Product Strategy, User Experience, Agile Methodology'
            },
            'tech': {
                'id': 'tech',
                'name': 'Tech Architect',
                'role': 'Technical Architect',
                'active': True,
                'avatar': '👨‍💻',
                'description': 'Suggests tech stack, builds initial design, and provides technical guidance',
                'capabilities': [
                    'Architecture design',
                    'Technology recommendations',
                    'Technical feasibility analysis',
                    'Code structure planning'
                ],
                'expertise': 'Full-stack Development, Cloud Architecture, DevOps'
            },
            'market': {
                'id': 'market',
                'name': 'Market Analyst',
                'role': 'Market Analyst',
                'active': True,
                'avatar': '📊',
                'description': 'Scrapes and summarizes competitor strategies, analyzes market opportunities',
                'capabilities': [
                    'Competitive analysis',
                    'Market research',
                    'Trend identification',
                    'Pricing strategy'
                ],
                'expertise': 'Market Research, Business Intelligence, Data Analysis'
            },
            'pitch': {
                'id': 'pitch',
                'name': 'Pitch Writer',
                'role': 'Pitch Writer',
                'active': True,
                'avatar': '✍️',
                'description': 'Drafts presentations, decks, and compelling content for stakeholders',
                'capabilities': [
                    'Presentation creation',
                    'Content writing',
                    'Storytelling',
                    'Stakeholder communication'
                ],
                'expertise': 'Business Writing, Presentation Design, Communications'
            },
            'sprint': {
                'id': 'sprint',
                'name': 'Sprint Planner',
                'role': 'Sprint Planner',
                'active': True,
                'avatar': '📋',
                'description': 'Allocates tasks over weekly sprints and manages project timelines',
                'capabilities': [
                    'Sprint planning',
                    'Task allocation',
                    'Timeline management',
                    'Progress tracking'
                ],
                'expertise': 'Agile Planning, Project Management, Resource Allocation'
            }
        }

    async def get_all_agents(self) -> List[Agent]:
        """Get all agents with their current configuration"""
        return [Agent(**config) for config in self.agent_configs.values()]

    async def toggle_agent(self, agent_id: str) -> Agent:
        """Toggle agent active status"""
        if agent_id not in self.agent_configs:
            raise ValueError(f"Agent {agent_id} not found")
        
        self.agent_configs[agent_id]['active'] = not self.agent_configs[agent_id]['active']
        logger.info(f"Agent {agent_id} active status: {self.agent_configs[agent_id]['active']}")
        
        return Agent(**self.agent_configs[agent_id])

    async def process_user_message(self, message: str, active_agent_ids: List[str]) -> List[AgentResponse]:
        """Process user message and generate responses from active agents"""
        responses = []
        
        # Filter to only active agents
        participating_agents = [
            agent_id for agent_id in active_agent_ids 
            if agent_id in self.agent_configs and self.agent_configs[agent_id]['active']
        ]
        
        logger.info(f"Processing message with {len(participating_agents)} agents: {participating_agents}")
        
        # Generate responses from each participating agent
        tasks = []
        for agent_id in participating_agents:
            if agent_id in self.agents:
                task = self._generate_agent_response(agent_id, message)
                tasks.append(task)
        
        # Execute all agent responses concurrently
        if tasks:
            agent_responses = await asyncio.gather(*tasks, return_exceptions=True)
            
            for i, response in enumerate(agent_responses):
                if isinstance(response, Exception):
                    logger.error(f"Error from agent {participating_agents[i]}: {response}")
                elif response:
                    responses.append(response)
        
        return responses

    async def _generate_agent_response(self, agent_id: str, message: str) -> Optional[AgentResponse]:
        """Generate a response from a specific agent"""
        try:
            agent = self.agents[agent_id]
            config = self.agent_configs[agent_id]
            
            # Generate response using the agent
            content = await agent.process_message(message)
            
            # Create response object
            response = AgentResponse(
                id=f"{agent_id}_{int(datetime.now().timestamp() * 1000)}",
                content=content,
                timestamp=datetime.now().isoformat(),
                sender=config['name'],
                agentId=agent_id,
                avatar=config['avatar'],
                confidence=random.uniform(0.8, 0.95)  # Simulate confidence score
            )
            
            return response
            
        except Exception as e:
            logger.error(f"Error generating response from agent {agent_id}: {e}")
            return None

    async def get_market_research(self, query: str) -> MarketResearch:
        """Get market research data"""
        try:
            market_agent = self.agents['market']
            research_data = await market_agent.conduct_research(query)
            return research_data
        except Exception as e:
            logger.error(f"Error getting market research: {e}")
            raise

    async def analyze_project(self, description: str) -> ProjectAnalysis:
        """Analyze a project using multiple agents"""
        try:
            # Get analysis from PM agent
            pm_agent = self.agents['pm']
            analysis = await pm_agent.analyze_project(description)
            return analysis
        except Exception as e:
            logger.error(f"Error analyzing project: {e}")
            raise

    async def create_sprint_plan(self, project_description: str, team_capacity: Dict[str, int]) -> Dict[str, Any]:
        """Create a sprint plan using the sprint planner agent"""
        try:
            sprint_agent = self.agents['sprint']
            plan = await sprint_agent.create_sprint_plan(project_description, team_capacity)
            return plan
        except Exception as e:
            logger.error(f"Error creating sprint plan: {e}")
            raise

    async def generate_pitch_deck(self, project_description: str, target_audience: str) -> Dict[str, Any]:
        """Generate a pitch deck using the pitch writer agent"""
        try:
            pitch_agent = self.agents['pitch']
            deck = await pitch_agent.create_pitch_deck(project_description, target_audience)
            return deck
        except Exception as e:
            logger.error(f"Error generating pitch deck: {e}")
            raise

    async def get_tech_recommendations(self, requirements: str) -> Dict[str, Any]:
        """Get technical recommendations from the tech architect"""
        try:
            tech_agent = self.agents['tech']
            recommendations = await tech_agent.get_tech_recommendations(requirements)
            return recommendations
        except Exception as e:
            logger.error(f"Error getting tech recommendations: {e}")
            raise