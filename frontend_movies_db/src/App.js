import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import MovieList from './components/MovieList';
import DirectorsList from './components/DirectorsList'; // You'll need to create this component
import StudiosList from './components/StudiosList'; // You'll need to create this component

function App() {
  return (
    <Router>
      <Navbar /> {/* Using Navbar */}
      <Routes>
        <Route path="/" element={<MovieList />} />
        <Route path="/directors" element={<DirectorsList />} /> {/* Directors route */}
        <Route path="/studios" element={<StudiosList />} /> {/* Studios route */}
      </Routes>
    </Router>
  );
}

export default App;
