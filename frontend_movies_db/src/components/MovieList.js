import React, { useState, useEffect } from "react";
import MovieItem from "./MovieItem";
import MovieDetails from "./MovieDetails";
import Orders from "./Order"; 
import "./MovieList.css";

function MovieList({ searchTerm }) { // Receive searchTerm as a prop
  const [movies, setMovies] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState(null);
  const [order, setOrder] = useState(""); // State for selected order

  useEffect(() => {
    const fetchMovies = async () => {
      let apiUrl = "http://127.0.0.1:8000/movies/movies/";
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
        setMovies(data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchMovies();
  }, [searchTerm, order]); // Depend on searchTerm and order

  const handleOrderChange = (selectedOrder) => {
    setOrder(selectedOrder); // Update the order state
  };

  const handleMovieClick = (movie) => {
    setSelectedMovie(movie);
  };

  return (
    <div>
      <Orders onOrderChange={handleOrderChange} /> {/* Add the order component */}
      <div className="movie-list">
        {selectedMovie ? (
          <MovieDetails movie={selectedMovie} />
        ) : (
          movies.map((movie) => (
            <MovieItem
              key={movie.id}
              movie={movie}
              onClick={handleMovieClick}
            />
          ))
        )}
      </div>
    </div>
  );
}

export default MovieList;
