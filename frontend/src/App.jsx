import React, { useState } from 'react';
import { Navbar } from './components/common/Navbar';
import { Footer } from './components/common/Footer';
import { TitleCheck } from './pages/TitleCheck';
import { PreviousSubmissions } from './pages/PreviousSubmissions';
import { DatabaseViewer } from './pages/DatabaseViewer';
import { Guidelines } from './pages/Guidelines';

export function App() {
  const [activeTab, setActiveTab] = useState('check');
  return (
    <div className="app-shell">
      <Navbar activeTab={activeTab} setActiveTab={setActiveTab} />
      
      <main className="app-main">
        {activeTab === 'check' && (
          <TitleCheck />
        )}
        {activeTab === 'submissions' && (
          <PreviousSubmissions />
        )}
        {activeTab === 'database' && <DatabaseViewer />}
        {activeTab === 'guidelines' && <Guidelines />}
      </main>

      <Footer />
    </div>
  );
}

export default App;
