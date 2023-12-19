import React from 'react';
import './MovieItem.css';

function MovieItem({ movie, onClick }) {
  return (
    
    <div className="movie-item" onClick={() => onClick(movie)}> 
      <h3>{movie.title}</h3>
      {/* Include other movie details you wish to display */}
    </div>
  );
}

export default MovieItem;
