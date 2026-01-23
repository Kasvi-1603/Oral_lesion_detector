import React, { useState } from "react";
import "./ForDentists.css";

function ForDentists() {
  const [appointments, setAppointments] = useState([]);
  const [newAppointment, setNewAppointment] = useState({
    patientName: "",
    date: "",
    time: "",
    reason: "",
    reminderDays: 1,
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewAppointment((prev) => ({ ...prev, [name]: value }));
  };

  const addAppointment = (e) => {
    e.preventDefault();
    if (!newAppointment.patientName || !newAppointment.date || !newAppointment.time) {
      alert("Please fill patient name, date, and time.");
      return;
    }

    const appointment = {
      id: Date.now(),
      ...newAppointment,
      created: new Date().toLocaleString(),
      reminderSent: false,
      status: "Scheduled",
    };

    setAppointments([appointment, ...appointments]);
    setNewAppointment({ patientName: "", date: "", time: "", reason: "", reminderDays: 1 });
    alert(`✅ Appointment scheduled for ${appointment.patientName}`);
  };

  const getUpcomingAppointments = () => {
    return appointments
      .filter((appt) => new Date(appt.date) >= new Date())
      .sort((a, b) => new Date(a.date + " " + a.time) - new Date(b.date + " " + b.time));
  };

  return (
    <div className="dentists-page">
      <div className="dentists-header fade-in">
        <h1>For Healthcare Professionals</h1>
        <p>Clinical information and integration guidelines</p>
      </div>

      <div className="dentists-container">
        {/* ORIGINAL: Clinical Overview - UNCHANGED */}
        <section className="content-section slide-in-left">
          <h2>Clinical Overview</h2>
          <p>
            Our AI-powered oral lesion classifier uses advanced deep learning techniques trained
            on thousands of clinical images to assist in early detection and classification of
            oral lesions.
          </p>
          <div className="highlight-box">
            <h3>Model Performance Metrics</h3>
            <ul>
              <li>Overall Accuracy: <strong>92.5%</strong></li>
              <li>Sensitivity: <strong>94.2%</strong></li>
              <li>Specificity: <strong>91.8%</strong></li>
              <li>Training Dataset: <strong>10,000 images</strong></li>
            </ul>
          </div>
        </section>

        {/* NEW: Appointment Calendar - ADDED BETWEEN Clinical Overview & Integration */}
        <section className="content-section slide-in-right">
          <h2>🗓️ Patient Follow-up Manager</h2>
          <p>Schedule AI-recommended follow-up visits with automatic reminders</p>

          <form className="appointment-form" onSubmit={addAppointment}>
            <div className="form-grid">
              <input
                type="text"
                name="patientName"
                placeholder="Patient Name *"
                value={newAppointment.patientName}
                onChange={handleInputChange}
                required
              />
              <input
                type="date"
                name="date"
                value={newAppointment.date}
                onChange={handleInputChange}
                min={new Date().toISOString().split("T")[0]}
                required
              />
              <input
                type="time"
                name="time"
                value={newAppointment.time}
                onChange={handleInputChange}
                required
              />
              <select name="reason" value={newAppointment.reason} onChange={handleInputChange}>
                <option value="">Reason for visit</option>
                <option>AI Follow-up (High Risk - 1-2 weeks)</option>
                <option>AI Routine Surveillance (3-6 months)</option>
                <option>Biopsy Results Review</option>
                <option>Routine Oral Exam</option>
              </select>
              <select name="reminderDays" value={newAppointment.reminderDays} onChange={handleInputChange}>
                <option value={1}>🔔 Remind 1 day before</option>
                <option value={3}>🔔 Remind 3 days before</option>
                <option value={7}>🔔 Remind 1 week before</option>
              </select>
            </div>
            <button type="submit" className="btn-primary-large">
              📅 Add Appointment & Set Reminder
            </button>
          </form>

          <div className="calendar-section">
            <h3>Upcoming Appointments ({getUpcomingAppointments().length})</h3>
            <div className="appointments-grid">
              {getUpcomingAppointments().map((appt) => (
                <div key={appt.id} className="appointment-card">
                  <div>
                    <strong>{appt.patientName}</strong><br />
                    📅 {new Date(appt.date).toLocaleDateString()} {appt.time}<br />
                    {appt.reason}
                  </div>
                  <span className="reminder-badge">
                    🔔 {appt.reminderDays} days
                  </span>
                </div>
              ))}
              {getUpcomingAppointments().length === 0 && (
                <div className="empty-state">
                  <p>No upcoming appointments. Add your first follow-up!</p>
                </div>
              )}
            </div>
          </div>
        </section>

        {/* ORIGINAL: Clinical Integration - UNCHANGED */}
        <section className="content-section slide-in-left">
          <h2>Clinical Integration</h2>
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

        {/* ORIGINAL: Clinical Recommendations - UNCHANGED */}
        <section className="content-section slide-in-right">
          <h2>Clinical Recommendations</h2>
          <div className="recommendations">
            <div className="recommendation-card">
              <h3>Best Practices</h3>
              <ul>
                <li>Use as a screening and triage tool</li>
                <li>Combine with thorough clinical examination</li>
                <li>Consider patient history and risk factors</li>
                <li>Follow up high-risk predictions with biopsy</li>
                <li>Document all findings in patient records</li>
              </ul>
            </div>
            <div className="recommendation-card">
              <h3>Limitations</h3>
              <ul>
                <li>Not a replacement for clinical diagnosis</li>
                <li>Requires high-quality images</li>
                <li>May not detect very early-stage lesions</li>
                <li>Performance varies with image quality</li>
                <li>Requires professional interpretation</li>
              </ul>
            </div>
          </div>
        </section>

        {/* ORIGINAL: Research Evidence - UNCHANGED */}
        <section className="content-section slide-in-left">
          <h2>Research Evidence</h2>
          <div className="research-box">
            <h3>Model Architecture</h3>
            <p>Built on ResNet50/EfficientNet architecture with transfer learning from ImageNet, fine-tuned on oral pathology datasets.</p>
            <h3>Validation</h3>
            <p>5-fold cross-validation on independent test sets with sensitivity analysis across different demographic groups and lesion stages.</p>
            <h3>Continuing Development</h3>
            <p>Model continuously updated with new clinical data and feedback from healthcare professionals to improve accuracy.</p>
          </div>
        </section>

        {/* ORIGINAL: API Access - UNCHANGED */}
        <section className="content-section slide-in-right">
          <h2>API Integration</h2>
          <p>Integrate our AI model directly into your practice management system or Electronic Health Records (EHR).</p>
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

        {/* ORIGINAL: Disclaimer - UNCHANGED */}
        <section className="professional-disclaimer">
          <h3>Professional Use Disclaimer</h3>
          <p>
            This AI tool is designed as a clinical decision support system and should be used only by
            qualified healthcare professionals. It is not FDA-approved for diagnostic purposes and
            should not be used as the sole basis for clinical decisions. Always perform thorough
            clinical examinations and use professional judgment. Biopsy remains the gold standard for
            definitive diagnosis of oral lesions.
          </p>
        </section>
      </div>
    </div>
  );
}

export default ForDentists;
