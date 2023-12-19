import React from 'react';
import Navbar from './components/Navbar';
import MovieList from './components/MovieList';

function App() {
  return (
    <div>
      <Navbar /> {/* Using Navbar */}
      {/* Other components will go here */}
      <MovieList />
    </div>
  );
}

export default App;
