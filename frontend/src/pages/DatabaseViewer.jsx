import React, { useState, useEffect } from 'react';
import { getDatabaseTitlesApi, getDatabaseStatsApi } from '../services/api';
import { SearchBar } from '../components/database/SearchBar';
import { FilterBar } from '../components/database/FilterBar';
import { TitleTable } from '../components/database/TitleTable';
import { Pagination } from '../components/database/Pagination';
import { Database, FileText, CheckCircle, XCircle } from 'lucide-react';

export const DatabaseViewer = () => {
  const [items, setItems] = useState([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [search, setSearch] = useState('');
  const [language, setLanguage] = useState('all');
  const [loading, setLoading] = useState(false);
  const [stats, setStats] = useState(null);

  const fetchTitles = async () => {
    setLoading(true);
    try {
      const data = await getDatabaseTitlesApi(page, 15, search, language);
      setItems(data.items);
      setTotal(data.total);
      setTotalPages(data.total_pages);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const fetchStats = async () => {
    try {
      const data = await getDatabaseStatsApi();
      setStats(data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchStats();
  }, []);

  useEffect(() => {
    fetchTitles();
  }, [page, search, language]);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      <div>
        <h2 style={{ fontSize: '1.8rem', color: '#FFF', fontWeight: 700 }}>PRGI Title Database Viewer</h2>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem', marginTop: '4px' }}>
          Read-only view of ~160,000 registered publication titles maintained by Press Registrar General of India.
        </p>
      </div>

      {stats && (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '16px' }}>
          <div className="glass-panel" style={{ padding: '16px 20px', display: 'flex', alignItems: 'center', gap: '16px' }}>
            <Database size={24} color="var(--accent-cyan)" />
            <div>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Registered Database</span>
              <h4 style={{ fontSize: '1.4rem', color: '#FFF', fontWeight: 700 }}>{stats.total_registered_titles}</h4>
            </div>
          </div>

          <div className="glass-panel" style={{ padding: '16px 20px', display: 'flex', alignItems: 'center', gap: '16px' }}>
            <FileText size={24} color="var(--accent-blue)" />
            <div>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Total Verification Requests</span>
              <h4 style={{ fontSize: '1.4rem', color: '#FFF', fontWeight: 700 }}>{stats.total_submissions}</h4>
            </div>
          </div>

          <div className="glass-panel" style={{ padding: '16px 20px', display: 'flex', alignItems: 'center', gap: '16px' }}>
            <CheckCircle size={24} color="#34D399" />
            <div>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Verified Applications</span>
              <h4 style={{ fontSize: '1.4rem', color: '#34D399', fontWeight: 700 }}>{stats.accepted_submissions}</h4>
            </div>
          </div>

          <div className="glass-panel" style={{ padding: '16px 20px', display: 'flex', alignItems: 'center', gap: '16px' }}>
            <XCircle size={24} color="#F87171" />
            <div>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Rejected Applications</span>
              <h4 style={{ fontSize: '1.4rem', color: '#F87171', fontWeight: 700 }}>{stats.rejected_submissions}</h4>
            </div>
          </div>
        </div>
      )}

      {/* Controls Bar */}
      <div className="glass-panel" style={{ padding: '16px 20px', display: 'flex', gap: '16px', flexWrap: 'wrap', alignItems: 'center' }}>
        <SearchBar value={search} onChange={(val) => { setSearch(val); setPage(1); }} />
        <FilterBar language={language} onLanguageChange={(lang) => { setLanguage(lang); setPage(1); }} />
      </div>

      <TitleTable items={items} loading={loading} />

      <Pagination
        page={page}
        totalPages={totalPages}
        totalItems={total}
        onPageChange={setPage}
      />
    </div>
  );
};
