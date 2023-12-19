import React from 'react';

function DirectorsOrder({ onOrderChange }) {
  return (
    <div>
      <label htmlFor="order">Order By: </label>
      <select id="order" onChange={(e) => onOrderChange(e.target.value)}>
        <option value="">Select</option>
        {/* Add options for ordering directors */}
        <option value="director_name">Name</option>
        <option value="director_date_of_birth">Date OF Birth</option>
        {/* Add more options as per your backend's capabilities */}
      </select>
    </div>
  );
}

export default DirectorsOrder;
