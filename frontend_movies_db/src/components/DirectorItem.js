import React from "react";
import "./DirectorItem.css";

function DirectorItem({ director, onClick }) {
  // Add a style object for background image
  const style = {
    backgroundImage: `url(${director.picture_url})`,
    backgroundSize: "cover",
    backgroundPosition: "center",
  };
  return (
    <div className="movie-item" style={style} onClick={() => onClick(director)}>
      <h3>{director.director_name}</h3>
      {/* Include other director details you wish to display */}
    </div>
  );
}

export default DirectorItem;
