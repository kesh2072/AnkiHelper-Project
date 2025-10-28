import React, { useState, useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { login } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://localhost:8000/api/token/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    const data = await response.json();

    if (response.ok) {
      login(data.access, data.refresh);
      alert("Logged in successfully!");
      navigate("/profile")
    } else {
      alert("Invalid credentials");
    }
  };

return(
  <div className="container d-flex justify-content-center align-items-center vh-75">
     <div className="w-100" style={{ maxWidth: "400px" }}>
  <form onSubmit={handleSubmit}> 
    <h1 className="h3 mb-3 fw-normal">Please sign in</h1> 
    <div class="form-floating mb-3"> 
    <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com" onChange={(e) => setUsername(e.target.value)}/> 
    <label for="floatingInput">Username</label> 
    </div> 
    <div class="form-floating mb-3"> 
      <input type="password" class="form-control" id="floatingPassword" placeholder="Password" onChange={(e) => setPassword(e.target.value)}/> 
      <label for="floatingPassword">Password</label> 
      </div> 
      <div class="form-check text-start mb-3">  
        <input class="form-check-input" type="checkbox" value="remember-me" id="checkDefault"/> 
        <label class="form-check-label" for="checkDefault">
          Remember me
  </label> 
  </div> 
  <button class="btn btn-primary w-100 py-2 mb-3" type="submit">Sign in</button> 
  </form>
  </div>
  </div>
)
}

export default Login;
