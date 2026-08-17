import React from 'react';
import { Award, AlertTriangle, XCircle } from 'lucide-react';

export const ProbabilityScore = ({ probability, status }) => {
  const getColors = () => {
    if (status === 'ACCEPTED') {
      return { text: '#34D399', stroke: '#10B981', bg: 'rgba(16, 185, 129, 0.15)', icon: Award, label: 'High Eligibility' };
    } else if (status === 'FLAGGED_FOR_REVIEW') {
      return { text: '#FBBF24', stroke: '#F59E0B', bg: 'rgba(245, 158, 11, 0.15)', icon: AlertTriangle, label: 'Moderate Risk' };
    } else {
      return { text: '#F87171', stroke: '#EF4444', bg: 'rgba(239, 68, 68, 0.15)', icon: XCircle, label: 'Rejection Risk' };
    }
  };

  const { text, stroke, bg, icon: Icon, label } = getColors();
  const radius = 54;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (probability / 100) * circumference;

  return (
    <div className="glass-panel" style={{ padding: '24px', display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', background: bg }}>
      <h3 style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '16px' }}>
        Verification Probability
      </h3>

      <div style={{ position: 'relative', width: '140px', height: '140px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <svg width="140" height="140" style={{ transform: 'rotate(-90deg)' }}>
          <circle
            cx="70"
            cy="70"
            r={radius}
            stroke="rgba(255, 255, 255, 0.1)"
            strokeWidth="10"
            fill="transparent"
          />
          <circle
            cx="70"
            cy="70"
            r={radius}
            stroke={stroke}
            strokeWidth="10"
            fill="transparent"
            strokeDasharray={circumference}
            strokeDashoffset={strokeDashoffset}
            strokeLinecap="round"
            style={{ transition: 'stroke-dashoffset 1s ease-in-out' }}
          />
        </svg>

        <div style={{ position: 'absolute', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <span style={{ fontSize: '2rem', fontWeight: 800, color: text }}>{probability}%</span>
          <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)', textTransform: 'uppercase' }}>Probability</span>
        </div>
      </div>

      <div style={{ marginTop: '16px', display: 'flex', alignItems: 'center', gap: '6px', color: text, fontWeight: 600, fontSize: '0.95rem' }}>
        <Icon size={18} />
        <span>{label}</span>
      </div>
      
      <p style={{ marginTop: '8px', fontSize: '0.75rem', color: 'var(--text-muted)', maxWidth: '220px' }}>
        Probability = 100% - Max Similarity Score (Subject to Guideline Rule Enforcement).
      </p>
    </div>
  );
};
