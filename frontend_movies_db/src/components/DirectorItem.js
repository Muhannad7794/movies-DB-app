import React from 'react';
import './MovieItem.css';

function DirectorItem({ director, onClick }) {
  return (
    <div className="movie-item" onClick={() => onClick(director)}>
      <h3>{director.director_name}</h3>
      {/* Include other director details you wish to display */}
    </div>
  );
}

export default DirectorItem;
