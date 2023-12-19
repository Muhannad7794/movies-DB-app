import React from 'react';
import './MovieItem.css';

function StudioItem({ studio, onClick }) {
  return (
    <div className="movie-item" onClick={() => onClick(studio)}>
      <h3>{studio.name}</h3>
      {/* Include other studio details you wish to display */}
    </div>
  );
}

export default StudioItem;
