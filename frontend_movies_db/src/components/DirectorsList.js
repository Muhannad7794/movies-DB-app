import React, { useState, useEffect } from 'react';
import DirectorItem from './DirectorItem';
import DirectorDetails from './DirectorDetails';
import DirectorsOrder from './DirectorsOrder';
import "./MovieList.css";

function DirectorsList({ searchTerm }) { // Receive searchTerm as a prop
  const [directors, setDirectors] = useState([]);
  const [selectedDirector, setSelectedDirector] = useState(null);
  const [order, setOrder] = useState(""); // State for selected order

  useEffect(() => {
    const fetchDirectors = async () => {
      let apiUrl = "http://127.0.0.1:8000/movies/directors/";
      let queryParts = [];
      if (searchTerm) {
        queryParts.push(`search=${encodeURIComponent(searchTerm)}`);
      }
      if (order) {
        queryParts.push(`ordering=${encodeURIComponent(order)}`);
      }
      if (queryParts.length) {
        apiUrl += `?${queryParts.join("&")}`;
      }

      try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        setDirectors(data);
      } catch (error) {
        console.error('Error fetching directors:', error);
      }
    };

    fetchDirectors();
  }, [searchTerm, order]); // Depend on searchTerm and order

  const handleDirectorClick = (director) => {
    setSelectedDirector(director); // Update the selected director state
  };

  const handleOrderChange = (selectedOrder) => {
    setOrder(selectedOrder); // Update the order state
  };

  return (
    <div className="movie-list">
      <DirectorsOrder onOrderChange={handleOrderChange} /> {/* Add the DirectorsOrder component */}
      <h2>Directors</h2>
      {selectedDirector ? (
        <DirectorDetails director={selectedDirector} />
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
