import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./DirectorDetails.css";
import "./DirectorsList.css";

function DirectorDetails({ directorProp }) {
  const { directorId } = useParams();
  const [director, setDirector] = useState(directorProp);

  const pictureStyle = {
    backgroundImage: director && director.picture_url ? `url(${director.picture_url})` : 'none',
    backgroundSize: "cover",
    backgroundPosition: "center",
    borderRadius: "15px", // Rounded corners for the image
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.5)", // Shadow for depth
    // Set height via aspect ratio here if needed
  };

  useEffect(() => {
    if (!directorProp && directorId) {
      fetch(`http://127.0.0.1:8000/movies/directors/${directorId}`)
        .then((response) => response.json())
        .then((data) => setDirector(data))
        .catch((error) => console.error("Error:", error));
    }
  }, [directorId, directorProp]);

  if (!director) {
    return <div>Loading...</div>;
  }

  return (
    <div className="directors-list">
      <div className="director-details-container">
        <div className="director-details-text">
          <h2>{director.director_name}</h2>
          <p>Nationality: {director.nationality}</p>
          <p>Date of Birth: {director.director_date_of_birth}</p>
          <p>Best Movies: {director.director_best_movies}</p>
          <p>Awards: {director.awards}</p>
          
        </div>
        <div className="director-details-image" style={pictureStyle}>
          {director.picture_url && (
            <img src={director.picture_url} alt={director.director_name} />
          )}
        </div>
      </div>
    </div>
    
  );
}

export default DirectorDetails;
