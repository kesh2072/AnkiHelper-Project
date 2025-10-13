// pages/ProfilePage.js
import React from "react";
import { Link } from "react-router-dom";

function Profile() {
  return (
    <div className="container py-5">
      <h1>Profile Page</h1>
      <ul>
        <li>
          <Link className="nav-link" to="/register/">Create an account</Link>
        </li>
      </ul>
    </div>
  );
}

export default Profile;
