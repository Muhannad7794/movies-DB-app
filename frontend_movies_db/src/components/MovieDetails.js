import React from 'react';
import { useNavigate } from 'react-router-dom';
import './MovieDetails.css';

function MovieDetails({ movie }) {
  const navigate = useNavigate();

  React.useEffect(() => {
    document.body.style.backgroundImage = `url(${movie.poster_url})`;
    document.body.style.backgroundSize = 'cover';
    document.body.style.backgroundPosition = 'center';
    document.body.style.margin = '0';
    document.body.style.padding = '0';
    // Set a class or style on body for other adjustments as needed

    return () => {
      // Revert body styles when the component unmounts
      document.body.style.backgroundImage = '';
      document.body.style.backgroundSize = '';
      document.body.style.backgroundPosition = '';
      document.body.style.margin = '';
      document.body.style.padding = '';
    };
  }, [movie.poster_url]);

  const handleDirectorClick = () => {
    navigate(`/directors/${movie.director.id}`);
  };

  const handleStudioClick = () => {
    navigate(`/studios/${movie.studio.id}`);
  };


  // Add a style object for background image
  const detailsStyle = {
    backgroundImage: `url(${movie.poster_url})`,
    backgroundSize: "cover",
    backgroundPosition: "center",
    position: "relative",
  };


  return (
    <div className="movie-details" style={detailsStyle}>
      <div className="movie-details-overlay"></div>
      <div className="movie-details-content">
        <h2>{movie.title}</h2>
        <p>Genre: {movie.genre}</p>
        <p>Release Year: {movie.release_year}</p>
        <p onClick={handleDirectorClick} className="interactive-text">
          Director: {movie.director.director_name}
        </p>
        <p>IMDB Score: {movie.credits_score}</p>
        <p onClick={handleStudioClick} className="interactive-text">
          Production Studio: {movie.studio.name}
        </p>
      </div>
    </div>
  );
}

export default MovieDetails;
