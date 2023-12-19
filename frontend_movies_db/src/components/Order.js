import React from 'react';

function MovieOrder({ onOrderChange }) {
  const handleOrderChange = (event) => {
    onOrderChange(event.target.value); // Pass the selected order back to MovieList
  };

  return (
    <div>
      <label htmlFor="order">Order By:</label>
      <select name="order" id="order" onChange={handleOrderChange}>
        <option value="">Default</option>
        <option value="title">Title</option>
        <option value="release_year">Release Year</option>
        <option value="credits_score">IMDB Score</option>
        {/* Add other ordering options based on your backend */}
      </select>
    </div>
  );
}

export default MovieOrder;
