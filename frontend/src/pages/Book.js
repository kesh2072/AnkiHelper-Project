// pages/Book.js
import { useState } from "react";

function Book() {
  const [book, setBook] = useState(null);

  const fetchBook = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/book/");
    const data = await res.json();
    setBook(data);
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
          <div className="card-body">
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
            <a href={book.text_url} className="btn btn-outline-secondary mt-3">
              Read Online
            </a>
          </div>
        </div>
      )}
    </div>
  );
}

export default Book;
