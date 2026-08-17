import React, { useState } from 'react';
import { useTitleCheck } from '../hooks/useTitleCheck';
import { TitleInput } from '../components/title-check/TitleInput';
import { CheckButton } from '../components/title-check/CheckButton';
import { SimilarityResult } from '../components/title-check/SimilarityResult';
import { ProbabilityScore } from '../components/title-check/ProbabilityScore';
import { MatchingTitles } from '../components/title-check/MatchingTitles';
import { GuidelineResult } from '../components/title-check/GuidelineResult';
import { Loading } from '../components/common/Loading';
import { ErrorMessage } from '../components/common/ErrorMessage';
import { RefreshCw, Sparkles } from 'lucide-react';

export const TitleCheck = ({ onSubmissionCreated }) => {
  const [title, setTitle] = useState('');
  const { loading, result, error, checkTitle, resetResult } = useTitleCheck();

  const handleVerify = async () => {
    if (title.trim()) {
      const data = await checkTitle(title.trim());
      if (data && onSubmissionCreated) {
        onSubmissionCreated(data);
      }
    }
  };

  const handleTestSample = async (sampleTitle) => {
    setTitle(sampleTitle);
    const data = await checkTitle(sampleTitle);
    if (data && onSubmissionCreated) {
      onSubmissionCreated(data);
    }
  };

  const sampleTitles = [
    { label: "Spelling Modification", title: "Namascar" },
    { label: "Prohibited Word", title: "Police News" },
    { label: "Combined Titles", title: "Hindu Indian Express" },
    { label: "Periodicity Addition", title: "Daily Times of India" },
    { label: "Multilingual Meaning", title: "Pratidin Sandhya" },
    { label: "Eligible Unique Title", title: "Apex Horizon Herald" }
  ];

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '32px' }}>
      {/* Title Input Card */}
      <div className="glass-panel" style={{ padding: '32px' }}>
        <div style={{ marginBottom: '24px' }}>
          <h2 style={{ fontSize: '1.8rem', color: '#FFF', fontWeight: 700 }}>Title Verification Portal</h2>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem', marginTop: '4px' }}>
            Submit a proposed publication title to check uniqueness against ~160,000 PRGI registered titles and verify official guideline compliance.
          </p>
        </div>

        <div style={{ display: 'flex', gap: '16px', flexWrap: 'wrap' }}>
          <div style={{ flexGrow: 1, minWidth: '300px' }}>
            <TitleInput
              value={title}
              onChange={setTitle}
              onSubmit={handleVerify}
              disabled={loading}
            />
          </div>
          <CheckButton
            onClick={handleVerify}
            loading={loading}
            disabled={!title.trim()}
          />
        </div>

        {/* Quick Test Samples */}
        <div style={{ marginTop: '24px', paddingTop: '20px', borderTop: '1px solid var(--border-color)' }}>
          <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '12px' }}>
            <Sparkles size={14} color="var(--accent-amber)" /> Test System Rule Verification Samples:
          </span>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
            {sampleTitles.map((sample, i) => (
              <button
                key={i}
                onClick={() => handleTestSample(sample.title)}
                disabled={loading}
                style={{
                  background: 'rgba(31, 41, 55, 0.6)',
                  border: '1px solid var(--border-color)',
                  color: 'var(--text-secondary)',
                  padding: '6px 14px',
                  borderRadius: '9999px',
                  fontSize: '0.8rem',
                  cursor: 'pointer',
                  transition: 'all 0.2s ease'
                }}
              >
                <strong style={{ color: '#FFF' }}>{sample.title}</strong> ({sample.label})
              </button>
            ))}
          </div>
        </div>
      </div>

      <ErrorMessage message={error} />

      {loading && <Loading />}

      {/* Verification Result Breakdown */}
      {result && !loading && (
        <div className="animate-fade-in" style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 300px', gap: '24px' }}>
            <SimilarityResult
              title={result.submitted_title}
              normalizedTitle={result.normalized_title}
              highestSimilarity={result.highest_similarity}
              status={result.status}
              summary={result.rejection_summary}
            />
            <ProbabilityScore
              probability={result.verification_probability}
              status={result.status}
            />
          </div>

          <GuidelineResult violations={result.guideline_violations} />

          <MatchingTitles matches={result.matched_titles} />

          <div style={{ display: 'flex', justifyContent: 'center', marginTop: '16px' }}>
            <button
              className="btn-primary"
              onClick={() => {
                resetResult();
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              style={{ background: 'var(--grad-primary)' }}
            >
              <RefreshCw size={18} /> Modify Title & Resubmit
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
