import React from "react";
import { Link, useLocation } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  const location = useLocation();

  return (
    <nav className="navbar">
      <div className="nav-container">
        <Link to="/" className="nav-logo">
          <span className="logo-icon">🦷</span>
          Oral Lesion Classifier
        </Link>
        <ul className="nav-menu">
          <li className="nav-item">
            <Link 
              to="/" 
              className={location.pathname === "/" ? "nav-link active" : "nav-link"}
            >
              Home
            </Link>
          </li>
          <li className="nav-item">
            <Link 
              to="/analysis" 
              className={location.pathname === "/analysis" ? "nav-link active" : "nav-link"}
            >
              Analysis
            </Link>
          </li>
          <li className="nav-item">
            <Link 
              to="/classifications" 
              className={location.pathname === "/classifications" ? "nav-link active" : "nav-link"}
            >
              Classifications
            </Link>
          </li>
          <li className="nav-item">
            <Link 
              to="/for-dentists" 
              className={location.pathname === "/for-dentists" ? "nav-link active" : "nav-link"}
            >
              For Dentists
            </Link>
          </li>
          <li className="nav-item">
            <Link 
              to="/about" 
              className={location.pathname === "/about" ? "nav-link active" : "nav-link"}
            >
              About
            </Link>
          </li>
          <li className="nav-item">
            <Link 
              to="/login" 
              className={location.pathname === "/login" ? "nav-link nav-link-login active" : "nav-link nav-link-login"}
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
