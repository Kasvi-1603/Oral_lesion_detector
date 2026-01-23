import React from "react";
import "./About.css";

function About() {
  return (
    <div className="about-page">
      <div className="about-header fade-in">
        <h1>About This Project</h1>
        <p>AI-powered oral lesion detection - College Project</p>
      </div>

      <div className="about-container">
        <section className="about-section slide-in-left">
          <h2>📋 Project Report</h2>
          <p>
            This project demonstrates the application of deep learning and computer vision
            techniques for binary classification of oral lesions. The system classifies
            oral cavity images as either <strong>Benign</strong> (non-cancerous) or 
            <strong>Malignant</strong> (cancerous) using a trained TensorFlow model.
          </p>
        </section>

        <section className="about-section slide-in-right">
          <h2>🔬 Technology Stack</h2>
          <div className="tech-stack">
            <div className="tech-item">
              <h3>Backend</h3>
              <p>FastAPI, TensorFlow, Python</p>
            </div>
            <div className="tech-item">
              <h3>Frontend</h3>
              <p>React, Modern CSS</p>
            </div>
            <div className="tech-item">
              <h3>AI Model</h3>
              <p>Binary CNN Classifier</p>
            </div>
          </div>
        </section>

        <section className="about-section slide-in-left">
          <h2>🎯 Project Objectives</h2>
          <div className="objectives-list">
            <div className="objective-item">
              <span className="objective-icon">✅</span>
              <p>Implement a full-stack ML application with FastAPI and React</p>
            </div>
            <div className="objective-item">
              <span className="objective-icon">✅</span>
              <p>Integrate a trained deep learning model for image classification</p>
            </div>
            <div className="objective-item">
              <span className="objective-icon">✅</span>
              <p>Create a professional user interface for medical image analysis</p>
            </div>
            <div className="objective-item">
              <span className="objective-icon">✅</span>
              <p>Demonstrate REST API design and frontend-backend integration</p>
            </div>
          </div>
        </section>

        <section className="about-section slide-in-right">
          <h2>📚 Key Features</h2>
          <ul className="features-list">
            <li>Real-time binary classification of oral lesion images</li>
            <li>RESTful API with FastAPI framework</li>
            <li>Multi-page React application with routing</li>
            <li>Image preprocessing pipeline</li>
            <li>Confidence score visualization</li>
            <li>Responsive and modern UI design</li>
          </ul>
        </section>

        <section className="about-section slide-in-left">
          <h2>🎓 Academic Purpose</h2>
          <p>
            This project was developed as part of an academic initiative to explore
            the application of deep learning in medical imaging. It demonstrates the potential
            of AI to assist in early detection of oral pathologies while highlighting the
            importance of professional medical oversight.
          </p>
        </section>

        <section className="disclaimer-section">
          <h2>⚠️ Important Notice</h2>
          <p>
            This tool is designed for <strong>educational and research purposes only</strong>. 
            It is not FDA-approved and should not be used as the sole basis for medical decisions.
            Always consult with qualified healthcare professionals for proper diagnosis
            and treatment of oral lesions.
          </p>
        </section>
      </div>
    </div>
  );
}

export default About;

