import React, { useState, useEffect } from "react";
import StudioItem from "./StudioItem";
import StudioDetails from "./StudioDetails";
import StudiosOrder from "./StudiosOrder";
import "./StudiosList.css";

function StudiosList({ searchTerm }) {
  const [studios, setStudios] = useState([]);
  const [selectedStudio, setSelectedStudio] = useState(null);
  const [order, setOrder] = useState(""); // State for selected order

  useEffect(() => {
    const fetchStudios = async () => {
      let apiUrl = "http://127.0.0.1:8000/movies/studios/";
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
        setStudios(data);
      } catch (error) {
        console.error("Error fetching studios:", error);
      }
    };

    fetchStudios();
  }, [searchTerm, order]);

  const handleStudioClick = (studio) => {
    setSelectedStudio(studio);
  };

  const handleOrderChange = (selectedOrder) => {
    setOrder(selectedOrder);
  };

  return (
    <div>
      <StudiosOrder onOrderChange={handleOrderChange} />
      <div className="studios-list">
        {selectedStudio ? (
          <StudioDetails studioProp={selectedStudio} />
        ) : (
          studios.map((studio) => (
            <StudioItem
              key={studio.id}
              studio={studio}
              onClick={() => handleStudioClick(studio)}
            />
          ))
        )}
      </div>
    </div>
  );
}

export default StudiosList;
