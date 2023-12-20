import React from 'react';
import { useNavigate } from 'react-router-dom';
import './MovieDetails.css';

function MovieDetails({ movie }) {
  const navigate = useNavigate();

  const handleDirectorClick = () => {
    navigate(`/directors/${movie.director.id}`); // Replace with correct ID if different
  };

  const handleStudioClick = () => {
    navigate(`/studios/${movie.studio.id}`); // Replace with correct ID if different
  };

  return (
    <div className="movie-details">
      <h2>{movie.title}</h2>
      <p>Genre: {movie.genre}</p>
      <p>Release Year: {movie.release_year}</p>
      <p onClick={handleDirectorClick} style={{ cursor: 'pointer' }}>Director: {movie.director.director_name}</p>
      <p>IMDB Score: {movie.credits_score}</p>
      <p onClick={handleStudioClick} style={{ cursor: 'pointer' }}>Production Studio: {movie.studio.name}</p>
    </div>
  );
}

export default MovieDetails;
