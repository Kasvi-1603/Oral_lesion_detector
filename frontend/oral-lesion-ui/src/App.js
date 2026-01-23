import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Analysis from "./pages/Analysis";
import Classifications from "./pages/Classifications";
import ForDentists from "./pages/ForDentists";
import About from "./pages/About";
import Login from "./pages/Login";
import Footer from "./components/Footer";
import SymptomExplanation from './pages/SymptomExplanation';
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/analysis" element={<Analysis />} />
            <Route path="/classifications" element={<Classifications />} />
            <Route path="/for-dentists" element={<ForDentists />} />
            <Route path="/about" element={<About />} />
            <Route path="/login" element={<Login />} />
            <Route path="/symptoms" element={<SymptomExplanation />} />
          </Routes>
        </div>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
