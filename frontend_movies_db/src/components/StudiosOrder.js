import React from 'react';

function StudiosOrder({ onOrderChange }) {
  return (
    <div>
      <label htmlFor="order">Order By: </label>
      <select id="order" onChange={(e) => onOrderChange(e.target.value)}>
        <option value="">Select</option>
        <option value="name">Name</option>
        <option value="founded">Founded Year</option>
      </select>
    </div>
  );
}

export default StudiosOrder;
