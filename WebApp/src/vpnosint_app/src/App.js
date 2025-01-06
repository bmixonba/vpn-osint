import React, { useEffect, useState } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const LeafletMap = ({ locations }) => {
  const mapRef = React.useRef(null);

  useEffect(() => {
    const map = L.map(mapRef.current).setView([51.505, -0.09], 2);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors',
    }).addTo(map);

    locations.forEach(location => {
      L.marker([location.lat, location.lng]).addTo(map);
    });

    return () => map.remove();
  }, [locations]);

  return <div ref={mapRef} style={{ height: '500px', width: '100%' }} />;
};

function App() {
  const [locations, setLocations] = useState([]);

  useEffect(() => {
    fetch('/api/locations')
      .then(response => response.json())
      .then(data => setLocations(data));
  }, []);

  return (
    <div className="App">
      <h1>VPN OSINT - Geospatial View </h1>
      <LeafletMap locations={locations} />
    </div>
  );
}

export default App;
