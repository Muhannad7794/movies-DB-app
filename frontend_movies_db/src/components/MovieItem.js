import React from 'react';
import './MovieItem.css';

function MovieItem({ movie, onClick }) {
  return (
    // Apply the CSS class to this div
    <div className="movie-item" onClick={() => onClick(movie)}> 
      <h3>{movie.title}</h3>
      {/* Include other movie details you wish to display */}
    </div>
  );
}

export default MovieItem;
