import React, { useState } from 'react';
import './SearchBar.css'; // Import the CSS

function SearchBar({ onSearch }) { // Add the onSearch prop
    const [searchTerm, setSearchTerm] = useState('');

    const handleSearch = (event) => {
        event.preventDefault();
        onSearch(searchTerm); // Use the onSearch function passed from MovieList
    };

    return (
        <div className="search-bar-container">
            <form onSubmit={handleSearch}>
                <input
                    className="search-bar"
                    type="text"
                    placeholder="Search"
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                />
                <button className="search-button" type="submit">Search</button>
            </form>
        </div>
    );
}

export default SearchBar;
