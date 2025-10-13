// App.js
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Book from "./pages/Book";
import Profile from "./pages/ProfilePage";
import Header from "./components/Header";
import SavedBooks from "./pages/SavedBooks";
import Register from "./pages/Register";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Book />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/saved" element={<SavedBooks />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  );
}

export default App;
