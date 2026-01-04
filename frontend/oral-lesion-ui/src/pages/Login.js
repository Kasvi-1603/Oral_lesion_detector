import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css";

function Login() {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    // TODO: Implement actual authentication
    alert(isLogin ? "Login successful!" : "Registration successful!");
    navigate("/analysis");
  };

  return (
    <div className="login-page">
      <div className="login-container fade-in">
        <div className="login-header">
          <h1>🦷 {isLogin ? "Welcome Back" : "Create Account"}</h1>
          <p>{isLogin ? "Sign in to continue" : "Join us today"}</p>
        </div>

        <form className="login-form" onSubmit={handleSubmit}>
          {!isLogin && (
            <div className="form-group">
              <label>Full Name</label>
              <input
                type="text"
                placeholder="Enter your name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required={!isLogin}
              />
            </div>
          )}

          <div className="form-group">
            <label>Email Address</label>
            <input
              type="email"
              placeholder="your.email@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          {isLogin && (
            <div className="form-options">
              <label className="checkbox-label">
                <input type="checkbox" />
                Remember me
              </label>
              <a href="#forgot" className="forgot-link">
                Forgot password?
              </a>
            </div>
          )}

          <button type="submit" className="btn-submit">
            {isLogin ? "Sign In" : "Create Account"}
          </button>
        </form>

        <div className="form-footer">
          <p>
            {isLogin ? "Don't have an account?" : "Already have an account?"}{" "}
            <button
              className="toggle-btn"
              onClick={() => setIsLogin(!isLogin)}
            >
              {isLogin ? "Sign Up" : "Sign In"}
            </button>
          </p>
        </div>

        <div className="social-login">
          <div className="divider">
            <span>or continue with</span>
          </div>
          <div className="social-buttons">
            <button className="social-btn">
              <span>🔵</span> Facebook
            </button>
            <button className="social-btn">
              <span>🔴</span> Google
            </button>
          </div>
        </div>

        <div className="professional-note">
          <p>
            <strong>Healthcare Professionals:</strong> Please contact us for
            institutional access and API integration.
          </p>
        </div>
      </div>
    </div>
  );
}

export default Login;

