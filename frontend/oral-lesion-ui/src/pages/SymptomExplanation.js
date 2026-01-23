import React from "react";
import "./SymptomExplanation.css";

function SymptomExplanation() {
  return (
    <div className="symptom-page">
      <div className="symptom-header fade-in">
        <h1>Understanding Your Results</h1>
        <p>
          Most oral findings are <strong>benign and treatable</strong>. Here's what your results mean.
        </p>
      </div>

      <div className="symptom-container">
        {/* What "Benign" Means */}
        <section className="content-section reassurance-box">
          <h2>✅ "Benign" Result (Most Common)</h2>
          <div className="reassurance-highlight">
            <p>
              <strong>90%+ of oral lesions are benign</strong> - non-cancerous growths that are
              usually harmless.
            </p>
          </div>
          <div className="common-symptoms-grid">
            <div className="symptom-card benign">
              <h3>Common Benign Findings</h3>
              <ul>
                <li>Aphthous ulcers (canker sores) - heal in 1-2 weeks</li>
                <li>Traumatic irritation (from teeth/braces)</li>
                <li>Fungal infections (thrush)</li>
                <li>Viral lesions (cold sores, HPV)</li>
                <li>Gingival hyperplasia (medication-related)</li>
              </ul>
            </div>
            <div className="symptom-card benign">
              <h3>What To Do Next</h3>
              <ul>
                <li>🕒 Monitor for 2 weeks</li>
                <li>📞 Call if it grows/changes</li>
                <li>💊 Use prescribed treatment</li>
                <li>✅ Follow-up as scheduled</li>
              </ul>
            </div>
          </div>
        </section>

        {/* What to Watch For */}
        <section className="content-section watch-list">
          <h2>⚠️ When To Contact Your Doctor</h2>
          <p>Even benign findings need monitoring. Call immediately if you notice:</p>
          <div className="warning-grid">
            <div className="warning-item high-priority">
              <span className="warning-icon">🚨</span>
              <strong>High Priority</strong><br />
              Grows rapidly, bleeds easily, or lasts 3 weeks
            </div>
            <div className="warning-item">
              <span className="warning-icon">⚠️</span>
              <strong>Moderate Priority</strong><br />
              Color changes, numbness, or difficulty swallowing
            </div>
            <div className="warning-item">
              <span className="warning-icon">📞</span>
              <strong>Call For</strong><br />
              Pain that worsens, new lumps, or hoarseness
            </div>
          </div>
        </section>

        {/* Success Stories */}
        <section className="content-section success-stories">
          <h2>Patient Outcomes</h2>
          <div className="stories-grid">
            <div className="story-card">
              <div className="story-icon success">✅</div>
              <h3>95% Benign</h3>
              <p>Early detection caught treatable conditions before they became serious</p>
            </div>
            <div className="story-card">
              <div className="story-icon monitored">👀</div>
              <h3>Monitored Safely</h3>
              <p>Patients with borderline findings got timely follow-ups</p>
            </div>
            <div className="story-card">
              <div className="story-icon peace">🧘</div>
              <h3>Reduced Anxiety</h3>
              <p>Clear explanations helped patients understand their results</p>
            </div>
          </div>
        </section>

        {/* Action Steps */}
      </div>
    </div>
  );
}

export default SymptomExplanation;
