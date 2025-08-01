'use client'

import { useState, useRef, useEffect } from 'react'
import { Send, Bot, User } from 'lucide-react'

export default function ChatInterface({ messages, setMessages, agents }) {
  const [inputMessage, setInputMessage] = useState('')
  const [isConnected, setIsConnected] = useState(false)
  const [socket, setSocket] = useState(null)
  const messagesEndRef = useRef(null)
  const inputRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  useEffect(() => {
    // Initialize WebSocket connection to backend
    const newSocket = new WebSocket('ws://localhost:8000/ws')

    newSocket.onopen = () => {
      setIsConnected(true)
      console.log('Connected to backend')
    }

    newSocket.onclose = () => {
      setIsConnected(false)
      console.log('Disconnected from backend')
    }

    newSocket.onmessage = (event) => {
      try {
        const response = JSON.parse(event.data)
        if (response.type === 'agent') {
          setMessages(prev => [...prev, response])
        }
      } catch (e) {
        console.error('Error parsing WebSocket message:', e)
      }
    }

    newSocket.onerror = (error) => {
      console.error('WebSocket error:', error)
      setIsConnected(false)
    }

    setSocket(newSocket)

    return () => {
      if (newSocket.readyState === WebSocket.OPEN) {
        newSocket.close()
      }
    }
  }, [setMessages])

  const handleSendMessage = async (e) => {
    e.preventDefault()
    if (!inputMessage.trim()) return

    const userMessage = {
      id: Date.now(),
      type: 'user',
      content: inputMessage,
      timestamp: new Date().toISOString(),
      sender: 'You'
    }

    setMessages(prev => [...prev, userMessage])

    // Send to backend via socket if connected
    if (socket && socket.readyState === WebSocket.OPEN) {
      socket.send(JSON.stringify({
        type: 'user_message',
        message: inputMessage,
        agents: agents.filter(a => a.active).map(a => a.id)
      }))
    } else {
      // Simulate agent responses for demo (remove when backend is connected)
      simulateAgentResponses(inputMessage)
    }

    setInputMessage('')
    inputRef.current?.focus()
  }

  const simulateAgentResponses = (userInput) => {
    // Demo responses - will be replaced with real AI agents
    const responses = [
      {
        id: Date.now() + 1,
        type: 'agent',
        content: `I'll help break down "${userInput}" into actionable components. Let me analyze the requirements and create a structured plan.`,
        timestamp: new Date().toISOString(),
        sender: 'Product Manager',
        agentId: 'pm',
        avatar: '👨‍💼'
      },
      {
        id: Date.now() + 2,
        type: 'agent',
        content: `From a technical perspective, I recommend we start with a modern tech stack. I'll outline the architecture and suggest the best frameworks for this project.`,
        timestamp: new Date().toISOString(),
        sender: 'Tech Architect',
        agentId: 'tech',
        avatar: '👨‍💻'
      },
      {
        id: Date.now() + 3,
        type: 'agent',
        content: `I'll research the competitive landscape and market opportunities. Let me gather data on similar solutions and identify gaps we can fill.`,
        timestamp: new Date().toISOString(),
        sender: 'Market Analyst',
        agentId: 'market',
        avatar: '📊'
      }
    ]

    // Simulate typing delay
    responses.forEach((response, index) => {
      setTimeout(() => {
        setMessages(prev => [...prev, response])
      }, (index + 1) * 1500)
    })
  }

  const formatTimestamp = (timestamp) => {
    return new Date(timestamp).toLocaleTimeString([], { 
      hour: '2-digit', 
      minute: '2-digit' 
    })
  }

  return (
    <div className="flex flex-col h-[600px] bg-white rounded-lg shadow-sm border">
      {/* Chat Header */}
      <div className="flex justify-between items-center p-4 border-b bg-gray-50 rounded-t-lg">
        <div className="flex items-center space-x-2">
          <div className="flex -space-x-2">
            {agents.filter(a => a.active).slice(0, 3).map((agent) => (
              <div
                key={agent.id}
                className="w-8 h-8 rounded-full bg-white border-2 border-white flex items-center justify-center text-sm"
                title={agent.name}
              >
                {agent.avatar}
              </div>
            ))}
            {agents.filter(a => a.active).length > 3 && (
              <div className="w-8 h-8 rounded-full bg-gray-200 border-2 border-white flex items-center justify-center text-xs font-medium">
                +{agents.filter(a => a.active).length - 3}
              </div>
            )}
          </div>
          <div>
            <h3 className="font-medium text-gray-900">Agent Team Chat</h3>
            <p className="text-sm text-gray-500">
              {agents.filter(a => a.active).length} agents ready to help
            </p>
          </div>
        </div>
        <div className="flex items-center space-x-2">
          <div className={`w-2 h-2 rounded-full ${isConnected ? 'bg-green-500' : 'bg-red-500'}`}></div>
          <span className="text-sm text-gray-500">
            {isConnected ? 'Connected' : 'Offline Mode'}
          </span>
        </div>
      </div>

      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.length === 0 && (
          <div className="text-center py-8">
            <Bot className="mx-auto h-12 w-12 text-gray-400 mb-4" />
            <h3 className="text-lg font-medium text-gray-900 mb-2">
              Welcome to Team Strategy Agent
            </h3>
            <p className="text-gray-500 max-w-md mx-auto">
              Describe your startup idea or project goal, and our AI agents will collaborate 
              to help you plan, strategize, and execute. Try something like:
            </p>
            <div className="mt-4 space-y-2 text-sm text-gray-600">
              <p className="bg-gray-50 rounded p-2 max-w-md mx-auto">
                "We want to build an AI tool for finance"
              </p>
              <p className="bg-gray-50 rounded p-2 max-w-md mx-auto">
                "Create a voice AI tutor for kids"
              </p>
            </div>
          </div>
        )}

        {messages.map((message) => (
          <div
            key={message.id}
            className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div className={`max-w-3xl ${message.type === 'user' ? 'order-2' : 'order-1'}`}>
              <div className="flex items-center space-x-2 mb-1">
                {message.type === 'agent' && (
                  <span className="text-lg">{message.avatar}</span>
                )}
                <span className="text-sm font-medium text-gray-700">
                  {message.sender}
                </span>
                <span className="text-xs text-gray-500">
                  {formatTimestamp(message.timestamp)}
                </span>
              </div>
              <div
                className={`rounded-lg px-4 py-2 ${
                  message.type === 'user'
                    ? 'bg-blue-600 text-white'
                    : 'bg-gray-100 text-gray-900'
                }`}
              >
                {message.content}
              </div>
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Area */}
      <form onSubmit={handleSendMessage} className="p-4 border-t bg-gray-50">
        <div className="flex space-x-2">
          <input
            ref={inputRef}
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            placeholder="Describe your startup idea or ask the team for help..."
            className="flex-1 rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            autoFocus
          />
          <button
            type="submit"
            disabled={!inputMessage.trim()}
            className="rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <Send className="h-4 w-4" />
          </button>
        </div>
      </form>
    </div>
  )
}