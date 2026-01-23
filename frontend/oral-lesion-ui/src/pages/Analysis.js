import React, { useState } from "react";
import ImageUpload from "../components/ImageUpload";
import { predictLesion } from "../services/api";
import "./Analysis.css";

function Analysis() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const [showChecklist, setShowChecklist] = useState(false);
  const [formData, setFormData] = useState({
    imageMatchesLesion: false,
    imageQualityOk: false,
    historyReviewed: false,
    alignsWithDifferential: false,
    highRiskManaged: false,
    lowRiskFollowUpPlanned: false,
    documentationDone: false,
    noRedFlagsIgnored: false,
  });

  const handleImageSelect = async (file) => {
    setSelectedImage(file);
    setError(null);
    setPrediction(null);
    setShowChecklist(false); // reset checklist visibility when a new image is chosen
    setFormData({
      imageMatchesLesion: false,
      imageQualityOk: false,
      historyReviewed: false,
      alignsWithDifferential: false,
      highRiskManaged: false,
      lowRiskFollowUpPlanned: false,
      documentationDone: false,
      noRedFlagsIgnored: false,
    });

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

  const handleChecklistChange = (e) => {
    const { name, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: checked,
    }));
  };

  const handleChecklistSubmit = (e) => {
    e.preventDefault();
    // Replace this with a real logging / API call if needed.
    const completedCount = Object.values(formData).filter(Boolean).length;
    alert(
      `Verification checklist submitted.\nCompleted steps: ${completedCount}/8\n\nThank you for reviewing the AI result.`
    );
    setShowChecklist(false);
  };

  return (
    <div className="analysis-page">
      <div className="analysis-header fade-in">
        <h1>AI Lesion Analysis</h1>
        <p>Upload an oral cavity image for instant AI analysis.</p>
      </div>

      <div className="analysis-container">
        <section className="content-section slide-in-left">
          <ImageUpload onImageSelect={handleImageSelect} />

          {/* Verify button - ALWAYS VISIBLE */}
          <div className="verify-section">
            <button
              type="button"
              className="btn-primary-large"
              onClick={() => setShowChecklist((prev) => !prev)}
            >
              {showChecklist ? "Close Verification Checklist" : "Verify AI Result"}
            </button>
          </div>

          {/* Checklist form - ALWAYS AVAILABLE */}
          {showChecklist && (
            <form className="verification-form" onSubmit={handleChecklistSubmit}>
              <h3>AI Result Verification Checklist</h3>
              <p>
                Tick each step once completed before relying on the AI result for clinical
                decision-making.
              </p>

              <div className="verification-grid">
                <label className="verification-item">
                  <input
                    type="checkbox"
                    name="imageMatchesLesion"
                    checked={formData.imageMatchesLesion}
                    onChange={handleChecklistChange}
                  />
                  <span>
                    The clinical image corresponds to the lesion examined (site, size, appearance).
                  </span>
                </label>

                <label className="verification-item">
                  <input
                    type="checkbox"
                    name="imageQualityOk"
                    checked={formData.imageQualityOk}
                    onChange={handleChecklistChange}
                  />
                  <span>
                    Image quality is adequate (focus, lighting, framing, no major artifacts).
                  </span>
                </label>

                <label className="verification-item">
                  <input
                    type="checkbox"
                    name="historyReviewed"
                    checked={formData.historyReviewed}
                    onChange={handleChecklistChange}
                  />
                  <span>
                    Patient history and risk factors (tobacco, alcohol, HPV, prior lesions) have
                    been reviewed.
                  </span>
                </label>

                <label className="verification-item">
                  <input
                    type="checkbox"
                    name="alignsWithDifferential"
                    checked={formData.alignsWithDifferential}
                    onChange={handleChecklistChange}
                  />
                  <span>
                    The AI prediction is consistent with your differential diagnosis.
                  </span>
                </label>

                <label className="verification-item">
                  <input
                    type="checkbox"
                    name="highRiskManaged"
                    checked={formData.highRiskManaged}
                    onChange={handleChecklistChange}
                  />
                  <span>
                    For high-risk / suspicious predictions, appropriate steps (biopsy or specialist
                    referral) are planned.
                  </span>
                </label>

                <label className="verification-item">
                  <input
                    type="checkbox"
                    name="lowRiskFollowUpPlanned"
                    checked={formData.lowRiskFollowUpPlanned}
                    onChange={handleChecklistChange}
                  />
                  <span>
                    For low-risk predictions, follow-up schedule and patient counselling are
                    documented.
                  </span>
                </label>

                <label className="verification-item">
                  <input
                    type="checkbox"
                    name="documentationDone"
                    checked={formData.documentationDone}
                    onChange={handleChecklistChange}
                  />
                  <span>
                    AI output and your clinical interpretation are documented in the patient record.
                  </span>
                </label>

                <label className="verification-item">
                  <input
                    type="checkbox"
                    name="noRedFlagsIgnored"
                    checked={formData.noRedFlagsIgnored}
                    onChange={handleChecklistChange}
                  />
                  <span>
                    No alarming clinical signs are being ignored solely because the AI suggests low
                    risk.
                  </span>
                </label>
              </div>

              <button type="submit" className="btn-primary-large verify-submit-button">
                Submit Verification
              </button>
            </form>
          )}

          {loading && (
            <div className="loading-box">
              <h3>Analyzing image with AI...</h3>
              <p>This may take a few seconds.</p>
            </div>
          )}

          {error && <div className="error-box">{error}</div>}

          {prediction && (
            <div className="results-section slide-in-right">
              <h2>Analysis Result</h2>
              <div className="prediction-summary">
                <p>
                  Predicted Class:{" "}
                  <strong>{prediction.prediction || "N/A"}</strong>
                </p>
                {prediction.confidence != null && (
                  <p>
                    Confidence:{" "}
                    <strong>{(prediction.confidence * 100).toFixed(2)}%</strong>
                  </p>
                )}
                {prediction.raw_score != null && (
                  <p>
                    Model Output Score:{" "}
                    <strong>{prediction.raw_score.toFixed(4)}</strong>
                  </p>
                )}
                <p className="model-note">
                  Binary classification model trained on oral lesion images. Score &gt; 0.5 typically
                  indicates a higher likelihood of malignancy; always interpret in clinical context.
                </p>
              </div>
            </div>
          )}
        </section>
      </div>
    </div>
  );
}

export default Analysis;
