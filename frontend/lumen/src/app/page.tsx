// frontend/lumen/src/app/page.tsx
'use client';

import { useState } from 'react';

// Mock data for initial testing before hooking up the backend server
const MOCK_STEPS = [
  { id: 1, agent: 'GitHub Webhook', message: 'Intercepted patch payload for Pull Request #12', status: 'completed' },
  { id: 2, agent: 'Orchestrator Brain', message: 'Parsing git diff entries and allocating tasks...', status: 'active' },
  { id: 3, agent: 'Security Agent', message: 'Scanning source lines for exposed API credentials...', status: 'pending' },
  { id: 4, agent: 'Performance Agent', message: 'Analyzing time complexity indicators...', status: 'pending' },
  { id: 5, agent: 'Quality Agent', message: 'Checking styling rules and naming patterns...', status: 'pending' },
  { id: 6, agent: 'Publisher Agent', message: 'Preparing final markdown comment bundle...', status: 'pending' },
];

export default function Dashboard() {
  const [pipelineSteps, setPipelineSteps] = useState(MOCK_STEPS);
  const [reviewDraft, setReviewDraft] = useState<string>('The multi-agent evaluation report will appear here once analysis concludes.');

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 font-sans p-6 md:p-12">
      {/* Header Panel */}
      <header className="mb-10 border-b border-slate-800 pb-6 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold tracking-tight text-white flex items-center gap-2">
            <span className="inline-block w-3 h-3 bg-indigo-500 rounded-full animate-pulse"></span>
            Lumen AI <span className="text-sm font-normal text-slate-400 bg-slate-900 border border-slate-800 px-2 py-0.5 rounded ml-2">Multi-Agent Control</span>
          </h1>
          <p className="text-slate-400 mt-1 text-sm">Autonomous Event-Driven Pull Request Auditing Engine</p>
        </div>
        <div className="flex gap-4 text-xs font-mono">
          <div className="bg-slate-900 border border-slate-800 px-3 py-2 rounded">
            <span className="text-slate-500">BACKEND:</span> <span className="text-emerald-400">ONLINE</span>
          </div>
        </div>
      </header>

      {/* Main Grid View */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        {/* Left Side: Agent Orchestration Pipeline Tracker */}
        <section className="lg:col-span-5 flex flex-col gap-6">
          <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-xl">
            <h2 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
              📊 Active Agent Tracking Matrix
            </h2>
            
            <div className="flex flex-col gap-4 relative before:absolute before:left-3.5 before:top-2 before:bottom-2 before:w-0.5 before:bg-slate-800">
              {pipelineSteps.map((step) => (
                <div key={step.id} className="flex gap-4 items-start relative z-10 bg-slate-900 py-1">
                  {/* Status Ring Indicator */}
                  <div className={`w-7 h-7 rounded-full flex items-center justify-center font-mono text-xs font-bold shrink-0 shadow-md ${
                    step.status === 'completed' ? 'bg-emerald-950 text-emerald-400 border border-emerald-500/30' :
                    step.status === 'active' ? 'bg-indigo-950 text-indigo-400 border border-indigo-500 border-dashed animate-spin-slow' :
                    'bg-slate-950 text-slate-600 border border-slate-800'
                  }`}>
                    {step.status === 'completed' ? '✓' : step.status === 'active' ? '●' : '○'}
                  </div>
                  
                  {/* Text Description Box */}
                  <div className="flex-1 min-w-0">
                    <div className="flex justify-between items-baseline mb-0.5">
                      <h4 className={`text-sm font-semibold tracking-wide ${step.status === 'active' ? 'text-indigo-400' : 'text-slate-200'}`}>
                        {step.agent}
                      </h4>
                      <span className={`text-[10px] font-mono px-1.5 py-0.5 rounded uppercase font-bold tracking-wider ${
                        step.status === 'completed' ? 'bg-emerald-500/10 text-emerald-400' :
                        step.status === 'active' ? 'bg-indigo-500/10 text-indigo-400 animate-pulse' :
                        'bg-slate-950 text-slate-500'
                      }`}>
                        {step.status}
                      </span>
                    </div>
                    <p className="text-xs text-slate-400 font-mono truncate">{step.message}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Right Side: Generated Live Review Markdown Output Viewer */}
        <section className="lg:col-span-7">
          <div className="bg-slate-900 border border-slate-800 rounded-xl h-full flex flex-col shadow-xl overflow-hidden">
            <div className="bg-slate-900/50 px-6 py-4 border-b border-slate-800 flex justify-between items-center">
              <h2 className="text-lg font-semibold text-white flex items-center gap-2">
                📝 Generated Report Output
              </h2>
              <span className="text-xs font-mono text-slate-500">markdown-preview</span>
            </div>
            
            <div className="p-6 flex-1 overflow-y-auto font-mono text-sm leading-relaxed text-slate-300 whitespace-pre-wrap bg-slate-950/40">
              {reviewDraft}
            </div>
          </div>
        </section>

      </div>
    </div>
  );
}