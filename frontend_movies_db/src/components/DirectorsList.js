import React, { useState, useEffect } from 'react';
import DirectorItem from './DirectorItem';
import DirectorDetails from './DirectorDetails'; // Import the DirectorDetails component
import "./MovieList.css"; // Assuming you're using the same CSS as for MovieList

function DirectorsList() {
  const [directors, setDirectors] = useState([]);
  const [selectedDirector, setSelectedDirector] = useState(null); // State to track the selected director

  useEffect(() => {
    const fetchDirectors = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/movies/directors/');
        const data = await response.json();
        setDirectors(data);
      } catch (error) {
        console.error('Error fetching directors:', error);
      }
    };

    fetchDirectors();
  }, []);

  const handleDirectorClick = (director) => {
    setSelectedDirector(director); // Update the selected director state
  };

  return (
    <div className="movie-list">
      <h2>Directors</h2>
      {selectedDirector ? (
        <DirectorDetails director={selectedDirector} /> // Display details of the selected director
      ) : (
        directors.map(director => (
          <DirectorItem 
            key={director.id} 
            director={director} 
            onClick={() => handleDirectorClick(director)} 
          />
        ))
      )}
    </div>
  );
}

export default DirectorsList;
