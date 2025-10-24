import React, { useState } from "react";

function Anki() {
  const [message, setMessage] = useState("");

  const viewDeck = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/anki/");
      if (!res.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await res.json();
      setMessage(JSON.stringify(data, null, 2));
    } catch (error) {
      console.error("Error fetching decks:", error);
      setMessage("Error fetching decks");
    }
  };

  return (
    <div className="p-4">
      <button
        className="btn btn-primary mb-4"
        onClick={viewDeck}
      >
        View your Anki decks
      </button>
      {message && (
        <pre className="bg-gray-100 p-4 rounded">{message}</pre>
      )}
    </div>
  );
}

export default Anki;