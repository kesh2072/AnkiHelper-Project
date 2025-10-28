import React, { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";

function ProfilePage() {
  const { logout } = useContext(AuthContext);
  const {isLoggedIn} = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
  };

  return (
    <div className="container py-5">
      <h1>Profile Page</h1>
      {isLoggedIn ? (
      <div>
      <button onClick={handleLogout} className="btn btn-danger">
        Logout
      </button>
        <Link to="/books/saved" className="btn btn-primary rounded-pill px-3" type="button">Saved Books</Link>
        <Link to="/anki" className="btn btn-primary rounded-pill px-3" type="button">Your Anki decks</Link>
      </div>
      ) : (
        <div>
          <Link to="/login" className="btn btn-primary rounded-pill px-3" type="button">Login</Link>
          <Link to="/register" className="btn btn-primary rounded-pill px-3" type="button">Create an account</Link>
      </div>
      )}
    </div>
  );
}

export default ProfilePage;