import React from "react";
import "./Order.css";
function MovieOrder({ onOrderChange }) {
  const handleOrderChange = (event) => {
    onOrderChange(event.target.value); // Pass the selected order back to MovieList
  };

  return (
    <div className="order-container ">
      <label htmlFor="order" className="order-label">
        Order By:
      </label>

      <select
        name="order"
        id="order"
        className="order-select"
        onChange={handleOrderChange}
      >
        <option value="">Default</option>
        <option value="title">Title</option>
        <option value="release_year">Release Year</option>
        <option value="credits_score">Credits Score</option>
        {/* Add other ordering options based on your backend */}
      </select>
    </div>
  );
}

export default MovieOrder;
