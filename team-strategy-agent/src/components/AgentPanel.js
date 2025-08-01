'use client'

import { useState } from 'react'
import { Settings, Power, User, Briefcase, BarChart3, FileText, Calendar } from 'lucide-react'

export default function AgentPanel({ agents, setAgents }) {
  const [selectedAgent, setSelectedAgent] = useState(null)

  const toggleAgent = (agentId) => {
    setAgents(prev => prev.map(agent => 
      agent.id === agentId 
        ? { ...agent, active: !agent.active }
        : agent
    ))
  }

  const getAgentIcon = (agentId) => {
    const icons = {
      pm: Briefcase,
      tech: Settings,
      market: BarChart3,
      pitch: FileText,
      sprint: Calendar
    }
    return icons[agentId] || User
  }

  const agentDescriptions = {
    pm: {
      description: "Breaks down feature ideas into specs and milestones, manages product roadmap",
      capabilities: [
        "Feature specification",
        "Roadmap planning", 
        "User story creation",
        "Requirements analysis"
      ],
      expertise: "Product Strategy, User Experience, Agile Methodology"
    },
    tech: {
      description: "Suggests tech stack, builds initial design, and provides technical guidance",
      capabilities: [
        "Architecture design",
        "Technology recommendations",
        "Technical feasibility analysis",
        "Code structure planning"
      ],
      expertise: "Full-stack Development, Cloud Architecture, DevOps"
    },
    market: {
      description: "Scrapes and summarizes competitor strategies, analyzes market opportunities",
      capabilities: [
        "Competitive analysis",
        "Market research",
        "Trend identification",
        "Pricing strategy"
      ],
      expertise: "Market Research, Business Intelligence, Data Analysis"
    },
    pitch: {
      description: "Drafts presentations, decks, and compelling content for stakeholders",
      capabilities: [
        "Presentation creation",
        "Content writing",
        "Storytelling",
        "Stakeholder communication"
      ],
      expertise: "Business Writing, Presentation Design, Communications"
    },
    sprint: {
      description: "Allocates tasks over weekly sprints and manages project timelines",
      capabilities: [
        "Sprint planning",
        "Task allocation",
        "Timeline management",
        "Progress tracking"
      ],
      expertise: "Agile Planning, Project Management, Resource Allocation"
    }
  }

  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
      {/* Agent Cards */}
      <div className="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-4">
        {agents.map((agent) => {
          const IconComponent = getAgentIcon(agent.id)
          const isSelected = selectedAgent?.id === agent.id
          
          return (
            <div
              key={agent.id}
              className={`bg-white rounded-lg border p-6 cursor-pointer transition-all duration-200 ${
                isSelected 
                  ? 'border-blue-500 shadow-lg' 
                  : 'border-gray-200 hover:border-gray-300 hover:shadow-md'
              } ${!agent.active ? 'opacity-60' : ''}`}
              onClick={() => setSelectedAgent(isSelected ? null : agent)}
            >
              {/* Agent Header */}
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center space-x-3">
                  <div className="text-2xl">{agent.avatar}</div>
                  <div>
                    <h3 className="font-semibold text-gray-900">{agent.name}</h3>
                    <p className="text-sm text-gray-600">{agent.role}</p>
                  </div>
                </div>
                <button
                  onClick={(e) => {
                    e.stopPropagation()
                    toggleAgent(agent.id)
                  }}
                  className={`p-2 rounded-full transition-colors ${
                    agent.active 
                      ? 'bg-green-100 text-green-600 hover:bg-green-200' 
                      : 'bg-gray-100 text-gray-400 hover:bg-gray-200'
                  }`}
                  title={agent.active ? 'Deactivate agent' : 'Activate agent'}
                >
                  <Power className="h-4 w-4" />
                </button>
              </div>

              {/* Agent Status */}
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-2">
                  <IconComponent className="h-4 w-4 text-gray-400" />
                  <span className="text-sm text-gray-600">
                    {agent.active ? 'Active' : 'Inactive'}
                  </span>
                </div>
                <div className={`w-2 h-2 rounded-full ${
                  agent.active ? 'bg-green-500' : 'bg-gray-300'
                }`}></div>
              </div>

              {/* Quick Description */}
              <p className="text-sm text-gray-500 mt-3 line-clamp-2">
                {agentDescriptions[agent.id]?.description}
              </p>
            </div>
          )
        })}
      </div>

      {/* Agent Details Panel */}
      <div className="lg:col-span-1">
        {selectedAgent ? (
          <div className="bg-white rounded-lg border p-6 sticky top-6">
            <div className="flex items-center space-x-3 mb-4">
              <div className="text-3xl">{selectedAgent.avatar}</div>
              <div>
                <h2 className="text-xl font-semibold text-gray-900">
                  {selectedAgent.name}
                </h2>
                <p className="text-gray-600">{selectedAgent.role}</p>
              </div>
            </div>

            <div className="space-y-6">
              {/* Description */}
              <div>
                <h3 className="font-medium text-gray-900 mb-2">Description</h3>
                <p className="text-sm text-gray-600">
                  {agentDescriptions[selectedAgent.id]?.description}
                </p>
              </div>

              {/* Capabilities */}
              <div>
                <h3 className="font-medium text-gray-900 mb-2">Key Capabilities</h3>
                <ul className="space-y-1">
                  {agentDescriptions[selectedAgent.id]?.capabilities.map((capability, index) => (
                    <li key={index} className="text-sm text-gray-600 flex items-center">
                      <span className="w-1.5 h-1.5 bg-blue-400 rounded-full mr-2"></span>
                      {capability}
                    </li>
                  ))}
                </ul>
              </div>

              {/* Expertise */}
              <div>
                <h3 className="font-medium text-gray-900 mb-2">Expertise</h3>
                <p className="text-sm text-gray-600">
                  {agentDescriptions[selectedAgent.id]?.expertise}
                </p>
              </div>

              {/* Status & Actions */}
              <div className="border-t pt-4">
                <div className="flex items-center justify-between mb-3">
                  <span className="text-sm font-medium text-gray-700">Status</span>
                  <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                    selectedAgent.active 
                      ? 'bg-green-100 text-green-800' 
                      : 'bg-gray-100 text-gray-800'
                  }`}>
                    {selectedAgent.active ? 'Active' : 'Inactive'}
                  </span>
                </div>
                <button
                  onClick={() => toggleAgent(selectedAgent.id)}
                  className={`w-full py-2 px-4 rounded-lg font-medium transition-colors ${
                    selectedAgent.active
                      ? 'bg-red-100 text-red-700 hover:bg-red-200'
                      : 'bg-green-100 text-green-700 hover:bg-green-200'
                  }`}
                >
                  {selectedAgent.active ? 'Deactivate Agent' : 'Activate Agent'}
                </button>
              </div>
            </div>
          </div>
        ) : (
          <div className="bg-white rounded-lg border p-6 text-center">
            <User className="mx-auto h-12 w-12 text-gray-400 mb-4" />
            <h3 className="text-lg font-medium text-gray-900 mb-2">
              Select an Agent
            </h3>
            <p className="text-gray-500">
              Click on an agent card to view detailed information and manage their settings.
            </p>
          </div>
        )}
      </div>

      {/* Team Summary */}
      <div className="lg:col-span-3">
        <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg p-6 border">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Team Overview</h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="text-center">
              <div className="text-2xl font-bold text-blue-600">
                {agents.filter(a => a.active).length}
              </div>
              <div className="text-sm text-gray-600">Active Agents</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-green-600">
                {agents.length}
              </div>
              <div className="text-sm text-gray-600">Total Agents</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-purple-600">5</div>
              <div className="text-sm text-gray-600">Specializations</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-orange-600">24/7</div>
              <div className="text-sm text-gray-600">Availability</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}