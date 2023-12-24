import React from "react";
import "./MovieItem.css";

function MovieItem({ movie, onClick }) {
  // Add a style object for background image
  const style = {
    backgroundImage: `url(${movie.poster_url})`,
    backgroundSize: "cover",
    backgroundPosition: "center",
  };

  return (
    <div className="movie-item" style={style} onClick={() => onClick(movie)}>
      <h3>{movie.title}</h3>
      {/* Include other movie details you wish to display */}
    </div>
  );
}

export default MovieItem;
