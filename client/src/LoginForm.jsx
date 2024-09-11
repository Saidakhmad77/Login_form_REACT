import { useState } from 'react';
import './LoginForm.css';

const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();
    console.log("Email:", email);
    console.log("Password:", password);
  };

  const handleRegister = () => {
    console.log("Redirecting to registration page...");
  };

  return (
    <div className="login-form-container">
      <form onSubmit={handleLogin}>
        <h2>Login</h2>
        <div className="input-container">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>

        <div className="input-container">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        <button type="submit" className="login-btn">Sign In</button>
      </form>

      <button onClick={handleRegister} className="register-btn">
        Register
      </button>
    </div>
  );
};

export default LoginForm;
