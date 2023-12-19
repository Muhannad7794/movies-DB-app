import React from 'react';
import './MovieDetails.css';

function MovieDetails({ movie }) {
  return (
    <div className="movie-details">
      <h2>{movie.title}</h2>
      {/* Display other movie details here */}
      <p>Genre: {movie.genre}</p>
      <p>Release Year: {movie.release_year}</p>
      <p>Director: {movie.director}</p>
      <p>IMDB Score: {movie.credits_score}</p>
      

      {/* Add more details as needed */}
    </div>
  );
}

export default MovieDetails;
