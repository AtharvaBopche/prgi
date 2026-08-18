import React, { useState } from 'react';
import { Navbar } from './components/common/Navbar';
import { Footer } from './components/common/Footer';
import { TitleCheck } from './pages/TitleCheck';
import { PreviousSubmissions } from './pages/PreviousSubmissions';
import { DatabaseViewer } from './pages/DatabaseViewer';
import { Guidelines } from './pages/Guidelines';

export function App() {
  const [activeTab, setActiveTab] = useState('check');
  // Option B: Submissions stay in React state memory only, disappearing upon page reload
  const [sessionSubmissions, setSessionSubmissions] = useState([]);

  const addSessionSubmission = (result) => {
    if (!result) return;
    const newEntry = {
      submitted_title: result.submitted_title,
      similarity_score: result.highest_similarity,
      verification_probability: result.verification_probability,
      status: result.status,
      rejection_reasons: result.guideline_violations ? result.guideline_violations.map(v => v.message) : [],
      submitted_at: result.processed_at || new Date().toISOString()
    };
    setSessionSubmissions(prev => [newEntry, ...prev.filter(item => item.submitted_title !== result.submitted_title)]);
  };

  return (
    <div className="app-shell">
      <Navbar activeTab={activeTab} setActiveTab={setActiveTab} />
      
      <main className="app-main">
        {activeTab === 'check' && (
          <TitleCheck onSubmissionCreated={addSessionSubmission} />
        )}
        {activeTab === 'submissions' && (
          <PreviousSubmissions submissions={sessionSubmissions} />
        )}
        {activeTab === 'database' && <DatabaseViewer />}
        {activeTab === 'guidelines' && <Guidelines />}
      </main>

      <Footer />
    </div>
  );
}

export default App;
