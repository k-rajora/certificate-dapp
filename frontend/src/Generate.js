import React, { useState } from "react";
import { API_URL } from "./api";

export default function Generate() {
  const [form, setForm] = useState({
    name: "",
    course: "",
    grade: "",
    date: ""
  });

  const [result, setResult] = useState(null);

  const generateCert = async () => {
    const res = await fetch(API_URL + "/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4 text-gray-700">Generate Certificate</h2>

      {/* Input Fields */}
      <div className="space-y-4">
        <input
          className="w-full p-3 border rounded-lg shadow-sm focus:ring focus:ring-blue-200"
          placeholder="Student Name"
          onChange={(e) => setForm({ ...form, name: e.target.value })}
        />

        <input
          className="w-full p-3 border rounded-lg shadow-sm focus:ring focus:ring-blue-200"
          placeholder="Course Name"
          onChange={(e) => setForm({ ...form, course: e.target.value })}
        />

        <input
          className="w-full p-3 border rounded-lg shadow-sm focus:ring focus:ring-blue-200"
          placeholder="Grade"
          onChange={(e) => setForm({ ...form, grade: e.target.value })}
        />

        <input
          className="w-full p-3 border rounded-lg shadow-sm focus:ring focus:ring-blue-200"
          type="date"
          onChange={(e) => setForm({ ...form, date: e.target.value })}
        />
      </div>

      {/* Submit */}
      <button
        onClick={generateCert}
        className="mt-6 w-full bg-blue-600 text-white font-semibold py-3 rounded-lg shadow hover:bg-blue-700 transition"
      >
        Generate Certificate
      </button>

      {/* Result */}
      {result && (
        <div className="mt-6 p-4 bg-green-50 border border-green-200 rounded-lg">
          <p className="font-semibold text-green-700">
            Certificate successfully generated!
          </p>

          <p><b>ID:</b> {result.certificate_id}</p>
          <p><b>Tx Hash:</b> {result.tx_hash}</p>

          <a
            className="text-blue-600 underline font-semibold"
            href={result.download_url}
            target="_blank"
          >
            Download Certificate PDF
          </a>
        </div>
      )}
    </div>
  );
}
