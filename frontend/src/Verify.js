import React, { useState, useEffect } from "react";
import { API_URL } from "./api";
import { useParams } from "react-router-dom";

export default function Verify() {
  const { cid } = useParams();
  const [certID, setCertID] = useState(cid || "");
  const [result, setResult] = useState(null);

  useEffect(() => {
    if (cid) verifyCert(cid);
  }, [cid]);

  const verifyCert = async (id) => {
    
    const res = await fetch(`${API_URL}/verify/${id}`);
    
    const data = await res.json();
    setResult(data);
  };
  
  return (
    <div>
      <h2 className="text-xl font-semibold mb-4 text-gray-700">Verify Certificate</h2>

      <input
        className="w-full p-3 border rounded-lg shadow-sm focus:ring focus:ring-blue-200"
        placeholder="Enter Certificate ID"
        value={certID}
        onChange={(e) => setCertID(e.target.value)}
      />

      <button
        onClick={() => verifyCert(certID)}
        className="mt-4 w-full bg-blue-600 text-white py-3 rounded-lg shadow hover:bg-blue-700 transition"
      >
        Verify Certificate
      </button>

      {/* Result */}
      {result && result.valid && (
        <div className="mt-6 p-4 bg-green-50 border border-green-200 rounded-lg">
          <h3 className="text-green-700 font-bold text-lg">✔ Certificate is VALID</h3>
          <p><b>Issuer:</b> {result.issuer}</p>
          <p><b>Timestamp:</b> {new Date(result.timestamp * 1000).toString()}</p>
          <p><b>Hash:</b> {result.hash}</p>
        </div>
      )}

      {result && !result.valid && (
        <div className="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg">
          <h3 className="text-red-700 font-bold text-lg">❌ Certificate NOT FOUND</h3>
          <p>{result.reason}</p>
        </div>
      )}
    </div>
  );
}
