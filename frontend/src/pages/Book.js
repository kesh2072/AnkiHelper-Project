import { useState } from "react";

function Book() {
  const [book, setBook] = useState(null);
  const [message, setMessage] = useState("");
  const token = localStorage.getItem("access");
  const [backText, setBackText] = useState("");
  const [tags, setTags] = useState("");
  const getSelectedText = () => {
    const selection = window.getSelection();
    return selection.toString().trim();
  };
  const [selectedText, setSelectedText] = useState("");
  const handleTextSelection = () => {
    const text = window.getSelection().toString().trim();
    setSelectedText(text);
  };
  const [deckName, setDeckName] = useState("Default");

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

  const addToAnki = async (front_text, back_text, tags="") => {
    if (!selectedText) return;

    try {
      const res = await fetch("http://127.0.0.1:8000/anki/api/addCard/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${localStorage.getItem("access")}`,
        },
        body: JSON.stringify({
          text: selectedText,
          deck: deckName,
          front_text: selectedText,
          back_text: backText,
        }),
      });

      const data = await res.json();
      setMessage(data.status || "Card added!");
    } catch (err) {
      console.error(err);
      setMessage("Failed to add card");
    }
  };

  return (
  <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50 py-8 px-4">
    <div className="max-w-7xl mx-auto">
      {/* Header */}
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">
          Gutendex Book Explorer
        </h1>
        <button
          className="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-8 rounded-lg shadow-md transition-colors duration-200"
          onClick={fetchBook}
        >
          Get Random Book
        </button>
      </div>

      {book && (
        <div className="grid lg:grid-cols-3 gap-6">
          {/* LEFT SIDE - Book Information (2/3 width) */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-xl shadow-lg p-6">
              <div onMouseUp={handleTextSelection}>
                {/* Book Header */}
                <div className="border-b border-gray-200 pb-4 mb-4">
                  <h2 className="text-3xl font-bold text-gray-900 mb-2">
                    {book.title}
                  </h2>
                  <p className="text-lg text-gray-600">
                    by {book.authors?.name}
                  </p>
                </div>

                {/* Summary */}
                <div className="mb-6">
                  <h3 className="text-xl font-semibold text-gray-800 mb-3">
                    Summary
                  </h3>
                  <p className="text-gray-700 leading-relaxed">
                    {book.summary}
                  </p>
                </div>

                {/* Book Details */}
                <div className="space-y-3 mb-6">
                  <div className="flex items-start">
                    <span className="font-semibold text-gray-800 w-32">
                      Subject:
                    </span>
                    <span className="text-gray-700">{book.subject}</span>
                  </div>
                  <div className="flex items-start">
                    <span className="font-semibold text-gray-800 w-32">
                      Bookshelves:
                    </span>
                    <span className="text-gray-700">{book.bookshelves}</span>
                  </div>
                  <div className="flex items-start">
                    <span className="font-semibold text-gray-800 w-32">
                      Language:
                    </span>
                    <span className="text-gray-700">{book.language}</span>
                  </div>
                </div>

                {/* Action Buttons */}
                <div className="flex flex-wrap gap-3">
                  <a
                    href={book.text_url}
                    className="bg-gray-100 hover:bg-gray-200 text-gray-800 font-semibold py-2 px-6 rounded-lg transition-colors duration-200"
                  >
                    Read Online
                  </a>
                  <button
                    className="bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-6 rounded-lg transition-colors duration-200"
                    onClick={saveBook}
                  >
                    Save Book
                  </button>
                </div>

                {/* Success Message */}
                {message && (
                  <div className="mt-4 p-3 bg-green-50 border border-green-200 rounded-lg">
                    <p className="text-green-800">{message}</p>
                  </div>
                )}
              </div>
            </div>
          </div>

          <div className="lg:col-span-1 space-y-6">
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-xl font-bold text-gray-800 mb-4 flex items-center">
                Add to Anki
              </h3>
              
              {selectedText ? (
                <div>
                  <div className="bg-gray-50 rounded-lg p-4 mb-4">
                    <p className="text-sm text-gray-600 mb-2">Selected Text:</p>
                    <p className="text-gray-800 font-medium">"{selectedText}"</p>
                  </div>
                  <button
                    className="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-4 rounded-lg transition-colors duration-200"
                    onClick={() => addToAnki(selectedText, backText, [""])}
                  >
                    Add to Deck
                  </button>
                </div>
              ) : (
                <div className="text-center py-8">
                  <p className="text-gray-500 text-sm">
                    Select text from the book summary to add it to your Anki deck
                  </p>
                </div>
              )}
            </div>

            {/* Translation Section */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-xl font-bold text-gray-800 mb-4 flex items-center">
                Translation
              </h3>
              
              {selectedText ? (
                <div>
                  <div className="bg-gray-50 rounded-lg p-4 mb-4">
                    <p className="text-sm text-gray-600 mb-2">Selected Text:</p>
                    <p className="text-gray-800 text-sm italic">"{selectedText}"</p>
                  </div>
                  <button
                    className="w-full bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 px-4 rounded-lg transition-colors duration-200 mb-4"
                    onClick={() => translateText(selectedText)}
                  >
                    Translate with DeepL
                  </button>
                  
                  {backText && (
                    <div className="bg-purple-50 border border-purple-200 rounded-lg p-4">
                      <p className="text-sm text-purple-600 mb-2">Translation:</p>
                      <p className="text-gray-800">{backText}</p>
                    </div>
                  )}
                </div>
              ) : (
                <div className="text-center py-8">
                  <p className="text-gray-500 text-sm">
                    Select text from the book summary to translate it
                  </p>
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  </div>
);
}
export default Book;