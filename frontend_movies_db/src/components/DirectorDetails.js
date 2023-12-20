import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import './MovieDetails.css';

function DirectorDetails({ directorProp }) {
  const { directorId } = useParams();
  const [director, setDirector] = useState(directorProp);

  useEffect(() => {
    if (!directorProp && directorId) {
      fetch(`http://127.0.0.1:8000/movies/directors/${directorId}`)
        .then(response => response.json())
        .then(data => setDirector(data))
        .catch(error => console.error('Error:', error));
    }
  }, [directorId, directorProp]);

  if (!director) {
    return <div>Loading...</div>;
  }

  return (
    <div className="movie-details">
      <h2>{director.director_name}</h2>
      <p>Nationality: {director.nationality}</p>
      <p>Date of Birth: {director.director_date_of_birth}</p>
      <p>Best Movies: {director.director_best_movies}</p>
      <p>Awards: {director.awards}</p>
    </div>
  );
}

export default DirectorDetails;
