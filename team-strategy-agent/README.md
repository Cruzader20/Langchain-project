# Team Strategy Agent 🤖

A Real-Time AI-powered team of agents that help startup teams plan, strategize, and execute their projects through collaborative multi-agent conversations.

## 🌟 Features

### AI Team Agents
- **👨‍💼 Product Manager**: Breaks down ideas into actionable specs and milestones
- **👨‍💻 Tech Architect**: Provides technical guidance and architecture recommendations  
- **📊 Market Analyst**: Conducts competitive analysis and market research
- **✍️ Pitch Writer**: Creates compelling presentations and content
- **📋 Sprint Planner**: Manages agile planning and task allocation

### Core Functionality
- **Real-time Chat**: Live conversation with multiple AI agents simultaneously
- **Agent Management**: Toggle agents on/off, view their specializations
- **Task Board**: Kanban-style sprint planning and task management
- **WebSocket Integration**: Real-time bi-directional communication
- **Responsive UI**: Modern, clean interface built with Next.js and Tailwind CSS

## 🏗️ Architecture

### Frontend (Next.js)
```
team-strategy-agent/
├── src/
│   ├── app/
│   │   └── page.js                 # Main application page
│   └── components/
│       ├── ChatInterface.js        # Real-time agent chat
│       ├── AgentPanel.js          # Agent management
│       └── TaskBoard.js           # Sprint planning board
└── package.json
```

### Backend (FastAPI)
```
backend/
├── simple_main.py                 # Main FastAPI application
├── agents/                        # AI agent implementations
│   ├── base_agent.py
│   ├── product_manager_agent.py
│   ├── tech_architect_agent.py
│   ├── market_analyst_agent.py
│   ├── pitch_writer_agent.py
│   └── sprint_planner_agent.py
├── models/
│   └── schemas.py                 # Pydantic data models
└── requirements.txt
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- Python 3.8+
- Git

### 1. Clone the Repository
```bash
git clone <repository-url>
cd team-strategy-agent
```

### 2. Start the Frontend
```bash
# Install dependencies
npm install

# Start development server
npm run dev
```
The frontend will be available at `http://localhost:3000`

### 3. Start the Backend
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn websockets pydantic

# Start the server
python simple_main.py
```
The backend API will be available at `http://localhost:8000`

## 💬 Usage

### Starting a Conversation
1. Open the application at `http://localhost:3000`
2. Navigate to the "Agent Chat" tab
3. Type your startup idea or question, for example:
   - "We want to build an AI tool for finance"
   - "Create a voice AI tutor for kids" 
   - "Help me plan a SaaS product launch"

### Managing Agents
1. Go to the "Team Agents" tab
2. Click on agent cards to view detailed information
3. Use the power button to activate/deactivate specific agents
4. View each agent's capabilities and expertise

### Sprint Planning
1. Access the "Tasks & Sprints" tab
2. Create new tasks and assign them to agents
3. Drag tasks between columns (To Do, In Progress, Review, Done)
4. Set priorities, due dates, and track progress

## 🔧 Technology Stack

### Frontend
- **Framework**: Next.js 14 with App Router
- **Language**: JavaScript
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **Real-time**: Native WebSocket API

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.8+
- **WebSocket**: Built-in FastAPI WebSocket support
- **Data Validation**: Pydantic
- **CORS**: FastAPI CORS middleware

## 🛠️ API Endpoints

### REST API
- `GET /` - Health check
- `GET /api/agents` - Get all agents
- `POST /api/agents/{agent_id}/toggle` - Toggle agent status
- `POST /api/chat/message` - Send message to agents (HTTP alternative)

### WebSocket
- `WS /ws` - Real-time agent communication

## 📊 Agent Capabilities

### Product Manager Agent
- Feature specification and breakdown
- User story creation
- Product roadmap planning
- Requirements analysis
- MVP definition

### Tech Architect Agent  
- System architecture design
- Technology stack recommendations
- Scalability planning
- Security considerations
- DevOps guidance

### Market Analyst Agent
- Competitive landscape analysis
- Market size and opportunity assessment
- Pricing strategy recommendations
- Trend identification
- Go-to-market planning

### Pitch Writer Agent
- Presentation deck creation
- Content strategy development
- Brand narrative crafting
- Stakeholder communication
- Marketing copy writing

### Sprint Planner Agent
- Agile sprint planning
- Task breakdown and estimation
- Resource allocation
- Timeline management
- Velocity tracking

## 🌐 Example Use Cases

### For Startups
- **Idea Validation**: Get instant feedback from multiple expert perspectives
- **MVP Planning**: Break down complex ideas into executable sprint plans
- **Market Research**: Understand competitive landscape and opportunities
- **Pitch Preparation**: Create compelling presentations for investors

### For Product Teams
- **Feature Planning**: Analyze and prioritize new feature development
- **Technical Architecture**: Get guidance on scalable system design
- **Sprint Management**: Optimize team productivity and task allocation
- **Stakeholder Communication**: Craft clear project updates and reports

### For Solo Builders
- **Multi-perspective Analysis**: Get diverse expert opinions on your ideas
- **Knowledge Gaps**: Fill in expertise you might be missing
- **Planning Support**: Structure your development approach
- **Content Creation**: Generate professional documentation and presentations

## 🚧 Development Status

### ✅ Completed Features
- Real-time multi-agent chat interface
- Agent management and configuration
- Task board with drag-and-drop functionality
- WebSocket backend integration
- Responsive UI design

### 🔄 In Progress
- Enhanced AI agent responses with more sophisticated logic
- Database integration for persistent data
- User authentication and sessions
- Advanced sprint planning features

### 📋 Planned Features
- Integration with external tools (Jira, Notion, GitHub)
- AI model integration (OpenAI, Anthropic)
- Advanced market research APIs
- Team collaboration features
- Mobile application

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Guidelines
1. Follow the existing code structure
2. Add appropriate error handling
3. Update documentation for new features
4. Test WebSocket connections thoroughly

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the backend logs for WebSocket connection errors
2. Ensure both frontend (3000) and backend (8000) are running
3. Verify CORS settings if having connection issues
4. Open an issue on GitHub for bug reports

---

**Built with ❤️ for startup teams and solo builders who want AI-powered strategic guidance.**
