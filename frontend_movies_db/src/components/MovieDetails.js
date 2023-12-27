import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./MovieDetails.css";
import "./MovieList.css";

function MovieDetails({ movie }) {
  const [recommendations, setRecommendations] = useState([]);
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

  const fetchRecommendations = async (movieId) => {
    try {
      const response = await fetch(
        `http://localhost:8000/movies/movies/${movieId}/recommendations/`
      );
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return await response.json();
    } catch (error) {
      console.error("Fetch error:", error);
      return null;
    }
  };

  useEffect(() => {
    if (movie.id) {
      fetchRecommendations(movie.id).then((data) => {
        if (data && data.results) {
          setRecommendations(data.results);
        }
      });
    }
  }, [movie.id]);

  return (
    <div className="movie-details-page">
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
      <div className="recommendations-section">
        <h3>Similar Movies</h3>
        <div className="recommendations-list">
          {recommendations.map((recMovie) => (
            <div className="recommendation-item" key={recMovie.id}>
              <h4>{recMovie.title}</h4>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default MovieDetails;
