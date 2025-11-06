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
        <button onClick={handleLogout} type="button" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
          Logout
        </button>
        <a href="/books/saved" type="button" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
          Saved Books
        </a>
        <a href="/anki" type="button" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
          Your Anki decks
        </a>
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