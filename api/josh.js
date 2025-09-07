import React, { useState, useRef } from "react";

// Teacher's Day single-file React component ready to paste into a Next.js page
// Styling uses Tailwind CSS classes (you can also use the Tailwind CDN for a quick deploy)

export default function TeachersDayApp() {
  const [teacher, setTeacher] = useState("Dear Teacher");
  const [message, setMessage] = useState("Thank you for inspiring me every day.");
  const [accent, setAccent] = useState("indigo");
  const [emoji, setEmoji] = useState("🌟");
  const [showCard, setShowCard] = useState(true);

  // For downloading the SVG card
  const svgRef = useRef(null);

  const accentMap = {
    indigo: "from-indigo-400 to-indigo-600",
    pink: "from-pink-400 to-pink-600",
    teal: "from-teal-400 to-teal-600",
    amber: "from-amber-400 to-amber-600",
  };

  function downloadCard() {
    const svg = svgRef.current;
    if (!svg) return;

    // Serialize SVG and convert to PNG via a temporary canvas
    const serializer = new XMLSerializer();
    const svgString = serializer.serializeToString(svg);
    const svgBlob = new Blob([svgString], { type: "image/svg+xml;charset=utf-8" });
    const url = URL.createObjectURL(svgBlob);

    const img = new Image();
    img.onload = () => {
      const canvas = document.createElement("canvas");
      canvas.width = img.width;
      canvas.height = img.height;
      const ctx = canvas.getContext("2d");
      // White background
      ctx.fillStyle = "#ffffff";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(img, 0, 0);
      const pngUrl = canvas.toDataURL("image/png");
      const a = document.createElement("a");
      a.href = pngUrl;
      a.download = `${teacher.replace(/\s+/g, "_") || "teachers_card"}.png`;
      a.click();
      URL.revokeObjectURL(url);
    };
    img.onerror = () => URL.revokeObjectURL(url);
    img.src = url;
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-100 to-white flex items-center justify-center p-6">
      <div className="max-w-4xl w-full grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
        {/* Controls */}
        <div className="p-6 bg-white rounded-2xl shadow-lg">
          <h1 className="text-2xl font-extrabold mb-2">Teacher's Day Card Maker</h1>
          <p className="text-sm text-gray-500 mb-4">Create a beautiful, shareable card for your teacher — then download or share it.</p>

          <label className="block text-sm font-medium text-gray-700 mt-3">Teacher's name</label>
          <input
            value={teacher}
            onChange={(e) => setTeacher(e.target.value)}
            className="mt-1 block w-full rounded-md border-gray-200 shadow-sm focus:ring-2 focus:ring-indigo-300 p-2"
            placeholder="e.g. Mrs. Santos"
          />

          <label className="block text-sm font-medium text-gray-700 mt-3">Message</label>
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            rows={4}
            className="mt-1 block w-full rounded-md border-gray-200 shadow-sm focus:ring-2 focus:ring-indigo-300 p-2"
          />

          <label className="block text-sm font-medium text-gray-700 mt-3">Accent</label>
          <div className="flex gap-2 mt-2">
            {Object.keys(accentMap).map((k) => (
              <button
                key={k}
                onClick={() => setAccent(k)}
                className={`px-3 py-1 rounded-md font-medium shadow-sm hover:scale-105 transform transition ${accent === k ? "ring-4 ring-offset-2" : "opacity-90"}`}>
                {k}
              </button>
            ))}
          </div>

          <label className="block text-sm font-medium text-gray-700 mt-3">Emoji</label>
          <div className="flex items-center gap-2 mt-2">
            <input value={emoji} onChange={(e) => setEmoji(e.target.value)} className="w-16 p-2 rounded-md text-xl text-center border-gray-200" />
            <div className="text-sm text-gray-600">Try: 🎓 🌟 ❤️ ✨ 🍎 📝</div>
          </div>

          <div className="flex gap-3 mt-6">
            <button
              onClick={() => setShowCard((s) => !s)}
              className="px-4 py-2 rounded-lg bg-white border shadow-sm hover:shadow-md">
              {showCard ? "Hide" : "Show"} preview
            </button>

            <button onClick={downloadCard} className="px-4 py-2 rounded-lg bg-indigo-600 text-white shadow hover:bg-indigo-700">Download PNG</button>

            <button
              onClick={() => {
                // quick reset
                setTeacher("Dear Teacher");
                setMessage("Thank you for inspiring me every day.");
                setAccent("indigo");
                setEmoji("🌟");
              }}
              className="px-4 py-2 rounded-lg bg-gray-50 border">
              Reset
            </button>
          </div>

          <p className="text-xs text-gray-400 mt-4">Tip: Add a heartfelt personal message and download the card to send via chat or print it.</p>
        </div>

        {/* Preview */}
        <div className="p-6 flex flex-col items-center">
          {showCard ? (
            <div className="w-full max-w-md">
              {/* SVG Card (so it can be downloaded crisply) */}
              <div className="text-right mb-2 text-xs text-gray-500">Preview (SVG)</div>
              <div className="rounded-2xl overflow-hidden shadow-2xl inline-block">
                <svg
                  ref={svgRef}
                  xmlns="http://www.w3.org/2000/svg"
                  width="900"
                  height="600"
                  viewBox="0 0 900 600"
                >
                  <defs>
                    <linearGradient id="g" x1="0" x2="1" y1="0" y2="1">
                      <stop offset="0%" stopColor="#8b5cf6" />
                      <stop offset="100%" stopColor="#4f46e5" />
                    </linearGradient>
                    <filter id="f" x="-20%" y="-20%" width="140%" height="140%">
                      <feDropShadow dx="0" dy="10" stdDeviation="24" floodColor="#000" floodOpacity="0.12" />
                    </filter>
                  </defs>

                  {/* Background */}
                  <rect width="900" height="600" rx="34" fill="#ffffff" />

                  {/* Decorative gradient blob */}
                  <g filter="url(#f)">
                    <ellipse cx="700" cy="120" rx="260" ry="140" fill={accent === 'pink' ? '#fb7185' : accent === 'teal' ? '#14b8a6' : accent === 'amber' ? '#f59e0b' : '#6366f1'} opacity="0.16" />
                    <ellipse cx="180" cy="440" rx="320" ry="160" fill={accent === 'pink' ? '#fb7185' : accent === 'teal' ? '#14b8a6' : accent === 'amber' ? '#f59e0b' : '#6366f1'} opacity="0.12" />
                  </g>

                  {/* Header */}
                  <g transform="translate(60,60)">
                    <rect x="0" y="0" width="780" height="120" rx="20" fill="#111827" opacity="0.04" />
                    <text x="40" y="54" fontFamily="Inter, Arial, sans-serif" fontSize="40" fontWeight="700" fill="#111827">{emoji} Teacher's Day</text>
                    <text x="40" y="94" fontFamily="Inter, Arial, sans-serif" fontSize="18" fill="#374151">{teacher}</text>
                  </g>

                  {/* Message box */}
                  <g transform="translate(80,200)">
                    <foreignObject x="0" y="0" width="740" height="340">
                      <div xmlns="http://www.w3.org/1999/xhtml" style={{ fontFamily: 'Inter, Arial, sans-serif' }}>
                        <div style={{ padding: 28, borderRadius: 16, background: 'linear-gradient(180deg, rgba(255,255,255,0.9), rgba(255,255,255,0.85))', width: 684, height: 284, boxSizing: 'border-box', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                          <div>
                            <div style={{ fontSize: 26, fontWeight: 700, color: '#0f172a', marginBottom: 12 }}>{teacher},</div>
                            <div style={{ fontSize: 16, color: '#334155', lineHeight: 1.45 }}>{message}</div>
                          </div>

                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                            <div style={{ fontSize: 14, color: '#475569' }}>With gratitude,</div>
                            <div style={{ fontSize: 18, fontWeight: 700, color: '#0f172a' }}>— Your student</div>
                          </div>
                        </div>
                      </div>
                    </foreignObject>
                  </g>
                </svg>
              </div>

              <div className="mt-4 text-sm text-gray-500">Right-click the image or use <strong>Download PNG</strong> to save a copy.</div>
            </div>
          ) : (
            <div className="w-full max-w-md flex items-center justify-center p-8 bg-gray-50 rounded-xl">
              <div className="text-gray-400">Preview hidden — show it to edit the card.</div>
            </div>
          )}
        </div>
      </div>

      {/* small footer */}
      <div className="fixed bottom-6 left-6 text-xs text-gray-400">Made with ❤️ — Teacher's Day</div>
    </div>
  );
}
