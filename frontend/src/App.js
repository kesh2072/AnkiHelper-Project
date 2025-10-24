// App.js
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Book from "./pages/Book";
import Profile from "./pages/ProfilePage";
import Header from "./components/Header";
import SavedBooks from "./pages/SavedBooks";
import Register from "./pages/Register";
import Login from "./pages/Login";
import Anki from "./pages/AnkiDeck";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Book />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/books/saved" element={<SavedBooks />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
        <Route path="/anki" element={<Anki />} />
      </Routes>
    </Router>
  );
}

export default App;
