import React, { useState, useEffect } from "react";
import MovieItem from "./MovieItem";
import MovieDetails from "./MovieDetails";
import SearchBar from "./SearchBar";
import Filter from "./Filter";
import Orders from "./Order"; // Import the Orders component
import "./MovieList.css";

function MovieList() {
  const [movies, setMovies] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");  // State to hold the search term
  const [filter, setFilter] = useState(""); // State for selected filter
  const [order, setOrder] = useState(""); // State for selected order

  useEffect(() => {
    const fetchMovies = async () => {
      let apiUrl = "http://127.0.0.1:8000/movies/movies/";
      let queryParts = [];
      if (searchTerm) {
        queryParts.push(`search=${encodeURIComponent(searchTerm)}`);
      }
      if (filter) {
        queryParts.push(`filter=${encodeURIComponent(filter)}`);
      }
      if (order) {
        queryParts.push(`ordering=${encodeURIComponent(order)}`);
      }
      if (queryParts.length) {
        apiUrl += `?${queryParts.join('&')}`;
      }

      try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        setMovies(data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchMovies();
  }, [searchTerm, filter, order]); // Depend on searchTerm, filter, and order

  const handleSearch = (term) => {
    setSelectedMovie(null);
    setSearchTerm(term);
  };

  const handleFilterChange = (selectedFilter) => {
    setFilter(selectedFilter);
  };

  const handleOrderChange = (selectedOrder) => {
    setOrder(selectedOrder); // Update the order state
  };

  const handleMovieClick = (movie) => {
    setSelectedMovie(movie);
  };

  return (
    <div>
      <SearchBar onSearch={handleSearch} />
      <Filter onFilterChange={handleFilterChange} />
      <Orders onOrderChange={handleOrderChange} /> {/* Add the order component */}
      <div className="movie-list">
        {selectedMovie ? (
          <MovieDetails movie={selectedMovie} />
        ) : (
          movies.map((movie) => (
            <MovieItem key={movie.id} movie={movie} onClick={handleMovieClick} />
          ))
        )}
      </div>
    </div>
  );
}

export default MovieList;
