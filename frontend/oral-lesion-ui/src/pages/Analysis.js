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
              <h2>📊 Prediction Results</h2>
              <div className="prediction-card">
                <div className="main-prediction">
                  <h3>{prediction.prediction}</h3>
                  <p className="confidence">
                    Confidence: {(prediction.confidence * 100).toFixed(2)}%
                  </p>
                </div>

                <div className="confidence-bar">
                  <div
                    className="confidence-fill"
                    style={{ width: `${prediction.confidence * 100}%` }}
                  ></div>
                </div>

                <h4>All Class Probabilities:</h4>
                <div className="probabilities">
                  {Object.entries(prediction.probabilities).map(([className, prob]) => (
                    <div key={className} className="prob-item">
                      <span className="class-name">{className}</span>
                      <span className="prob-value">{(prob * 100).toFixed(2)}%</span>
                      <div className="prob-bar">
                        <div
                          className="prob-fill"
                          style={{ width: `${prob * 100}%` }}
                        ></div>
                      </div>
                    </div>
                  ))}
                </div>
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

