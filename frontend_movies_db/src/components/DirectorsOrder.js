import React from 'react';
import './Order.css'; // Make sure to import the CSS file

function DirectorsOrder({ onOrderChange }) {
  return (
    <div className="order-container"> {/* Add the class name for styling */}
      <label htmlFor="order" className="order-label">Order By:</label>
      <select id="order" className="order-select" onChange={(e) => onOrderChange(e.target.value)}> {/* Add the class name for styling */}
        <option value="">Select</option>
        <option value="director_name">Name</option>
        <option value="director_date_of_birth">Date OF Birth</option>
        {/* Add more options as per your backend's capabilities */}
      </select>
    </div>
  );
}

export default DirectorsOrder;
