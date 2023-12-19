import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; 

function Navbar() {
  return (
    <nav>
      <h1>The Movies Database</h1>
      <div className="nav-links">
        <Link to="/">Movies</Link>
        <Link to="/directors">Directors</Link>
        <Link to="/studios">Studios</Link>
      </div>
    </nav>
  );
}

export default Navbar;
