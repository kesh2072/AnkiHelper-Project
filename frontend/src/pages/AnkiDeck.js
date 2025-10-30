import React, { useState } from "react";

function Anki() {
  const [message, setMessage] = useState("");
  const [decks, setDecks] = useState([]);
  const [cards, setCards] = useState([]);
  const [selectedDeck, setSelectedDeck] = useState(null);

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

  const openDeck = async (deckName) => {
  const token = localStorage.getItem("access");
  setSelectedDeck(deckName);

  try {
    const res = await fetch(`http://127.0.0.1:8000/anki/api/deck/${deckName}/`, {
      headers: {
        "Authorization": `Bearer ${token}`,
        "Content-Type": "application/json"
      }
    });

    if (res.status === 401) {
      console.error("Unauthorized request – token missing or invalid");
      setMessage("Please log in again.");
      return;
    }

    const data = await res.json();
    console.log("Deck data:", data);
    setCards(data);
  } catch (error) {
    console.error("Error fetching cards:", error);
    setMessage("Error fetching cards");
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
              <button
                  className="btn btn-primary"
                  onClick={() => openDeck(deck)}
                >
                  Open Deck
                </button>
            </div>
          </div>
        </div>
      ))}
    </div>
    {selectedDeck && (
        <div className="mt-5">
          <h3>Cards in {selectedDeck}</h3>
          <ul className="list-group">
            {cards.map((card) => (
            <li key={card.cardId} className="list-group-item">
              {Object.entries(card.fields).map(([key, value]) => (
                <div key={key}>
                  <strong>{key}:</strong>{" "}
                  <span dangerouslySetInnerHTML={{ __html: value.value }}></span>
                </div>
              ))}
            </li>
          ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default Anki;