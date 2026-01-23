import React from "react";
import { Link, useLocation } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  const location = useLocation();

  return (
    <nav className="navbar">
      <div className="nav-container">
        <Link to="/" className="nav-logo">
          Oral Lesion Classifier
        </Link>
        
        <ul className="nav-menu">
          <li>
            <Link 
              to="/" 
              className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}
            >
              Home
            </Link>
          </li>
          <li>
            <Link 
              to="/analysis" 
              className={`nav-link ${location.pathname === '/analysis' ? 'active' : ''}`}
            >
              Analysis
            </Link>
          </li>
          <li>
            <Link 
              to="/classifications" 
              className={`nav-link ${location.pathname === '/classifications' ? 'active' : ''}`}
            >
              Classifications
            </Link>
          </li>
          <li>
            <Link 
              to="/for-dentists" 
              className={`nav-link ${location.pathname === '/for-dentists' ? 'active' : ''}`}
            >
              For Dentists
            </Link>
          </li>
          <li>
            <Link 
              to="/about" 
              className={`nav-link ${location.pathname === '/about' ? 'active' : ''}`}
            >
              About
            </Link>
          </li>
          {/* NEW: Patient Info Button */}
          <li>
            <Link 
              to="/symptoms" 
              className={`nav-link patient-link ${location.pathname === '/symptoms' ? 'active' : ''}`}
            >
              🩺 Patient Info
            </Link>
          </li>
          <li>
            <Link 
              to="/login" 
              className={`nav-link ${location.pathname === '/login' ? 'active' : ''}`}
            >
              Login
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
