import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    """Base class for all AI agents in the team strategy system"""
    
    def __init__(self, agent_id: str, name: str, role: str):
        self.agent_id = agent_id
        self.name = name
        self.role = role
        self.created_at = datetime.now()
        self.message_count = 0
        self.active = True
        
    @abstractmethod
    async def process_message(self, message: str) -> str:
        """Process a user message and return a response"""
        pass
    
    async def get_status(self) -> Dict[str, Any]:
        """Get current agent status"""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "role": self.role,
            "active": self.active,
            "message_count": self.message_count,
            "uptime": (datetime.now() - self.created_at).total_seconds()
        }
    
    async def set_active(self, active: bool):
        """Set agent active status"""
        self.active = active
        logger.info(f"Agent {self.agent_id} active status set to: {active}")
    
    def _increment_message_count(self):
        """Increment the message counter"""
        self.message_count += 1
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract keywords from text for analysis"""
        import re
        # Simple keyword extraction
        words = re.findall(r'\w+', text.lower())
        # Filter out common words
        common_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'a', 'an', 'as', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can'}
        keywords = [word for word in words if word not in common_words and len(word) > 2]
        return list(set(keywords))  # Remove duplicates
    
    def _format_response(self, content: str, add_signature: bool = True) -> str:
        """Format response with agent signature if needed"""
        if add_signature and not content.endswith(f"\n\n— {self.name}"):
            content += f"\n\n— {self.name}"
        return content
    
    def _log_interaction(self, message: str, response: str):
        """Log agent interactions for monitoring"""
        self._increment_message_count()
        logger.info(f"Agent {self.agent_id} processed message. Count: {self.message_count}")
        logger.debug(f"Input: {message[:100]}...")
        logger.debug(f"Output: {response[:100]}...")
    
    async def _simulate_processing_time(self, min_seconds: float = 0.5, max_seconds: float = 2.0):
        """Simulate realistic processing time"""
        import random
        delay = random.uniform(min_seconds, max_seconds)
        await asyncio.sleep(delay)