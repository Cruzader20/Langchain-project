import asyncio
import json
import logging
from typing import Dict, List, Any
from datetime import datetime, timedelta
import re

from .base_agent import BaseAgent
from models.schemas import ProjectAnalysis

logger = logging.getLogger(__name__)

class ProductManagerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="pm",
            name="Product Manager",
            role="Product Strategy & Requirements"
        )
        
        self.expertise = [
            "Feature specification",
            "User story creation", 
            "Product roadmapping",
            "Requirements analysis",
            "Stakeholder management",
            "MVP definition",
            "User experience planning"
        ]

    async def process_message(self, message: str) -> str:
        """Process user message and provide product management insights"""
        try:
            # Analyze the message for product-related keywords
            message_lower = message.lower()
            
            # Determine response type based on message content
            if any(keyword in message_lower for keyword in ['idea', 'product', 'feature', 'build', 'create', 'develop']):
                return await self._analyze_product_idea(message)
            elif any(keyword in message_lower for keyword in ['requirements', 'specs', 'specification']):
                return await self._create_requirements(message)
            elif any(keyword in message_lower for keyword in ['roadmap', 'timeline', 'planning']):
                return await self._create_roadmap(message)
            elif any(keyword in message_lower for keyword in ['user', 'customer', 'personas']):
                return await self._analyze_users(message)
            else:
                return await self._general_product_advice(message)
                
        except Exception as e:
            logger.error(f"Error in ProductManagerAgent.process_message: {e}")
            return "I encountered an issue analyzing your request. Could you please rephrase your product requirements?"

    async def _analyze_product_idea(self, idea: str) -> str:
        """Analyze a product idea and break it down"""
        # Extract key components from the idea
        components = await self._extract_product_components(idea)
        
        response = f"Excellent! I'll help break down '{idea}' into actionable components:\n\n"
        
        response += "**🎯 Core Product Vision:**\n"
        response += f"- Primary purpose: {components.get('purpose', 'Solve user problems efficiently')}\n"
        response += f"- Target audience: {components.get('audience', 'Early adopters and tech-savvy users')}\n\n"
        
        response += "**📋 Key Features (MVP):**\n"
        for i, feature in enumerate(components.get('features', []), 1):
            response += f"{i}. {feature}\n"
        
        response += "\n**🔄 Recommended Development Phases:**\n"
        response += "Phase 1: Core functionality + user authentication\n"
        response += "Phase 2: Advanced features + integrations\n"
        response += "Phase 3: Analytics + optimization\n\n"
        
        response += "**💡 Next Steps:**\n"
        response += "1. Define detailed user stories\n"
        response += "2. Create wireframes and user flows\n"
        response += "3. Validate assumptions with target users\n"
        response += "4. Prioritize features by impact vs effort"
        
        return response

    async def _create_requirements(self, request: str) -> str:
        """Create detailed requirements based on request"""
        response = "I'll help create comprehensive requirements:\n\n"
        
        response += "**📝 Functional Requirements:**\n"
        response += "- User registration and authentication\n"
        response += "- Core feature implementation\n"
        response += "- Data storage and retrieval\n"
        response += "- User interface interactions\n\n"
        
        response += "**⚙️ Non-Functional Requirements:**\n"
        response += "- Performance: <2s page load times\n"
        response += "- Scalability: Support 10K+ concurrent users\n"
        response += "- Security: Industry-standard encryption\n"
        response += "- Availability: 99.9% uptime\n\n"
        
        response += "**🧪 Acceptance Criteria:**\n"
        response += "- Given: User has valid account\n"
        response += "- When: User performs core actions\n"
        response += "- Then: System responds appropriately\n\n"
        
        response += "Would you like me to elaborate on any specific requirement area?"
        
        return response

    async def _create_roadmap(self, request: str) -> str:
        """Create a product roadmap"""
        response = "Here's a strategic product roadmap:\n\n"
        
        response += "**📅 Quarter 1 (Weeks 1-12):**\n"
        response += "- MVP development and testing\n"
        response += "- User feedback collection\n"
        response += "- Core feature refinement\n\n"
        
        response += "**📅 Quarter 2 (Weeks 13-24):**\n"
        response += "- Advanced feature development\n"
        response += "- Integration with third-party services\n"
        response += "- Performance optimization\n\n"
        
        response += "**📅 Quarter 3 (Weeks 25-36):**\n"
        response += "- Analytics and reporting features\n"
        response += "- Mobile application development\n"
        response += "- User experience enhancements\n\n"
        
        response += "**🎯 Success Metrics:**\n"
        response += "- User adoption rate > 80%\n"
        response += "- Feature completion rate > 95%\n"
        response += "- User satisfaction score > 4.5/5\n"
        
        return response

    async def _analyze_users(self, request: str) -> str:
        """Analyze user needs and create personas"""
        response = "Let me help define your target users:\n\n"
        
        response += "**👤 Primary Persona: 'The Innovator'**\n"
        response += "- Age: 25-40\n"
        response += "- Role: Startup founder, Product manager\n"
        response += "- Goals: Scale business, improve efficiency\n"
        response += "- Pain points: Time management, resource allocation\n\n"
        
        response += "**👤 Secondary Persona: 'The Optimizer'**\n"
        response += "- Age: 30-45\n"
        response += "- Role: Team lead, Operations manager\n"
        response += "- Goals: Streamline processes, increase productivity\n"
        response += "- Pain points: Manual workflows, data silos\n\n"
        
        response += "**📊 User Journey Mapping:**\n"
        response += "1. Discovery: User identifies problem\n"
        response += "2. Evaluation: User researches solutions\n"
        response += "3. Trial: User tests our product\n"
        response += "4. Adoption: User integrates into workflow\n"
        response += "5. Advocacy: User recommends to others\n\n"
        
        response += "Should I create detailed user stories for these personas?"
        
        return response

    async def _general_product_advice(self, message: str) -> str:
        """Provide general product management advice"""
        advice_options = [
            "From a product perspective, I recommend focusing on user validation first. Understanding your target audience's real pain points will guide all subsequent decisions.",
            
            "As your PM, I suggest we start with a clear problem statement. What specific user problem are we solving, and how do we know it's worth solving?",
            
            "Let's think about this strategically. I recommend we define success metrics early - what does 'winning' look like for this initiative?",
            
            "I'd approach this by breaking it into smaller, testable hypotheses. This allows us to learn and iterate quickly with minimal risk.",
            
            "From a product standpoint, we should consider the competitive landscape and identify our unique value proposition. How will we differentiate?"
        ]
        
        import random
        base_response = random.choice(advice_options)
        
        response = f"{base_response}\n\n"
        response += "**📋 Product Management Framework I recommend:**\n"
        response += "1. Define the problem clearly\n"
        response += "2. Identify target users and use cases\n"
        response += "3. Design minimum viable solution\n"
        response += "4. Test with real users\n"
        response += "5. Iterate based on feedback\n\n"
        response += "What specific aspect would you like me to focus on?"
        
        return response

    async def _extract_product_components(self, idea: str) -> Dict[str, Any]:
        """Extract key product components from an idea description"""
        components = {
            'purpose': 'Solve user problems efficiently',
            'audience': 'Early adopters and tech-savvy users',
            'features': []
        }
        
        # Simple keyword-based feature extraction
        idea_lower = idea.lower()
        
        if 'ai' in idea_lower or 'artificial intelligence' in idea_lower:
            components['features'].extend([
                'AI-powered core functionality',
                'Machine learning algorithms',
                'Intelligent recommendations'
            ])
        
        if 'finance' in idea_lower or 'financial' in idea_lower:
            components['features'].extend([
                'Financial data integration',
                'Transaction tracking',
                'Budget management',
                'Reporting and analytics'
            ])
            components['audience'] = 'Finance professionals and business owners'
        
        if 'voice' in idea_lower or 'speech' in idea_lower:
            components['features'].extend([
                'Voice recognition',
                'Speech-to-text conversion',
                'Audio processing',
                'Voice commands'
            ])
        
        if 'tutor' in idea_lower or 'education' in idea_lower:
            components['features'].extend([
                'Personalized learning paths',
                'Progress tracking',
                'Interactive lessons',
                'Performance analytics'
            ])
            components['audience'] = 'Students, parents, and educators'
        
        # Default features if none detected
        if not components['features']:
            components['features'] = [
                'User registration and profiles',
                'Core functionality',
                'Data management',
                'User dashboard',
                'Settings and preferences'
            ]
        
        return components

    async def analyze_project(self, description: str) -> ProjectAnalysis:
        """Provide comprehensive project analysis"""
        try:
            components = await self._extract_product_components(description)
            
            analysis = ProjectAnalysis(
                summary=f"Strategic analysis of: {description}",
                recommendations=[
                    "Start with MVP focused on core user problem",
                    "Validate assumptions through user interviews",
                    "Create detailed user personas and journey maps",
                    "Define clear success metrics and KPIs",
                    "Plan iterative development approach"
                ],
                tech_stack=[
                    "Frontend: React.js or Next.js",
                    "Backend: Node.js or Python",
                    "Database: PostgreSQL or MongoDB",
                    "Hosting: AWS or Vercel"
                ],
                timeline={
                    "MVP": "8-12 weeks",
                    "Beta Release": "16-20 weeks", 
                    "Public Launch": "24-28 weeks"
                },
                risks=[
                    "User adoption challenges",
                    "Competition from established players",
                    "Technical complexity underestimation",
                    "Resource allocation issues"
                ],
                opportunities=[
                    "First-mover advantage in niche",
                    "High user demand for solution",
                    "Potential for rapid scaling",
                    "Multiple monetization options"
                ]
            )
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error in analyze_project: {e}")
            raise