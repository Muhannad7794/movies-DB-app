import React from 'react';
import './Order.css'; // Make sure to import the CSS file

function StudiosOrder({ onOrderChange }) {
  return (
    <div className="order-container"> {/* Add the class name for styling */}
      <label htmlFor="order" className="order-label">Order By:</label>
      <select id="order" className="order-select" onChange={(e) => onOrderChange(e.target.value)}> {/* Add the class name for styling */}
        <option value="">Select</option>
        <option value="name">Name</option>
        <option value="founded">Founded Year</option>
      </select>
    </div>
  );
}

export default StudiosOrder;
