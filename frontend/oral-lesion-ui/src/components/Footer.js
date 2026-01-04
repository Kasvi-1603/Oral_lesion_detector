import React from "react";
import "./Footer.css";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-section">
          <h3>🦷 Oral Lesion Classifier</h3>
          <p>AI-powered oral health analysis for early detection</p>
        </div>
        <div className="footer-section">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/analysis">Analysis</a></li>
            <li><a href="/about">About</a></li>
          </ul>
        </div>
        <div className="footer-section">
          <h4>Important Notice</h4>
          <p className="disclaimer">
            For educational and research purposes only.
            Not a substitute for professional medical diagnosis.
          </p>
        </div>
      </div>
      <div className="footer-bottom">
        <p>&copy; 2026 Oral Lesion Classifier. All rights reserved.</p>
      </div>
    </footer>
  );
}

export default Footer;


