import { useState } from "react";

function Book() {
  const [book, setBook] = useState(null);
  const [message, setMessage] = useState("");
  const token = localStorage.getItem("access");
  const getSelectedText = () => {
    const selection = window.getSelection();
    return selection.toString().trim();
  };
  const [selectedText, setSelectedText] = useState("");
  const handleTextSelection = () => {
    const text = window.getSelection().toString().trim();
    setSelectedText(text);
  };

  const fetchBook = async () => {
    const res = await fetch("http://127.0.0.1:8000/books/api/book/");
    const data = await res.json();
    setBook(data);
    setMessage("", data);
  };

  const saveBook = async () => {
    if (!book) return;
    const res = await fetch("http://127.0.0.1:8000/books/save/", {
      method: "POST",
      headers: { 
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`,
       },
      body: JSON.stringify({
        title: book.title,
        author: book.authors,
        subject: book.subjects,
        bookshelves: book.bookshelves,
        language: book.language,
        text_url: book.text_url
      }),
    });

    const data = await res.json();
    setMessage(data.message || "Book saved!"); 
  };

  const translateText = async (text) => {
    const token = localStorage.getItem("access");
    try {
      const res = await fetch("http://127.0.0.1:8000/books/translate/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ text }),
      });

      const data = await res.json();
      alert("Translation: " + data.translation);
    } catch (err) {
      console.error(err);
      alert("Translation failed");
    }
  };

  return (
    <div className="container py-5">
      <h1 className="text-center mb-4">Random Gutendex Book</h1>

      <div className="text-center">
        <button className="btn btn-primary" onClick={fetchBook}>
          Get Book
        </button>
      </div>

      {book && (
        <div className="card mt-4 shadow-sm">
          <div className="card-body" onMouseUp={handleTextSelection}>
            <h5 className="card-title">{book.title}</h5>
            <h6 className="card-subtitle mb-2 text-muted">
              {book.authors?.name}
            </h6>
            <p className="card-text">{book.summary}</p>

            <ul className="list-group list-group-flush">
              <li className="list-group-item">
                <strong>Subject:</strong> {book.subject}
              </li>
              <li className="list-group-item">
                <strong>Bookshelves:</strong> {book.bookshelves}
              </li>
              <li className="list-group-item">
                <strong>Language:</strong> {book.language}
              </li>
            </ul>

            <a href={book.text_url} className="btn btn-outline-secondary mt-3 me-2">
              Read Online
            </a>

            <button className="btn btn-success mt-3" onClick={saveBook}>
              Save Book
            </button>

            {message && (
              <p className="mt-3 text-success">
                {message}
              </p>
            )}
            {selectedText && (
              <div className="mt-3">
                <p>Selected: "{selectedText}"</p>
                <button
                  className="btn btn-primary me-2"
                  onClick={() => translateText(selectedText)}
                >
                  Translate with DeepL
                </button>
                <button
                  className="btn btn-success"
                >
                  Add to Anki
                </button>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default Book;
