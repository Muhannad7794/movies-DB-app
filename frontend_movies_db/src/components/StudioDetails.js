import React from 'react';
import './MovieDetails.css'; // You'll need to create this CSS file

function StudioDetails({ studio }) {
  return (
    <div className="movie-details">
      <h2>{studio.name}</h2>
      {/* Display other studio details here */}
      <p>Founded: {studio.founded}</p>
      <p>Location: {studio.location}</p>
      {/* Add more details as needed */}
    </div>
  );
}

export default StudioDetails;
