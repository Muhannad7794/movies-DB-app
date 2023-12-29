import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./StudioDetails.css";
import "./StudiosList.css";

function StudioDetails({ studioProp }) {
  const { studioId } = useParams();
  const [studio, setStudio] = useState(studioProp);

  const pictureStyle = {
    backgroundImage:
      studio && studio.picture_url ? `url(${studio.picture_url})` : "none",
    backgroundSize: "cover",
    backgroundPosition: "center",
    borderRadius: "15px", // Rounded corners for the image
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.5)", // Shadow for depth
    // Set height via aspect ratio here if needed
  };

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
    <div className="studios-list">
      <div className="studio-details-container">
        <div className="studio-details-text">
          <h2>{studio.name}</h2>
          <p>Founded: {studio.founded}</p>
          <p>Location: {studio.location}</p>
        </div>
        <div className="studio-details-image" style={pictureStyle}>
          {studio.picture_url && (
            <img src={studio.picture_url} alt={studio.director_name} />
          )}
        </div>
      </div>
    </div>
  );
}

export default StudioDetails;
