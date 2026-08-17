import React from 'react';
import { ShieldCheck, Search, History, Database, BookOpen } from 'lucide-react';

export const Navbar = ({ activeTab, setActiveTab }) => {
  return (
    <header className="glass-panel" style={{ borderRadius: 0, borderTop: 0, borderLeft: 0, borderRight: 0, marginBottom: '32px' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '16px 24px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', cursor: 'pointer' }} onClick={() => setActiveTab('check')}>
          <div style={{ background: 'var(--grad-primary)', padding: '10px', borderRadius: '12px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <ShieldCheck size={26} color="#FFF" />
          </div>
          <div>
            <h1 style={{ fontSize: '1.4rem', fontWeight: 700, color: '#FFF' }}>PRGI Title Verifier</h1>
            <p style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>Press Registrar General of India • Automated Title Engine</p>
          </div>
        </div>

        <nav style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
          <button
            onClick={() => setActiveTab('check')}
            style={{
              background: activeTab === 'check' ? 'rgba(59, 130, 246, 0.2)' : 'transparent',
              color: activeTab === 'check' ? '#60A5FA' : 'var(--text-secondary)',
              border: activeTab === 'check' ? '1px solid rgba(59, 130, 246, 0.4)' : '1px solid transparent',
              padding: '10px 18px',
              borderRadius: '10px',
              fontWeight: 600,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              transition: 'all 0.2s ease'
            }}
          >
            <Search size={18} /> Title Checker
          </button>

          <button
            onClick={() => setActiveTab('submissions')}
            style={{
              background: activeTab === 'submissions' ? 'rgba(59, 130, 246, 0.2)' : 'transparent',
              color: activeTab === 'submissions' ? '#60A5FA' : 'var(--text-secondary)',
              border: activeTab === 'submissions' ? '1px solid rgba(59, 130, 246, 0.4)' : '1px solid transparent',
              padding: '10px 18px',
              borderRadius: '10px',
              fontWeight: 600,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              transition: 'all 0.2s ease'
            }}
          >
            <History size={18} /> Previous Submissions
          </button>

          <button
            onClick={() => setActiveTab('database')}
            style={{
              background: activeTab === 'database' ? 'rgba(59, 130, 246, 0.2)' : 'transparent',
              color: activeTab === 'database' ? '#60A5FA' : 'var(--text-secondary)',
              border: activeTab === 'database' ? '1px solid rgba(59, 130, 246, 0.4)' : '1px solid transparent',
              padding: '10px 18px',
              borderRadius: '10px',
              fontWeight: 600,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              transition: 'all 0.2s ease'
            }}
          >
            <Database size={18} /> Database Viewer
          </button>

          <button
            onClick={() => setActiveTab('guidelines')}
            style={{
              background: activeTab === 'guidelines' ? 'rgba(139, 92, 246, 0.2)' : 'transparent',
              color: activeTab === 'guidelines' ? '#C4B5FD' : 'var(--text-secondary)',
              border: activeTab === 'guidelines' ? '1px solid rgba(139, 92, 246, 0.4)' : '1px solid transparent',
              padding: '10px 18px',
              borderRadius: '10px',
              fontWeight: 600,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              transition: 'all 0.2s ease'
            }}
          >
            <BookOpen size={18} /> Guidelines
          </button>
        </nav>
      </div>
    </header>
  );
};
