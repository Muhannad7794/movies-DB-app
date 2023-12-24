import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import DirectorDetails from "./components/DirectorDetails";
import StudioDetails from "./components/StudioDetails";
import Navbar from "./components/Navbar";
import MovieList from "./components/MovieList";
import DirectorsList from "./components/DirectorsList";
import StudiosList from "./components/StudiosList";
import SearchBar from "./components/SearchBar";

function App() {
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = (term) => {
    setSearchTerm(term);
  };

  return (
    <Router>
      <Navbar /> {/* Using Navbar */}
      <SearchBar onSearch={handleSearch} />
      <Routes>
        <Route path="/" element={<MovieList searchTerm={searchTerm} />} />
        <Route
          path="/directors"
          element={<DirectorsList searchTerm={searchTerm} />}
        />
        <Route
          path="/studios"
          element={<StudiosList searchTerm={searchTerm} />}
        />
        <Route path="/directors/:directorId" element={<DirectorDetails />} />
        <Route path="/studios/:studioId" element={<StudioDetails />} />
      </Routes>
    </Router>
  );
}

export default App;
