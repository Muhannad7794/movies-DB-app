import React from 'react';
import Navbar from './components/Navbar'; // Importing Navbar
// import SearchBar from './components/SearchBar';
import MovieList from './components/MovieList';

function App() {
  return (
    <div>
      <Navbar /> {/* Using Navbar */}
      {/* Other components will go here */}
      {/* <SearchBar /> */}
      <MovieList />
    </div>
  );
}

export default App;
