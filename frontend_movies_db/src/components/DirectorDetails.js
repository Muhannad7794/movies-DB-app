import React from 'react';
import './MovieDetails.css';

function DirectorDetails({ director }) {
  return (
    <div className="movie-details">
      <h2>{director.director_name}</h2>
      {/* Display other director details here */}
      <p>Nationality: {director.nationality}</p>
      <p>Date of Birth: {director.director_date_of_birth}</p>
      <p>Best Movies: {director.director_best_movies}</p>
      <p>Awards: {director.awards}</p>

      {/* Add more details as needed */}
    </div>
  );
}

export default DirectorDetails;
