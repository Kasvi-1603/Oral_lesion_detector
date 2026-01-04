import React from "react";
import "./About.css";

function About() {
  return (
    <div className="about-page">
      <div className="about-header fade-in">
        <h1>About This Project</h1>
        <p>AI-powered oral lesion detection system</p>
      </div>

      <div className="about-container">
        {/* Project Overview */}
        <section className="about-section slide-in-left">
          <h2>📋 Project Overview</h2>
          <p>
            This is a full-stack machine learning application that performs binary classification
            of oral lesion images. The system uses a trained deep learning model to classify images
            as either <strong>Benign</strong> (non-cancerous) or <strong>Malignant</strong> (cancerous),
            demonstrating practical integration of AI models in web applications.
          </p>
        </section>

        {/* Technology Stack */}
        <section className="about-section slide-in-right">
          <h2>🔬 Technology Stack</h2>
          <div className="tech-stack">
            <div className="tech-item">
              <h3>Backend</h3>
              <p>FastAPI, TensorFlow, Python</p>
            </div>
            <div className="tech-item">
              <h3>Frontend</h3>
              <p>React, React Router, CSS</p>
            </div>
            <div className="tech-item">
              <h3>AI Model</h3>
              <p>Binary CNN Classifier</p>
            </div>
          </div>
        </section>

        {/* Project Objectives */}
        <section className="about-section slide-in-left">
          <h2>🎯 Project Objectives</h2>
          <div className="objectives-list">
            <div className="objective-item">
              <span className="objective-icon">✅</span>
              <p>Implement full-stack ML application with FastAPI and React</p>
            </div>
            <div className="objective-item">
              <span className="objective-icon">✅</span>
              <p>Integrate trained TensorFlow model for binary classification</p>
            </div>
            <div className="objective-item">
              <span className="objective-icon">✅</span>
              <p>Design responsive web interface for image analysis</p>
            </div>
            <div className="objective-item">
              <span className="objective-icon">✅</span>
              <p>Demonstrate REST API and frontend-backend integration</p>
            </div>
          </div>
        </section>

        {/* Future Scope */}
        <section className="about-section slide-in-right">
          <h2>🚀 Future Enhancements</h2>
          <ul className="features-list">
            <li>Multi-class classification for specific lesion types</li>
            <li>Model explainability with visualization techniques</li>
            <li>User authentication and prediction history</li>
            <li>Mobile application development</li>
            <li>Clinical validation and testing</li>
          </ul>
        </section>

        {/* Academic Purpose */}
        <section className="about-section slide-in-left">
          <h2>🎓 Academic Purpose</h2>
          <p>
            This project was developed as part of academic coursework to explore the application
            of deep learning in medical imaging. It demonstrates technical implementation concepts
            including machine learning model integration, API development, and modern web application
            architecture.
          </p>
        </section>

        {/* Disclaimer */}
        <section className="disclaimer-section">
          <h2>⚠️ Important Notice</h2>
          <p>
            This is an <strong>educational project</strong> developed for academic purposes only.
            The system is not FDA-approved or clinically validated. It should not be used for
            actual medical diagnosis. Always consult qualified healthcare professionals for
            medical advice and diagnosis.
          </p>
        </section>
      </div>
    </div>
  );
}

export default About;

