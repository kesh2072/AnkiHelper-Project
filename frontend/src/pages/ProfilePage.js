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
      <button onClick={handleLogout} className="btn btn-danger">
        Logout
      </button>
      ) : (
        <div>
        <Link to="/login">Login</Link>
        <Link to="/register">Create an account</Link>
      </div>
      )}
    </div>
  );
}

export default ProfilePage;