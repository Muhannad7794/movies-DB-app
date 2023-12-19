import React from 'react';

function MovieFilter({ onFilterChange }) {
  const handleFilterChange = (event) => {
    // Call the onFilterChange function passed from MovieList with the selected filter value
    onFilterChange(event.target.value);
  };

  return (
    <div>
      {/* Example filter: Genre */}
      <label htmlFor="genre">Genre:</label>
      <select name="genre" id="genre" onChange={handleFilterChange}>
        <option value="">All</option>
        {/* Populate options based on available genres */}
        <option value="Action">Action</option>
        <option value="Adventure">Adventure</option>
        <option value="Comedy">Comedy</option>
        <option value="Children">Children</option>
        <option value="Drama">Drama</option>
        <option value="Horror">Horror</option>
        <option value="Sci-Fi">Sci-Fi</option>
        <option value="Romance">Romance</option>
        <option value="Music">Music</option>
        <option value="Fantasy">Fantasy</option>
        <option value="War">War</option>
        <option value="Crime">Crime</option>
        <option value="Thriller">Thriller</option>
        <option value="Mystery">Mystery</option>
        <option value="Western">Western</option>
        <option value="Animation">Animation</option>
        <option value="Action">Action</option>
        <option value="Biography">Biography</option>
        <option value="History">History</option>
        <option value="Family">Family</option>

        
        </select>

    </div>
  );
}

export default MovieFilter;
