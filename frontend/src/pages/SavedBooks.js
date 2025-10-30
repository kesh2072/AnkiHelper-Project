import { useState, useEffect, useContext } from "react";
import { AuthContext } from "../context/AuthContext";

function SavedBooks() {
  const [message, setMessage] = useState("");
  const [savedBooks, setSavedBooks] = useState([]);
  const token = localStorage.getItem("access");
  const {isLoggedIn} = useContext(AuthContext);

  const deleteArticle = async (id) => {
  const token = localStorage.getItem("access");

  const res = await fetch(`http://127.0.0.1:8000/books/delete/${id}/`, {
    method: "DELETE",
    headers: {
      "Authorization": `Bearer ${token}`,
    },
  });

  const data = await res.json();
  if (res.ok) {
    setMessage(data.message);
    setSavedBooks(prev => prev.filter(article => article.id !== id));
  } else {
    setMessage(data.error || "Could not delete article");
  }
  };

  useEffect(() => {
    const fetchSavedBooks = async () => {
      const res = await fetch("http://127.0.0.1:8000/books/saved/", {
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
      });
      const data = await res.json();
      setSavedBooks(data);

    };

    fetchSavedBooks();
  }, []);

  return (
    <div>
    {isLoggedIn ? (
      <div className="container py-5">
      <h1 className="text-center mb-4">My Saved Books</h1>

      {savedBooks.length === 0 ? (
        <p className="text-center">No saved books yet.</p>
      ) : (
        savedBooks.map((book, index) => (
          <div key={index} className="card mt-4 shadow-sm">
            <div className="card-body">
              <h5 className="card-title">{book.title}</h5>
              <h6 className="card-subtitle mb-2 text-muted">{book.author}</h6>
              <p className="card-text">{book.excerpt}</p>
              <button
                className="btn btn-danger btn-sm"
                onClick={() => deleteArticle(book.id)}
              >
                Delete
              </button>
              {book.text_url && (
                <a
                  href={book.text_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="btn btn-outline-secondary mt-3"
                >
                  Read Online
                </a>
              )}
            </div>
          </div>
        ))
      )}
    </div>
    ) : (
      <div>
      <p>
        please log in to view this page
      </p>
      </div>
    )
}
</div>
    
  );
}

export default SavedBooks;
