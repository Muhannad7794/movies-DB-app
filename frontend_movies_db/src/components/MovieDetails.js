import React from "react";
import { useNavigate } from "react-router-dom";
import "./MovieDetails.css";

function MovieDetails({ movie }) {
  const navigate = useNavigate();

  const handleDirectorClick = () => {
    navigate(`/directors/${movie.director.id}`);
  };

  const handleStudioClick = () => {
    navigate(`/studios/${movie.studio.id}`);
  };

  const detailsStyle = {
    backgroundImage: `url(${movie.poster_url})`,
    backgroundSize: "cover",
    backgroundPosition: "center",
    borderRadius: "15px", // Rounded corners for the image
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.5)", // Shadow for depth
    // Set height via aspect ratio here if needed
  };

  return (
    <div className="movie-details-container">
      <div className="movie-details-text">
        <h2>{movie.title}</h2>
        <p>Genre: {movie.genre}</p>
        <p>Release Year: {movie.release_year}</p>
        <p
          onClick={handleDirectorClick}
          className="interactive-text"
          id="director_click"
        >
          Director: {movie.director.director_name}
        </p>
        <p>IMDB Score: {movie.credits_score}</p>
        <p
          onClick={handleStudioClick}
          className="interactive-text"
          id="studio_click"
        >
          Production Studio: {movie.studio.name}
        </p>
      </div>
      <div className="movie-details-image" style={detailsStyle}>
        <img src={movie.poster_url} alt={movie.title} />
      </div>
    </div>
  );
}

export default MovieDetails;
