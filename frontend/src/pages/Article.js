import { useState } from "react";

function Article() {
  const [article, setArticle] = useState(null);
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
    const [backText, setBackText] = useState("");
    const [note, setNote] = useState("");

  const fetchArticle = async () => {
    const res = await fetch("http://127.0.0.1:8000/books/api/article/");
    const data = await res.json();
    setArticle(data);
    setMessage("", data);
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

  async function addToAnki(front, back, note) {
    try {
        const response = await fetch("/add_to_anki", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            word: front,
            translation: back,
            note: note
        }),
        });
        const data = await response.json();
        if (data.error) throw new Error(data.error);
        alert("Added to Anki!");
    } catch (err) {
        console.error("Anki error:", err);
        alert("Failed to add card.");
    }
    }

  function showAnkiModal(word, translation) {
    const modal = document.createElement('div');
    modal.className = 'anki-modal';
    modal.innerHTML = `
        <label>Word: <input id="word" value="${word}"></label><br>
        <label>Translation: <input id="translation" value="${translation}"></label><br>
        <label>Sentence / Note:</label><br>
        <textarea id="note"></textarea><br>
        <button id="addToAnki">Add to Anki</button>
    `;
    document.body.appendChild(modal);

    document.getElementById('addToAnki').onclick = async () => {
        const payload = {
        word: document.getElementById('word').value,
        translation: document.getElementById('translation').value,
        note: document.getElementById('note').value
        };
        await fetch('/add_to_anki', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
        });
        alert('Added to Anki!');
        modal.remove();
    };
    }

  return(
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50 py-8 px-4">
    <div className="max-w-7xl mx-auto">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">
          News Articles
        </h1>
        <button
          className="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 px-8 rounded-lg shadow-md transition-colors duration-200"
          onClick={fetchArticle}
        >
          Get Random Article
        </button>
      </div>

      {article && (
        <div className="grid lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2">
            <div className="bg-white rounded-xl shadow-lg p-6">
              <div onMouseUp={handleTextSelection}>
                <div className="border-b border-gray-200 pb-4 mb-4">
                  <h2 className="text-3xl font-bold text-gray-900 mb-2">
                    {article.title}
                  </h2>
                </div>

                <div className="mb-6">
                  <h3 className="text-xl font-semibold text-gray-800 mb-3">
                    Content
                  </h3>
                  <p className="text-gray-700 leading-relaxed">
                    {article.text}
                  </p>
                </div>

                {message && (
                  <div className="mt-4 p-3 bg-green-50 border border-green-200 rounded-lg">
                    <p className="text-green-800">{message}</p>
                  </div>
                )}
              </div>
            </div>
          </div>

          {selectedText ? (
            <div>
                <div className="bg-gray-50 rounded-lg p-4 mb-4">
                <p className="text-sm text-gray-600 mb-2">Selected Text:</p>
                <p className="text-gray-800 font-medium">"{selectedText}"</p>
                </div>

                <label className="block text-sm font-medium text-gray-600 mb-1">Translation</label>
                <input
                type="text"
                value={backText}
                onChange={(e) => setBackText(e.target.value)}
                placeholder="Enter or fetch translation..."
                className="w-full border rounded-lg p-2 mb-3"
                />

                <label className="block text-sm font-medium text-gray-600 mb-1">Notes</label>
                <textarea
                value={note}
                onChange={(e) => setNote(e.target.value)}
                placeholder="Optional sentence or context"
                className="w-full border rounded-lg p-2 mb-4"
                />

                <button
                className="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-4 rounded-lg transition-colors duration-200"
                onClick={() => addToAnki(selectedText, backText, note)}
                >
                Add to Deck
                </button>
            </div>
            ): (
                <div></div>
            )
            }

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
      )}
    </div>
  </div>
);
}

export default Article;