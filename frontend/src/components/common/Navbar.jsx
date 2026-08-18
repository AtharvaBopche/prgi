import React from 'react';
import { ShieldCheck, Search, History, Database, BookOpen } from 'lucide-react';

export const Navbar = ({ activeTab, setActiveTab }) => {
  return (
    <header className="navbar glass-panel">
      <div className="navbar-inner">
        <button className="brand" onClick={() => setActiveTab('check')}>
          <span className="brand-icon">
            <ShieldCheck size={26} color="#FFF" />
          </span>
          <span>
            <span className="brand-title">PRGI Title Verifier</span>
            <span className="brand-subtitle">Press Registrar General of India • Automated Title Engine</span>
          </span>
        </button>

        <nav className="navbar-links" aria-label="Main navigation">
          <button
            onClick={() => setActiveTab('check')}
            className={`nav-button ${activeTab === 'check' ? 'is-active' : ''}`}
          >
            <Search size={18} /> Title Checker
          </button>

          <button
            onClick={() => setActiveTab('submissions')}
            className={`nav-button ${activeTab === 'submissions' ? 'is-active' : ''}`}
          >
            <History size={18} /> Previous Submissions
          </button>

          <button
            onClick={() => setActiveTab('database')}
            className={`nav-button ${activeTab === 'database' ? 'is-active' : ''}`}
          >
            <Database size={18} /> Database Viewer
          </button>

          <button
            onClick={() => setActiveTab('guidelines')}
            className={`nav-button nav-button-guidelines ${activeTab === 'guidelines' ? 'is-active' : ''}`}
          >
            <BookOpen size={18} /> Guidelines
          </button>
        </nav>
      </div>
    </header>
  );
};
