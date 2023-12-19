import React from 'react';
import './MovieDetails.css';

function MovieDetails({ movie }) {
  return (
    <div className="movie-details">
      <h2>{movie.title}</h2>
      {/* Display other movie details here */}
      <p>Genre: {movie.genre}</p>
      <p>Release Year: {movie.release_year}</p>
      <p>Director: {movie.director.director_name}</p>
      <p>IMDB Score: {movie.credits_score}</p>
      <p>Production Studio: {movie.studio.name}</p>
      

      {/* Add more details as needed */}
    </div>
  );
}

export default MovieDetails;
