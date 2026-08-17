import React from 'react';

export const Footer = () => {
  return (
    <footer style={{ marginTop: '60px', borderTop: '1px solid var(--border-color)', padding: '24px', textAlign: 'center', color: 'var(--text-muted)', fontSize: '0.85rem' }}>
      <p>© {new Date().getFullYear()} Press Registrar General of India (PRGI). Official Title Verification Portal.</p>
      <p style={{ marginTop: '4px' }}>Automated Uniqueness & Guideline Compliance Engine • Powered by Multi-Algorithm Phonetic & Fuzzy Search</p>
    </footer>
  );
};
