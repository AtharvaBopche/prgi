import React from 'react';
import { ChevronLeft, ChevronRight } from 'lucide-react';

export const Pagination = ({ page, totalPages, totalItems, onPageChange }) => {
  return (
    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '20px', padding: '0 8px' }}>
      <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
        Showing page <strong style={{ color: '#FFF' }}>{page}</strong> of <strong style={{ color: '#FFF' }}>{totalPages}</strong> ({totalItems} total records)
      </span>

      <div style={{ display: 'flex', gap: '8px' }}>
        <button
          onClick={() => onPageChange(page - 1)}
          disabled={page <= 1}
          style={{
            background: 'rgba(31, 41, 55, 0.8)',
            border: '1px solid var(--border-color)',
            color: page <= 1 ? 'var(--text-muted)' : '#FFF',
            padding: '8px 14px',
            borderRadius: '8px',
            cursor: page <= 1 ? 'not-allowed' : 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
            fontSize: '0.85rem'
          }}
        >
          <ChevronLeft size={16} /> Previous
        </button>

        <button
          onClick={() => onPageChange(page + 1)}
          disabled={page >= totalPages}
          style={{
            background: 'rgba(31, 41, 55, 0.8)',
            border: '1px solid var(--border-color)',
            color: page >= totalPages ? 'var(--text-muted)' : '#FFF',
            padding: '8px 14px',
            borderRadius: '8px',
            cursor: page >= totalPages ? 'not-allowed' : 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
            fontSize: '0.85rem'
          }}
        >
          Next <ChevronRight size={16} />
        </button>
      </div>
    </div>
  );
};
