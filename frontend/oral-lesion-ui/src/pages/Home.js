import React from "react";
import { Link } from "react-router-dom";
import "./Home.css";

function Home() {
  return (
    <div className="home">
      {/* Hero Section */}
      <section className="hero">
        <div className="hero-content fade-in">
          <h1 className="hero-title">
            <span className="gradient-text">AI-Powered</span> Oral Lesion Detection
          </h1>
          <p className="hero-subtitle">
            Binary classification of oral lesions (Benign vs Malignant) using deep learning
          </p>
          <div className="hero-stats">
            <div className="stat">
              <span className="stat-icon">🤖</span>
              <strong>Binary Classification</strong>
            </div>
            <div className="stat">
              <span className="stat-icon">🔬</span>
              <strong>TensorFlow Model</strong>
            </div>
            <div className="stat">
              <span className="stat-icon">⚡</span>
              <strong>Real-Time Results</strong>
            </div>
          </div>
          <div className="hero-buttons">
            <Link to="/analysis" className="btn btn-primary">
              Start Analysis
            </Link>
            <Link to="/about" className="btn btn-secondary">
              Learn More
            </Link>
          </div>
        </div>
        <div className="hero-image slide-in-right">
          <div className="image-placeholder">
            <span className="hero-icon">🦷</span>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="features">
        <h2 className="section-title">Why Choose Our System?</h2>
        <div className="features-grid">
          <div className="feature-card slide-in-left">
            <div className="feature-icon">🔬</div>
            <h3>Binary Classification</h3>
            <p>AI model classifies lesions as Benign (non-cancerous) or Malignant (cancerous)</p>
          </div>
          <div className="feature-card fade-in">
            <div className="feature-icon">⚡</div>
            <h3>Fast & Accurate</h3>
            <p>Get real predictions in seconds with confidence scores from trained neural network</p>
          </div>
          <div className="feature-card slide-in-right">
            <div className="feature-icon">🔒</div>
            <h3>Secure & Private</h3>
            <p>Your medical images are processed securely and not stored permanently</p>
          </div>
          <div className="feature-card slide-in-left">
            <div className="feature-icon">📊</div>
            <h3>Confidence Scores</h3>
            <p>Clear probability breakdown for both Benign and Malignant classifications</p>
          </div>
          <div className="feature-card fade-in">
            <div className="feature-icon">🎯</div>
            <h3>TensorFlow Powered</h3>
            <p>Built on industry-standard TensorFlow deep learning framework</p>
          </div>
          <div className="feature-card slide-in-right">
            <div className="feature-icon">👨‍⚕️</div>
            <h3>Clinical Support</h3>
            <p>Designed to assist healthcare professionals in early screening</p>
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section className="how-it-works">
        <h2 className="section-title">How It Works</h2>
        <div className="steps">
          <div className="step">
            <div className="step-number">1</div>
            <h3>Upload Image</h3>
            <p>Upload a clear image of the oral cavity or lesion</p>
          </div>
          <div className="step-arrow">→</div>
          <div className="step">
            <div className="step-number">2</div>
            <h3>Binary Classification</h3>
            <p>AI model classifies as Benign or Malignant</p>
          </div>
          <div className="step-arrow">→</div>
          <div className="step">
            <div className="step-number">3</div>
            <h3>Get Results</h3>
            <p>Receive predictions with confidence scores</p>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="cta">
        <div className="cta-content">
          <h2>Ready to Start?</h2>
          <p>Upload an oral cavity image for instant binary classification (Benign vs Malignant)</p>
          <Link to="/analysis" className="btn btn-large">
            Try It Now →
          </Link>
        </div>
      </section>

      {/* Disclaimer Banner */}
      <section className="disclaimer-banner">
        <div className="disclaimer-content">
          <span className="warning-icon">⚠️</span>
          <p>
            <strong>Important:</strong> This tool is for educational and research purposes only. 
            It should not be used as a substitute for professional medical diagnosis. 
            Please consult a healthcare professional for medical advice.
          </p>
        </div>
      </section>
    </div>
  );
}

export default Home;

