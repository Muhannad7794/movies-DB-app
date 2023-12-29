import React from "react";
import "./StudioItem.css";

function StudioItem({ studio, onClick }) {
  // Add a style object for background image
  const style = {
    backgroundImage: `url(${studio.picture_url})`,
    backgroundSize: "cover",
    backgroundPosition: "center",
  };
  return (
    <div className="studio-item" style={style} onClick={() => onClick(studio)}>
      <h3>{studio.name}</h3>
      {/* Include other studio details you wish to display */}
    </div>
  );
}

export default StudioItem;
