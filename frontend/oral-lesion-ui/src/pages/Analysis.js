import React, { useState } from "react";
import ImageUpload from "../components/ImageUpload";
import { predictLesion } from "../services/api";
import "./Analysis.css";

function Analysis() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleImageSelect = async (file) => {
    setSelectedImage(file);
    setError(null);
    setPrediction(null);
    setLoading(true);

    try {
      console.log("Sending file to backend:", file.name);
      const result = await predictLesion(file);
      console.log("Prediction result:", result);
      setPrediction(result);
    } catch (err) {
      console.error("Prediction error:", err);
      setError(err.message || "Failed to get prediction. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="analysis-page">
      <div className="analysis-container">
        <div className="analysis-header fade-in">
          <h1>🔬 AI-Powered Analysis</h1>
          <p>Upload an oral cavity image for instant AI analysis</p>
        </div>

        <div className="analysis-content">
          <ImageUpload onImageSelect={handleImageSelect} />

          {loading && (
            <div className="loading fade-in">
              <div className="spinner"></div>
              <p>Analyzing image with AI...</p>
              <p className="loading-subtext">This may take a few seconds</p>
            </div>
          )}

          {error && (
            <div className="error fade-in">
              <span className="error-icon">❌</span>
              <p>{error}</p>
            </div>
          )}

          {prediction && !loading && (
            <div className="results fade-in">
              <h2>📊 Analysis Results</h2>
              <div className={`prediction-card ${prediction.prediction === "Malignant" ? "malignant" : "benign"}`}>
                <div className="main-prediction">
                  <div className="prediction-badge">
                    {prediction.prediction === "Benign" ? "✓" : "⚠"}
                  </div>
                  <h3>{prediction.prediction}</h3>
                  <p className="confidence">
                    Confidence: {(prediction.confidence * 100).toFixed(2)}%
                  </p>
                </div>

                <div className="confidence-bar">
                  <div
                    className={`confidence-fill ${prediction.prediction === "Malignant" ? "malignant" : "benign"}`}
                    style={{ width: `${prediction.confidence * 100}%` }}
                  ></div>
                </div>

                <div className="binary-probabilities">
                  <div className="prob-card benign-card">
                    <div className="prob-header">
                      <span className="prob-icon">✓</span>
                      <span className="prob-label">Benign</span>
                    </div>
                    <div className="prob-percentage">
                      {(prediction.probabilities.Benign * 100).toFixed(2)}%
                    </div>
                    <div className="prob-bar-mini">
                      <div 
                        className="prob-fill-mini benign"
                        style={{ width: `${prediction.probabilities.Benign * 100}%` }}
                      ></div>
                    </div>
                  </div>

                  <div className="prob-card malignant-card">
                    <div className="prob-header">
                      <span className="prob-icon">⚠</span>
                      <span className="prob-label">Malignant</span>
                    </div>
                    <div className="prob-percentage">
                      {(prediction.probabilities.Malignant * 100).toFixed(2)}%
                    </div>
                    <div className="prob-bar-mini">
                      <div 
                        className="prob-fill-mini malignant"
                        style={{ width: `${prediction.probabilities.Malignant * 100}%` }}
                      ></div>
                    </div>
                  </div>
                </div>

                {prediction.raw_score !== undefined && (
                  <div className="technical-details">
                    <h4>Technical Details</h4>
                    <p>Model Output Score: {prediction.raw_score.toFixed(4)}</p>
                    <p className="tech-note">
                      Binary classification model trained on oral lesion images. 
                      Score &gt; 0.5 indicates malignant lesion.
                    </p>
                  </div>
                )}
              </div>

              <div className="disclaimer">
                ⚠️ <strong>Important:</strong> This tool is for educational and research
                purposes only and should not be used as a substitute for professional
                medical diagnosis. Please consult a healthcare professional for medical advice.
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Analysis;


