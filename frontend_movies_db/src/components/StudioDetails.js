import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./MovieDetails.css";
import "./MovieList.css";

function StudioDetails({ studioProp }) {
  const { studioId } = useParams();
  const [studio, setStudio] = useState(studioProp);

  useEffect(() => {
    if (!studioProp && studioId) {
      fetch(`http://127.0.0.1:8000/movies/studios/${studioId}`)
        .then((response) => response.json())
        .then((data) => setStudio(data))
        .catch((error) => console.error("Error:", error));
    }
  }, [studioId, studioProp]);

  if (!studio) {
    return <div>Loading...</div>;
  }

  return (
    <div className="movie-list">
      <div className="movie-details-container">
        <div className="movie-details-text">
          <h2>{studio.name}</h2>
          <p>Founded: {studio.founded}</p>
          <p>Location: {studio.location}</p>
        </div>
      </div>
    </div>
  );
}

export default StudioDetails;
