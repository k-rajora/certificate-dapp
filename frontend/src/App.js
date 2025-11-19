import React from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Generate from "./Generate";
import Verify from "./Verify";

export default function App() {
  return (
    <BrowserRouter>
      <div className="container">
        <h1 style={{
          textAlign: "center",
          color: "#c1007e",
          marginBottom: "20px"
        }}>
          example.com Certificate System
        </h1>

        <nav style={{ textAlign: "center", marginBottom: "20px",
          color : "#fffff"
         }}>
          <Link to="/">Generate</Link> | 
          <Link to="/verify">Verify</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Generate />} />
          <Route path="/verify" element={<Verify />} />
          <Route path="/verify/:cid" element={<Verify />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
