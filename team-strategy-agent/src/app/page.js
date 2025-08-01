'use client'

import { useState, useEffect, useRef } from 'react'
import ChatInterface from '@/components/ChatInterface'
import AgentPanel from '@/components/AgentPanel'
import TaskBoard from '@/components/TaskBoard'
import { Send, Users, Target, BarChart3 } from 'lucide-react'

export default function Home() {
  const [activeTab, setActiveTab] = useState('chat')
  const [messages, setMessages] = useState([])
  const [agents, setAgents] = useState([
    { id: 'pm', name: 'Product Manager', role: 'PM Agent', active: true, avatar: '👨‍💼' },
    { id: 'tech', name: 'Tech Architect', role: 'Technical Architect', active: true, avatar: '👨‍💻' },
    { id: 'market', name: 'Market Analyst', role: 'Market Analyst', active: true, avatar: '📊' },
    { id: 'pitch', name: 'Pitch Writer', role: 'Pitch Writer', active: true, avatar: '✍️' },
    { id: 'sprint', name: 'Sprint Planner', role: 'Sprint Planner', active: true, avatar: '📋' }
  ])
  const [tasks, setTasks] = useState([])

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <h1 className="text-xl font-bold text-gray-900">Team Strategy Agent</h1>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <span className="text-sm text-gray-500">
                {agents.filter(a => a.active).length} agents active
              </span>
            </div>
          </div>
        </div>
      </header>

      {/* Navigation Tabs */}
      <div className="bg-white border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <nav className="flex space-x-8">
            <button
              onClick={() => setActiveTab('chat')}
              className={`py-4 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'chat'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              <div className="flex items-center">
                <Send className="mr-2 h-4 w-4" />
                Agent Chat
              </div>
            </button>
            <button
              onClick={() => setActiveTab('agents')}
              className={`py-4 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'agents'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              <div className="flex items-center">
                <Users className="mr-2 h-4 w-4" />
                Team Agents
              </div>
            </button>
            <button
              onClick={() => setActiveTab('tasks')}
              className={`py-4 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'tasks'
                  ? 'border-blue-500 text-blue-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              <div className="flex items-center">
                <Target className="mr-2 h-4 w-4" />
                Tasks & Sprints
              </div>
            </button>
          </nav>
        </div>
      </div>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {activeTab === 'chat' && (
          <ChatInterface 
            messages={messages} 
            setMessages={setMessages}
            agents={agents}
          />
        )}
        {activeTab === 'agents' && (
          <AgentPanel 
            agents={agents} 
            setAgents={setAgents}
          />
        )}
        {activeTab === 'tasks' && (
          <TaskBoard 
            tasks={tasks} 
            setTasks={setTasks}
            agents={agents}
          />
        )}
      </main>
    </div>
  )
}
