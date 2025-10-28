import React, { useState } from "react";

function Anki() {
  const [message, setMessage] = useState("");
  const [decks, setDecks] = useState([]);

  const viewDeck = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/anki/api/anki/");
      if (!res.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await res.json();
      setDecks(data);
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
      <div className="row">
      {decks.map((deck, index) => (
        <div className="col-md-4 mb-3" key={index}>
          <div className="card h-100">
            <div className="card-body">
              <h5 className="card-title">{deck}</h5>
              <p className="card-text">Put some deck information here</p>
              <button className="btn btn-primary">Open Deck</button>
            </div>
          </div>
        </div>
      ))}
    </div>
    </div>
  );
}

export default Anki;