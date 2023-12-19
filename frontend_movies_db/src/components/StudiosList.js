import React, { useState, useEffect } from 'react';
import "./MovieList.css";


function StudiosList() {
  const [studios, setStudios] = useState([]);

  useEffect(() => {
    const fetchStudios = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/movies/studios/');
        const data = await response.json();
        setStudios(data);
      } catch (error) {
        console.error('Error fetching studios:', error);
      }
    };

    fetchStudios();
  }, []);

  return (
    <div className="movie-list">
      <h2>Studios</h2>
      <ul>
        {studios.map(studio => (
          <li key={studio.id}>
            {studio.name} - Founded: {studio.founded}
            {/* Add more studio details here if needed */}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default StudiosList;
