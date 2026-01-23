import React from "react";
import { Link } from "react-router-dom";
import "./Classifications.css";

function Classifications() {
  const classifications = [
    {
      id: 1,
      name: "Benign",
      icon: "✅",
      description: "Non-cancerous oral lesions and normal tissue",
      characteristics: [
        "No malignant characteristics present",
        "May include normal tissue variations",
        "Could be non-cancerous abnormalities",
        "Generally lower health risk"
      ],
      examples: [
        "Normal healthy tissue",
        "Benign ulcers",
        "Non-cancerous growths",
        "Inflammatory conditions"
      ],
      risk: "Low",
      color: "#10b981",
      action: "Regular monitoring and routine dental checkups recommended"
    },
    {
      id: 2,
      name: "Malignant",
      icon: "⚠️",
      description: "Cancerous lesions requiring immediate medical attention",
      characteristics: [
        "Shows characteristics of cancer",
        "May include oral squamous cell carcinoma",
        "Potentially aggressive growth patterns",
        "Requires urgent intervention"
      ],
      examples: [
        "Oral squamous cell carcinoma",
        "Advanced pre-cancerous lesions",
        "Cancerous growths",
        "High-risk lesions"
      ],
      risk: "Very High",
      color: "#ef4444",
      action: "URGENT: Immediate medical attention and biopsy required"
    }
  ];

  return (
    <div className="classifications-page">
      <div className="classifications-header fade-in">
        <h1>📚 Binary Classification Guide</h1>
        <p>Understanding our AI model's classification system</p>
        <div className="model-badge">
          <span>🤖 Binary Classification Model</span>
        </div>
      </div>

      <div className="info-section fade-in">
        <h2>About Our AI Model</h2>
        <p>
          Our system uses a trained deep learning model that performs <strong>binary classification</strong> 
          of oral cavity images. This means the AI classifies images into one of two categories: 
          <strong> Benign</strong> (non-cancerous) or <strong>Malignant</strong> (cancerous).
        </p>
      </div>

      <div className="classifications-container">
        {classifications.map((item, index) => (
          <div 
            key={item.id} 
            className={`classification-card ${index % 2 === 0 ? 'slide-in-left' : 'slide-in-right'}`}
            style={{ borderLeft: `5px solid ${item.color}` }}
          >
            <div className="card-header">
              <span className="card-icon" style={{ fontSize: '4rem' }}>{item.icon}</span>
              <h2 style={{ color: item.color }}>{item.name}</h2>
              <span 
                className={`risk-badge risk-${item.risk.toLowerCase().replace(' ', '-')}`}
                style={{ background: item.color, color: 'white' }}
              >
                {item.risk} Risk
              </span>
            </div>

            <p className="description">{item.description}</p>

            <div className="characteristics">
              <h3>Key Characteristics:</h3>
              <ul>
                {item.characteristics.map((char, idx) => (
                  <li key={idx}>{char}</li>
                ))}
              </ul>
            </div>

            <div className="characteristics">
              <h3>May Include:</h3>
              <ul>
                {item.examples.map((example, idx) => (
                  <li key={idx}>{example}</li>
                ))}
              </ul>
            </div>

            <div className="action-box" style={{ borderLeft: `4px solid ${item.color}` }}>
              <strong>Recommended Action:</strong>
              <p>{item.action}</p>
            </div>
          </div>
        ))}
      </div>

      <div className="limitation-section">
        <h2>⚠️ Model Limitations</h2>
        <div className="limitations-grid">
          <div className="limitation-card">
            <h3>🎯 Binary Only</h3>
            <p>The model classifies lesions as either Benign or Malignant. It does not provide specific lesion types (e.g., leukoplakia, erythroplakia, specific tumor types).</p>
          </div>
          <div className="limitation-card">
            <h3>🔬 Not a Diagnosis</h3>
            <p>The AI prediction is NOT a medical diagnosis. Biopsy and histopathological examination remain the gold standard for definitive diagnosis.</p>
          </div>
          <div className="limitation-card">
            <h3>👨‍⚕️ Professional Review Required</h3>
            <p>All results should be reviewed by qualified healthcare professionals. Never make treatment decisions based solely on AI predictions.</p>
          </div>
          <div className="limitation-card">
            <h3>📊 Training Data Dependent</h3>
            <p>Model accuracy depends on the quality and diversity of training data. Performance may vary with different image qualities and patient populations.</p>
          </div>
        </div>
      </div>

      <div className="cta-section">
        <h2>Ready to Test the AI?</h2>
        <p>Upload an oral cavity image for instant binary classification</p>
        <Link to="/analysis" className="btn btn-primary">
          Start Analysis →
        </Link>
      </div>

      <div className="medical-note">
        <p>
          <strong>Medical Disclaimer:</strong> This binary classification tool is for educational and research 
          purposes only. It is not FDA-approved and should not be used as the sole basis for medical decisions. 
          Always consult with a qualified healthcare professional for proper diagnosis and treatment. 
          Pre-cancerous lesions (like leukoplakia or erythroplakia) may be classified as either benign or 
          malignant depending on their characteristics.
        </p>
      </div>
    </div>
  );
}

export default Classifications;

