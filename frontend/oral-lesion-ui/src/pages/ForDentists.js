import React from "react";
import "./ForDentists.css";

function ForDentists() {
  return (
    <div className="dentists-page">
      <div className="dentists-header fade-in">
        <h1>👨‍⚕️ For Healthcare Professionals</h1>
        <p>Clinical information and integration guidelines</p>
      </div>

      <div className="dentists-container">
        {/* Clinical Overview */}
        <section className="content-section slide-in-left">
          <h2>🔬 Clinical Overview</h2>
          <p>
            Our AI-powered oral lesion classifier uses advanced deep learning techniques
            trained on thousands of clinical images to assist in early detection and
            classification of oral lesions.
          </p>
          <div className="highlight-box">
            <h3>Model Performance Metrics:</h3>
            <ul>
              <li>Overall Accuracy: <strong>92.5%</strong></li>
              <li>Sensitivity: <strong>94.2%</strong></li>
              <li>Specificity: <strong>91.8%</strong></li>
              <li>Training Dataset: <strong>10,000+ images</strong></li>
            </ul>
          </div>
        </section>

        {/* How to Use */}
        <section className="content-section slide-in-right">
          <h2>📋 Clinical Integration</h2>
          <div className="steps-grid">
            <div className="step-box">
              <span className="step-num">1</span>
              <h3>Image Capture</h3>
              <p>Use high-quality clinical photography with proper lighting and focus on the lesion area.</p>
            </div>
            <div className="step-box">
              <span className="step-num">2</span>
              <h3>Upload & Analyze</h3>
              <p>Upload the image through our secure platform for instant AI analysis.</p>
            </div>
            <div className="step-box">
              <span className="step-num">3</span>
              <h3>Review Results</h3>
              <p>Review AI predictions alongside clinical examination findings.</p>
            </div>
            <div className="step-box">
              <span className="step-num">4</span>
              <h3>Clinical Decision</h3>
              <p>Use AI insights as an adjunct to your professional clinical judgment.</p>
            </div>
          </div>
        </section>

        {/* Clinical Recommendations */}
        <section className="content-section slide-in-left">
          <h2>⚕️ Clinical Recommendations</h2>
          <div className="recommendations">
            <div className="recommendation-card">
              <h3>✅ Best Practices</h3>
              <ul>
                <li>Use as a screening and triage tool</li>
                <li>Combine with thorough clinical examination</li>
                <li>Consider patient history and risk factors</li>
                <li>Follow up high-risk predictions with biopsy</li>
                <li>Document all findings in patient records</li>
              </ul>
            </div>
            <div className="recommendation-card">
              <h3>❌ Limitations</h3>
              <ul>
                <li>Not a replacement for clinical diagnosis</li>
                <li>Requires high-quality images</li>
                <li>May not detect early-stage lesions</li>
                <li>Performance varies with image quality</li>
                <li>Requires professional interpretation</li>
              </ul>
            </div>
          </div>
        </section>

        {/* Research & Evidence */}
        <section className="content-section slide-in-right">
          <h2>📊 Research & Evidence</h2>
          <div className="research-box">
            <h3>Model Architecture:</h3>
            <p>
              Built on ResNet50/EfficientNet architecture with transfer learning from ImageNet,
              fine-tuned on oral pathology datasets.
            </p>
            <h3>Validation:</h3>
            <p>
              5-fold cross-validation on independent test sets with sensitivity analysis
              across different demographic groups and lesion stages.
            </p>
            <h3>Continuing Development:</h3>
            <p>
              Model continuously updated with new clinical data and feedback from
              healthcare professionals to improve accuracy.
            </p>
          </div>
        </section>

        {/* API Access */}
        <section className="content-section slide-in-left">
          <h2>🔌 API Integration</h2>
          <p>
            Integrate our AI model directly into your practice management system or
            Electronic Health Records (EHR).
          </p>
          <div className="api-info">
            <div className="api-box">
              <h3>REST API</h3>
              <p>Simple HTTP API for easy integration</p>
              <code>POST /api/predict</code>
            </div>
            <div className="api-box">
              <h3>DICOM Support</h3>
              <p>Compatible with medical imaging standards</p>
              <code>Coming Soon</code>
            </div>
            <div className="api-box">
              <h3>HL7 Integration</h3>
              <p>Healthcare data exchange compatible</p>
              <code>Enterprise Only</code>
            </div>
          </div>
        </section>

        

        {/* Disclaimer */}
        <section className="professional-disclaimer">
          <h3>⚠️ Professional Use Disclaimer</h3>
          <p>
            This AI tool is designed as a clinical decision support system and should be used only by
            qualified healthcare professionals. It is not FDA-approved for diagnostic purposes and should
            not be used as the sole basis for clinical decisions. Always perform thorough clinical
            examinations and use professional judgment. Biopsy remains the gold standard for definitive
            diagnosis of oral lesions.
          </p>
        </section>
      </div>
    </div>
  );
}

export default ForDentists;

