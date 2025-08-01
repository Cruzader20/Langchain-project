import asyncio
import logging
from typing import Dict, List, Any
from datetime import datetime, timedelta
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

class SprintPlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="sprint",
            name="Sprint Planner", 
            role="Agile Planning & Task Management"
        )

    async def process_message(self, message: str) -> str:
        """Process user message and provide sprint planning insights"""
        try:
            await self._simulate_processing_time()
            
            message_lower = message.lower()
            
            if any(keyword in message_lower for keyword in ['sprint', 'planning', 'scrum']):
                return await self._create_sprint_plan(message)
            elif any(keyword in message_lower for keyword in ['task', 'tasks', 'backlog']):
                return await self._manage_tasks(message)
            elif any(keyword in message_lower for keyword in ['timeline', 'schedule', 'roadmap']):
                return await self._create_timeline(message)
            elif any(keyword in message_lower for keyword in ['capacity', 'estimation', 'velocity']):
                return await self._analyze_capacity(message)
            else:
                return await self._general_planning_advice(message)
                
        except Exception as e:
            logger.error(f"Error in SprintPlannerAgent.process_message: {e}")
            return "I encountered an issue with sprint planning. Could you specify what planning aspect you need help with?"

    async def _create_sprint_plan(self, message: str) -> str:
        """Create a comprehensive sprint plan"""
        response = "I'll help you create an effective sprint plan:\n\n"
        
        response += "**🎯 Sprint Planning Framework:**\n\n"
        
        response += "**1. Sprint Setup (Duration: 2 weeks)**\n"
        response += "- Sprint Goal: Clear, measurable objective\n"
        response += "- Team Capacity: Available hours per team member\n"
        response += "- Definition of Done: Quality standards\n"
        response += "- Success Metrics: How to measure completion\n\n"
        
        response += "**2. Sprint Backlog Creation:**\n\n"
        
        response += "**Week 1 - Foundation & Core Features:**\n"
        response += "- Setup development environment (2-3 days)\n"
        response += "- Implement core user authentication (3-4 days)\n"
        response += "- Design basic UI components (2-3 days)\n"
        response += "- Setup testing framework (1-2 days)\n\n"
        
        response += "**Week 2 - Feature Development:**\n"
        response += "- Implement main feature functionality (4-5 days)\n"
        response += "- Add data validation and error handling (2 days)\n"
        response += "- Conduct testing and bug fixes (2-3 days)\n"
        response += "- Documentation and deployment prep (1 day)\n\n"
        
        response += "**3. Daily Sprint Activities:**\n\n"
        
        response += "**Daily Standups (15 minutes):**\n"
        response += "- What did you complete yesterday?\n"
        response += "- What will you work on today?\n"
        response += "- Any blockers or impediments?\n\n"
        
        response += "**Sprint Review (End of sprint):**\n"
        response += "- Demo completed features\n"
        response += "- Gather stakeholder feedback\n"
        response += "- Review sprint goals achievement\n\n"
        
        response += "**Sprint Retrospective:**\n"
        response += "- What went well?\n"
        response += "- What could be improved?\n"
        response += "- Action items for next sprint\n\n"
        
        response += "**📊 Sprint Metrics to Track:**\n"
        response += "- Velocity (story points completed)\n"
        response += "- Burndown chart progress\n"
        response += "- Bug discovery and resolution rate\n"
        response += "- Team satisfaction and morale"
        
        return response

    async def _manage_tasks(self, message: str) -> str:
        """Provide task management and backlog guidance"""
        response = "Here's how I recommend managing your product backlog and tasks:\n\n"
        
        response += "**📋 Task Prioritization Framework:**\n\n"
        
        response += "**1. MoSCoW Method:**\n"
        response += "- Must Have: Critical for MVP success\n"
        response += "- Should Have: Important but not critical\n"
        response += "- Could Have: Nice to have features\n"
        response += "- Won't Have: Out of scope for current iteration\n\n"
        
        response += "**2. Value vs Effort Matrix:**\n\n"
        
        response += "**High Value, Low Effort (Quick Wins):**\n"
        response += "- User authentication improvements\n"
        response += "- Basic analytics dashboard\n"
        response += "- Email notifications\n"
        response += "- Performance optimizations\n\n"
        
        response += "**High Value, High Effort (Major Projects):**\n"
        response += "- Core AI functionality\n"
        response += "- Advanced integrations\n"
        response += "- Mobile application\n"
        response += "- Enterprise features\n\n"
        
        response += "**Low Value, Low Effort (Fill-ins):**\n"
        response += "- UI polish and refinements\n"
        response += "- Additional export formats\n"
        response += "- Help documentation updates\n"
        response += "- Minor feature enhancements\n\n"
        
        response += "**3. Task Breakdown Structure:**\n\n"
        
        response += "**Epic → User Stories → Tasks:**\n"
        response += "- Epic: Large feature (e.g., 'User Management')\n"
        response += "- User Story: Specific user need (e.g., 'As a user, I can reset my password')\n"
        response += "- Task: Development work (e.g., 'Create password reset API endpoint')\n\n"
        
        response += "**📏 Estimation Guidelines:**\n"
        response += "- Use story points or t-shirt sizes (S, M, L, XL)\n"
        response += "- Consider complexity, uncertainty, and effort\n"
        response += "- Break down tasks larger than 3-5 days\n"
        response += "- Include testing and documentation time\n\n"
        
        response += "**🔄 Backlog Refinement:**\n"
        response += "- Review and update priorities weekly\n"
        response += "- Add acceptance criteria to user stories\n"
        response += "- Remove or archive outdated items\n"
        response += "- Ensure 2-3 sprints worth of ready stories"
        
        return response

    async def _create_timeline(self, message: str) -> str:
        """Create project timeline and milestones"""
        response = "I'll help you create a realistic project timeline:\n\n"
        
        response += "**📅 Project Timeline (6-Month Plan):**\n\n"
        
        response += "**Month 1-2: Foundation Phase**\n"
        response += "- Week 1-2: Project setup and team onboarding\n"
        response += "- Week 3-4: Core architecture and database design\n"
        response += "- Week 5-6: Basic user authentication and authorization\n"
        response += "- Week 7-8: Initial UI framework and components\n\n"
        
        response += "**Month 3-4: Core Development Phase**\n"
        response += "- Week 9-10: Main feature development (40% complete)\n"
        response += "- Week 11-12: API development and integration\n"
        response += "- Week 13-14: User interface implementation\n"
        response += "- Week 15-16: Initial testing and bug fixes\n\n"
        
        response += "**Month 5-6: Polish and Launch Phase**\n"
        response += "- Week 17-18: Feature completion and refinement\n"
        response += "- Week 19-20: Comprehensive testing and QA\n"
        response += "- Week 21-22: Performance optimization\n"
        response += "- Week 23-24: Documentation and deployment preparation\n\n"
        
        response += "**🎯 Key Milestones:**\n\n"
        
        response += "**Milestone 1 (Month 2): Technical Foundation**\n"
        response += "- Development environment ready\n"
        response += "- Database schema finalized\n"
        response += "- Basic user management working\n"
        response += "- CI/CD pipeline established\n\n"
        
        response += "**Milestone 2 (Month 4): MVP Functionality**\n"
        response += "- Core features 80% complete\n"
        response += "- API endpoints functional\n"
        response += "- User interface responsive\n"
        response += "- Basic testing coverage\n\n"
        
        response += "**Milestone 3 (Month 6): Production Ready**\n"
        response += "- All features complete and tested\n"
        response += "- Performance benchmarks met\n"
        response += "- Security audit completed\n"
        response += "- Documentation finalized\n\n"
        
        response += "**⚠️ Risk Mitigation:**\n"
        response += "- Buffer time: 20% added to estimates\n"
        response += "- Weekly progress reviews and adjustments\n"
        response += "- Alternative approaches for high-risk items\n"
        response += "- Regular stakeholder communication\n\n"
        
        response += "**📊 Progress Tracking:**\n"
        response += "- Weekly burndown charts\n"
        response += "- Feature completion percentage\n"
        response += "- Quality metrics (bugs, test coverage)\n"
        response += "- Team velocity and capacity utilization"
        
        return response

    async def _analyze_capacity(self, message: str) -> str:
        """Analyze team capacity and velocity"""
        response = "Let me help you analyze team capacity and planning:\n\n"
        
        response += "**👥 Team Capacity Analysis:**\n\n"
        
        response += "**1. Individual Capacity Calculation:**\n"
        response += "- Total work hours per week: 40 hours\n"
        response += "- Meetings and admin: -8 hours\n"
        response += "- Code reviews and support: -6 hours\n"
        response += "- Net development time: 26 hours/week\n\n"
        
        response += "**2. Team Composition & Skills:**\n\n"
        
        response += "**Frontend Developer:**\n"
        response += "- Capacity: 26 hours/week\n"
        response += "- Specialties: React, UI/UX, responsive design\n"
        response += "- Can assist: Testing, documentation\n\n"
        
        response += "**Backend Developer:**\n"
        response += "- Capacity: 26 hours/week\n"
        response += "- Specialties: API development, database, DevOps\n"
        response += "- Can assist: System architecture, security\n\n"
        
        response += "**Full-stack Developer:**\n"
        response += "- Capacity: 26 hours/week\n"
        response += "- Specialties: End-to-end features, integration\n"
        response += "- Can assist: Any area as needed\n\n"
        
        response += "**3. Sprint Velocity Estimation:**\n\n"
        
        response += "**Sprint 1-2 (Team Forming):**\n"
        response += "- Velocity: 60-70% of capacity\n"
        response += "- Focus: Setup, learning, establishing practices\n"
        response += "- Expected story points: 15-20 per sprint\n\n"
        
        response += "**Sprint 3-6 (Team Performing):**\n"
        response += "- Velocity: 80-90% of capacity\n"
        response += "- Focus: Consistent feature delivery\n"
        response += "- Expected story points: 25-30 per sprint\n\n"
        
        response += "**4. Capacity Planning Best Practices:**\n\n"
        
        response += "**Account for Non-Development Work:**\n"
        response += "- Planning meetings: 10% of time\n"
        response += "- Code reviews: 15% of time\n"
        response += "- Bug fixes and support: 10% of time\n"
        response += "- Learning and improvement: 5% of time\n\n"
        
        response += "**🔧 Optimization Strategies:**\n"
        response += "- Pair programming for complex features\n"
        response += "- Cross-training to reduce bottlenecks\n"
        response += "- Automation of repetitive tasks\n"
        response += "- Regular retrospectives for process improvement\n\n"
        
        response += "**📈 Capacity Monitoring:**\n"
        response += "- Track actual vs planned hours weekly\n"
        response += "- Monitor team happiness and energy levels\n"
        response += "- Adjust sprint commitments based on data\n"
        response += "- Plan for vacations and holidays"
        
        return response

    async def _general_planning_advice(self, message: str) -> str:
        """Provide general agile planning guidance"""
        response = "Here's my agile planning guidance for your project:\n\n"
        
        response += "**🚀 Agile Planning Principles:**\n\n"
        
        response += "**1. Start with Why:**\n"
        response += "- Define clear project vision and goals\n"
        response += "- Understand user needs and pain points\n"
        response += "- Establish success criteria and metrics\n"
        response += "- Align team on priorities and trade-offs\n\n"
        
        response += "**2. Embrace Iterative Development:**\n"
        response += "- Plan in short cycles (1-2 week sprints)\n"
        response += "- Deliver working software regularly\n"
        response += "- Gather feedback early and often\n"
        response += "- Adapt plans based on learning\n\n"
        
        response += "**3. Focus on Value Delivery:**\n"
        response += "- Prioritize features by user value\n"
        response += "- Start with minimum viable product (MVP)\n"
        response += "- Validate assumptions with real users\n"
        response += "- Measure and optimize continuously\n\n"
        
        response += "**📋 Planning Toolkit:**\n\n"
        
        response += "**User Story Mapping:**\n"
        response += "- Map user journey from end to end\n"
        response += "- Identify core user activities\n"
        response += "- Break down into smaller user stories\n"
        response += "- Prioritize by user value and effort\n\n"
        
        response += "**Sprint Planning Meetings:**\n"
        response += "- Review and refine product backlog\n"
        response += "- Select items for upcoming sprint\n"
        response += "- Break down work and estimate effort\n"
        response += "- Commit to realistic sprint goals\n\n"
        
        response += "**🔄 Continuous Improvement:**\n"
        response += "- Conduct regular retrospectives\n"
        response += "- Track team velocity and satisfaction\n"
        response += "- Experiment with new practices\n"
        response += "- Share learnings across teams\n\n"
        
        response += "What specific planning challenge can I help you solve?"
        
        return response

    async def create_sprint_plan(self, project_description: str, team_capacity: Dict[str, int]) -> Dict[str, Any]:
        """Create a detailed sprint plan"""
        try:
            await self._simulate_processing_time(2.0, 3.0)
            
            # Calculate total capacity
            total_capacity = sum(team_capacity.values())
            
            # Create sprint plan
            plan = {
                "sprint_name": "Sprint 1 - Foundation",
                "duration": 2,  # weeks
                "goals": [
                    "Establish development environment and CI/CD pipeline",
                    "Implement core user authentication system", 
                    "Create basic UI framework and components",
                    "Set up testing infrastructure"
                ],
                "tasks": [
                    {
                        "id": "S1-T1",
                        "title": "Development Environment Setup",
                        "description": "Configure development tools, databases, and deployment pipeline",
                        "assigned_to": "backend",
                        "estimated_hours": 16,
                        "priority": "high",
                        "status": "todo"
                    },
                    {
                        "id": "S1-T2", 
                        "title": "User Authentication System",
                        "description": "Implement login, registration, and password reset functionality",
                        "assigned_to": "backend",
                        "estimated_hours": 24,
                        "priority": "high",
                        "status": "todo"
                    },
                    {
                        "id": "S1-T3",
                        "title": "UI Component Library",
                        "description": "Create reusable React components and design system",
                        "assigned_to": "frontend",
                        "estimated_hours": 20,
                        "priority": "medium",
                        "status": "todo"
                    },
                    {
                        "id": "S1-T4",
                        "title": "Testing Framework Setup",
                        "description": "Configure unit, integration, and e2e testing tools",
                        "assigned_to": "fullstack",
                        "estimated_hours": 12,
                        "priority": "medium", 
                        "status": "todo"
                    }
                ],
                "capacity": team_capacity,
                "estimated_completion": "95%",
                "risks": [
                    "Third-party service integration delays",
                    "Team member availability changes",
                    "Technical complexity underestimation"
                ],
                "success_metrics": [
                    "All development tools configured and working",
                    "Users can register and login successfully",
                    "Basic UI components implemented and tested",
                    "CI/CD pipeline successfully deploys to staging"
                ]
            }
            
            return plan
            
        except Exception as e:
            logger.error(f"Error creating sprint plan: {e}")
            raise