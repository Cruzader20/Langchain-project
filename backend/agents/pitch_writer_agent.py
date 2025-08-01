import asyncio
import logging
from typing import Dict, List, Any
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

class PitchWriterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="pitch",
            name="Pitch Writer",
            role="Content & Presentation Creation"
        )

    async def process_message(self, message: str) -> str:
        """Process user message and provide content creation insights"""
        try:
            await self._simulate_processing_time()
            
            message_lower = message.lower()
            
            if any(keyword in message_lower for keyword in ['pitch', 'presentation', 'deck']):
                return await self._create_pitch_outline(message)
            elif any(keyword in message_lower for keyword in ['content', 'copy', 'writing']):
                return await self._provide_content_strategy(message)
            elif any(keyword in message_lower for keyword in ['story', 'narrative', 'messaging']):
                return await self._develop_narrative(message)
            else:
                return await self._general_content_advice(message)
                
        except Exception as e:
            logger.error(f"Error in PitchWriterAgent.process_message: {e}")
            return "I encountered an issue with content creation. Could you specify what type of content you need?"

    async def _create_pitch_outline(self, message: str) -> str:
        """Create a compelling pitch deck outline"""
        response = "I'll help you create a compelling pitch deck structure:\n\n"
        
        response += "**🎯 Essential Pitch Deck Slides:**\n\n"
        
        response += "**1. Problem & Solution (Slides 1-3)**\n"
        response += "- Hook: Start with a relatable problem\n"
        response += "- Problem: Define the pain point clearly\n"
        response += "- Solution: Present your unique approach\n\n"
        
        response += "**2. Market Opportunity (Slides 4-5)**\n"
        response += "- Market size and growth potential\n"
        response += "- Target customer segments\n"
        response += "- Why now? Market timing factors\n\n"
        
        response += "**3. Product Demo (Slide 6)**\n"
        response += "- Live demo or compelling screenshots\n"
        response += "- Key features and benefits\n"
        response += "- User experience highlights\n\n"
        
        response += "**4. Business Model & Traction (Slides 7-8)**\n"
        response += "- Revenue model and pricing\n"
        response += "- Early traction and metrics\n"
        response += "- Customer testimonials\n\n"
        
        response += "**5. Competition & Go-to-Market (Slides 9-10)**\n"
        response += "- Competitive landscape analysis\n"
        response += "- Unique differentiation\n"
        response += "- Marketing and sales strategy\n\n"
        
        response += "**6. Team & Financials (Slides 11-12)**\n"
        response += "- Founding team credentials\n"
        response += "- Financial projections\n"
        response += "- Funding requirements and use of funds\n\n"
        
        response += "**💡 Key Storytelling Tips:**\n"
        response += "- Keep each slide focused on one key message\n"
        response += "- Use visuals over text whenever possible\n"
        response += "- Practice the narrative flow between slides\n"
        response += "- End with a clear call to action"
        
        return response

    async def _provide_content_strategy(self, message: str) -> str:
        """Provide content marketing and messaging strategy"""
        response = "Here's a comprehensive content strategy framework:\n\n"
        
        response += "**📝 Content Pillars:**\n\n"
        
        response += "**1. Educational Content (40%)**\n"
        response += "- How-to guides and tutorials\n"
        response += "- Industry insights and trends\n"
        response += "- Best practices and frameworks\n"
        response += "- Webinars and expert interviews\n\n"
        
        response += "**2. Product Content (30%)**\n"
        response += "- Feature announcements and demos\n"
        response += "- Use case studies and success stories\n"
        response += "- Product updates and roadmap\n"
        response += "- Behind-the-scenes development\n\n"
        
        response += "**3. Community Content (20%)**\n"
        response += "- User-generated content and testimonials\n"
        response += "- Community highlights and events\n"
        response += "- Q&A sessions and feedback\n"
        response += "- Partner collaborations\n\n"
        
        response += "**4. Thought Leadership (10%)**\n"
        response += "- Industry predictions and opinions\n"
        response += "- Research findings and reports\n"
        response += "- Speaking at conferences and events\n"
        response += "- Executive insights and vision\n\n"
        
        response += "**📱 Content Distribution Strategy:**\n"
        response += "- Blog: Long-form educational content\n"
        response += "- LinkedIn: Professional networking and B2B\n"
        response += "- Twitter: Quick updates and engagement\n"
        response += "- YouTube: Video tutorials and demos\n"
        response += "- Email: Nurture sequences and updates\n\n"
        
        response += "**📊 Content Success Metrics:**\n"
        response += "- Engagement rates and social shares\n"
        response += "- Website traffic and lead generation\n"
        response += "- Brand awareness and mention tracking\n"
        response += "- Conversion rates from content to trial"
        
        return response

    async def _develop_narrative(self, message: str) -> str:
        """Develop compelling narrative and messaging"""
        response = "Let me help you craft a compelling brand narrative:\n\n"
        
        response += "**📖 Brand Story Framework:**\n\n"
        
        response += "**1. The Hero's Journey Structure:**\n"
        response += "- Hero: Your target customer\n"
        response += "- Problem: The challenge they face daily\n"
        response += "- Guide: Your company as the mentor\n"
        response += "- Plan: Your solution and process\n"
        response += "- Success: The transformation you enable\n\n"
        
        response += "**2. Core Messaging Architecture:**\n\n"
        
        response += "**Mission Statement:**\n"
        response += "- What: What you do (clear and simple)\n"
        response += "- Who: Who you serve (specific target)\n"
        response += "- Why: Why it matters (emotional connection)\n\n"
        
        response += "**Value Proposition:**\n"
        response += "- For [target customer]\n"
        response += "- Who [specific problem]\n"
        response += "- Our product is [solution category]\n"
        response += "- That [key benefit]\n"
        response += "- Unlike [alternative]\n"
        response += "- We [unique differentiator]\n\n"
        
        response += "**3. Key Messages by Audience:**\n\n"
        
        response += "**For Users:**\n"
        response += "- Focus on time savings and efficiency\n"
        response += "- Emphasize ease of use and reliability\n"
        response += "- Highlight immediate benefits\n\n"
        
        response += "**For Decision Makers:**\n"
        response += "- ROI and cost savings\n"
        response += "- Risk mitigation and compliance\n"
        response += "- Scalability and future-proofing\n\n"
        
        response += "**For Investors:**\n"
        response += "- Market size and growth potential\n"
        response += "- Competitive advantages and moats\n"
        response += "- Scalable business model\n\n"
        
        response += "**🎯 Messaging Guidelines:**\n"
        response += "- Keep language simple and jargon-free\n"
        response += "- Lead with benefits, support with features\n"
        response += "- Use customer language and pain points\n"
        response += "- Test messages with real customers"
        
        return response

    async def _general_content_advice(self, message: str) -> str:
        """Provide general content and communications advice"""
        response = "Here's my content strategy recommendation:\n\n"
        
        response += "**✍️ Content Creation Framework:**\n\n"
        
        response += "**1. Audience-First Approach:**\n"
        response += "- Start with customer research and personas\n"
        response += "- Map content to customer journey stages\n"
        response += "- Address specific pain points and questions\n"
        response += "- Use customer language and terminology\n\n"
        
        response += "**2. Content Quality Standards:**\n"
        response += "- Provide genuine value in every piece\n"
        response += "- Maintain consistent brand voice and tone\n"
        response += "- Ensure accuracy and credibility\n"
        response += "- Optimize for readability and engagement\n\n"
        
        response += "**3. Distribution and Amplification:**\n"
        response += "- Choose channels where your audience lives\n"
        response += "- Repurpose content across multiple formats\n"
        response += "- Leverage employee and customer advocacy\n"
        response += "- Build relationships with industry influencers\n\n"
        
        response += "**📈 Content Performance Optimization:**\n"
        response += "- A/B test headlines and formats\n"
        response += "- Analyze engagement patterns and preferences\n"
        response += "- Iterate based on performance data\n"
        response += "- Stay updated on platform algorithm changes\n\n"
        
        response += "**🚀 Content Innovation Ideas:**\n"
        response += "- Interactive content and tools\n"
        response += "- User-generated content campaigns\n"
        response += "- Live streaming and real-time engagement\n"
        response += "- Collaborative content with partners\n\n"
        
        response += "What specific content challenge can I help you tackle?"
        
        return response

    async def create_pitch_deck(self, project_description: str, target_audience: str) -> Dict[str, Any]:
        """Create a detailed pitch deck structure"""
        try:
            await self._simulate_processing_time(2.0, 3.5)
            
            deck = {
                "title": f"Pitch Deck: {project_description}",
                "target_audience": target_audience,
                "slides": [
                    {
                        "slide_number": 1,
                        "title": "Company Introduction",
                        "content": "Hook + Company name and tagline",
                        "speaker_notes": "Start with attention-grabbing problem statement"
                    },
                    {
                        "slide_number": 2,
                        "title": "Problem",
                        "content": "Define the pain point your target customers face",
                        "speaker_notes": "Make this relatable and quantifiable"
                    },
                    {
                        "slide_number": 3,
                        "title": "Solution",
                        "content": "Your unique approach to solving the problem",
                        "speaker_notes": "Connect directly back to the problem slide"
                    },
                    {
                        "slide_number": 4,
                        "title": "Market Opportunity",
                        "content": "TAM, SAM, SOM analysis with growth projections",
                        "speaker_notes": "Focus on realistic capture, not just total market"
                    },
                    {
                        "slide_number": 5,
                        "title": "Product Demo",
                        "content": "Live demo or compelling product screenshots",
                        "speaker_notes": "Show, don't tell - let the product speak"
                    },
                    {
                        "slide_number": 6,
                        "title": "Business Model",
                        "content": "Revenue streams and pricing strategy",
                        "speaker_notes": "Explain how you make money clearly"
                    },
                    {
                        "slide_number": 7,
                        "title": "Traction",
                        "content": "Key metrics, customers, and growth",
                        "speaker_notes": "Show momentum and validation"
                    },
                    {
                        "slide_number": 8,
                        "title": "Competition",
                        "content": "Competitive landscape and differentiation",
                        "speaker_notes": "Acknowledge competition but highlight your edge"
                    },
                    {
                        "slide_number": 9,
                        "title": "Go-to-Market Strategy",
                        "content": "Customer acquisition and growth plan",
                        "speaker_notes": "Show you understand how to scale"
                    },
                    {
                        "slide_number": 10,
                        "title": "Team",
                        "content": "Founding team and key hires",
                        "speaker_notes": "Highlight relevant experience and expertise"
                    },
                    {
                        "slide_number": 11,
                        "title": "Financials",
                        "content": "Revenue projections and key metrics",
                        "speaker_notes": "Be realistic but show growth potential"
                    },
                    {
                        "slide_number": 12,
                        "title": "Funding Ask",
                        "content": "Investment amount and use of funds",
                        "speaker_notes": "Clear ask with specific fund allocation"
                    }
                ],
                "key_points": [
                    "Keep slides visual and minimal text",
                    "Tell a story that flows logically",
                    "Practice timing - aim for 10-12 minutes",
                    "Prepare for questions and objections",
                    "Have appendix slides for detailed questions"
                ],
                "call_to_action": f"Investment opportunity for {target_audience}"
            }
            
            return deck
            
        except Exception as e:
            logger.error(f"Error creating pitch deck: {e}")
            raise