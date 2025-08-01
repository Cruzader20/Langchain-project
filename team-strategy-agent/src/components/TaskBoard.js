'use client'

import { useState } from 'react'
import { Plus, Clock, User, Flag, Calendar, MoreVertical, CheckCircle2 } from 'lucide-react'

export default function TaskBoard({ tasks, setTasks, agents }) {
  const [showNewTaskForm, setShowNewTaskForm] = useState(false)
  const [newTask, setNewTask] = useState({
    title: '',
    description: '',
    priority: 'medium',
    assignedTo: '',
    dueDate: '',
    sprint: 'current'
  })

  const columns = [
    { id: 'todo', title: 'To Do', color: 'bg-gray-100' },
    { id: 'inprogress', title: 'In Progress', color: 'bg-blue-100' },
    { id: 'review', title: 'Review', color: 'bg-yellow-100' },
    { id: 'done', title: 'Done', color: 'bg-green-100' }
  ]

  const priorities = {
    low: { color: 'bg-green-100 text-green-800', label: 'Low' },
    medium: { color: 'bg-yellow-100 text-yellow-800', label: 'Medium' },
    high: { color: 'bg-red-100 text-red-800', label: 'High' }
  }

  // Sample tasks for demo
  const sampleTasks = [
    {
      id: '1',
      title: 'Market Research for AI Finance Tool',
      description: 'Research competitors and market opportunities in AI finance space',
      status: 'todo',
      priority: 'high',
      assignedTo: 'market',
      assignedAgent: 'Market Analyst',
      createdBy: 'PM Agent',
      dueDate: '2024-01-20',
      sprint: 'current',
      tags: ['research', 'finance', 'ai']
    },
    {
      id: '2',
      title: 'Technical Architecture Design',
      description: 'Design system architecture and choose tech stack',
      status: 'inprogress',
      priority: 'high',
      assignedTo: 'tech',
      assignedAgent: 'Tech Architect',
      createdBy: 'PM Agent',
      dueDate: '2024-01-22',
      sprint: 'current',
      tags: ['architecture', 'backend']
    },
    {
      id: '3',
      title: 'User Persona Development',
      description: 'Create detailed user personas for target audience',
      status: 'review',
      priority: 'medium',
      assignedTo: 'pm',
      assignedAgent: 'Product Manager',
      createdBy: 'Market Analyst',
      dueDate: '2024-01-18',
      sprint: 'current',
      tags: ['ux', 'personas']
    },
    {
      id: '4',
      title: 'Pitch Deck Creation',
      description: 'Create compelling pitch deck for stakeholders',
      status: 'done',
      priority: 'medium',
      assignedTo: 'pitch',
      assignedAgent: 'Pitch Writer',
      createdBy: 'PM Agent',
      dueDate: '2024-01-15',
      sprint: 'current',
      tags: ['presentation', 'pitch']
    }
  ]

  const currentTasks = tasks.length > 0 ? tasks : sampleTasks

  const handleCreateTask = (e) => {
    e.preventDefault()
    const task = {
      id: Date.now().toString(),
      ...newTask,
      status: 'todo',
      assignedAgent: agents.find(a => a.id === newTask.assignedTo)?.name || '',
      createdBy: 'You',
      tags: []
    }
    setTasks(prev => [...prev, task])
    setNewTask({
      title: '',
      description: '',
      priority: 'medium',
      assignedTo: '',
      dueDate: '',
      sprint: 'current'
    })
    setShowNewTaskForm(false)
  }

  const moveTask = (taskId, newStatus) => {
    setTasks(prev => prev.map(task =>
      task.id === taskId ? { ...task, status: newStatus } : task
    ))
  }

  const getTasksByStatus = (status) => {
    return currentTasks.filter(task => task.status === status)
  }

  const getAgentAvatar = (agentId) => {
    const agent = agents.find(a => a.id === agentId)
    return agent?.avatar || '👤'
  }

  const formatDate = (dateString) => {
    const date = new Date(dateString)
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Sprint Board</h2>
          <p className="text-gray-600">Manage tasks and track progress across your team</p>
        </div>
        <button
          onClick={() => setShowNewTaskForm(true)}
          className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 flex items-center space-x-2"
        >
          <Plus className="h-4 w-4" />
          <span>New Task</span>
        </button>
      </div>

      {/* Sprint Stats */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {columns.map(column => {
          const tasks = getTasksByStatus(column.id)
          return (
            <div key={column.id} className="bg-white p-4 rounded-lg border">
              <div className="flex items-center justify-between">
                <h3 className="font-medium text-gray-900">{column.title}</h3>
                <span className="text-2xl font-bold text-gray-600">{tasks.length}</span>
              </div>
            </div>
          )
        })}
      </div>

      {/* Kanban Board */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {columns.map(column => (
          <div key={column.id} className="bg-white rounded-lg border">
            <div className={`p-4 ${column.color} rounded-t-lg border-b`}>
              <h3 className="font-semibold text-gray-900 flex items-center justify-between">
                {column.title}
                <span className="bg-white rounded-full px-2 py-1 text-xs font-medium">
                  {getTasksByStatus(column.id).length}
                </span>
              </h3>
            </div>
            <div className="p-4 space-y-3 min-h-[400px]">
              {getTasksByStatus(column.id).map(task => (
                <div
                  key={task.id}
                  className="bg-gray-50 rounded-lg p-3 border hover:shadow-md transition-shadow cursor-move"
                  draggable
                  onDragStart={(e) => e.dataTransfer.setData('text/plain', task.id)}
                  onDragOver={(e) => e.preventDefault()}
                  onDrop={(e) => {
                    e.preventDefault()
                    const draggedTaskId = e.dataTransfer.getData('text/plain')
                    moveTask(draggedTaskId, column.id)
                  }}
                >
                  {/* Task Header */}
                  <div className="flex items-start justify-between mb-2">
                    <h4 className="font-medium text-gray-900 text-sm leading-tight">
                      {task.title}
                    </h4>
                    <button className="text-gray-400 hover:text-gray-600">
                      <MoreVertical className="h-4 w-4" />
                    </button>
                  </div>

                  {/* Task Description */}
                  <p className="text-xs text-gray-600 mb-3 line-clamp-2">
                    {task.description}
                  </p>

                  {/* Task Tags */}
                  {task.tags && task.tags.length > 0 && (
                    <div className="flex flex-wrap gap-1 mb-3">
                      {task.tags.slice(0, 2).map(tag => (
                        <span
                          key={tag}
                          className="px-2 py-1 bg-blue-100 text-blue-700 text-xs rounded-full"
                        >
                          {tag}
                        </span>
                      ))}
                      {task.tags.length > 2 && (
                        <span className="px-2 py-1 bg-gray-100 text-gray-600 text-xs rounded-full">
                          +{task.tags.length - 2}
                        </span>
                      )}
                    </div>
                  )}

                  {/* Task Footer */}
                  <div className="flex items-center justify-between text-xs">
                    <div className="flex items-center space-x-2">
                      {/* Priority */}
                      <span className={`px-2 py-1 rounded-full text-xs font-medium ${priorities[task.priority].color}`}>
                        {priorities[task.priority].label}
                      </span>
                      
                      {/* Assignee */}
                      <div className="flex items-center space-x-1">
                        <span>{getAgentAvatar(task.assignedTo)}</span>
                        <span className="text-gray-600">{task.assignedAgent}</span>
                      </div>
                    </div>

                    {/* Due Date */}
                    {task.dueDate && (
                      <div className="flex items-center space-x-1 text-gray-500">
                        <Calendar className="h-3 w-3" />
                        <span>{formatDate(task.dueDate)}</span>
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* New Task Modal */}
      {showNewTaskForm && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 w-full max-w-md mx-4">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Create New Task</h3>
            <form onSubmit={handleCreateTask} className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Title
                </label>
                <input
                  type="text"
                  value={newTask.title}
                  onChange={(e) => setNewTask(prev => ({ ...prev, title: e.target.value }))}
                  className="w-full rounded-lg border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  required
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Description
                </label>
                <textarea
                  value={newTask.description}
                  onChange={(e) => setNewTask(prev => ({ ...prev, description: e.target.value }))}
                  className="w-full rounded-lg border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  rows={3}
                />
              </div>
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Priority
                  </label>
                  <select
                    value={newTask.priority}
                    onChange={(e) => setNewTask(prev => ({ ...prev, priority: e.target.value }))}
                    className="w-full rounded-lg border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  >
                    <option value="low">Low</option>
                    <option value="medium">Medium</option>
                    <option value="high">High</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Assign to
                  </label>
                  <select
                    value={newTask.assignedTo}
                    onChange={(e) => setNewTask(prev => ({ ...prev, assignedTo: e.target.value }))}
                    className="w-full rounded-lg border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                  >
                    <option value="">Select agent...</option>
                    {agents.filter(a => a.active).map(agent => (
                      <option key={agent.id} value={agent.id}>
                        {agent.avatar} {agent.name}
                      </option>
                    ))}
                  </select>
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Due Date
                </label>
                <input
                  type="date"
                  value={newTask.dueDate}
                  onChange={(e) => setNewTask(prev => ({ ...prev, dueDate: e.target.value }))}
                  className="w-full rounded-lg border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div className="flex justify-end space-x-3 pt-4">
                <button
                  type="button"
                  onClick={() => setShowNewTaskForm(false)}
                  className="px-4 py-2 text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
                >
                  Create Task
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}