import React, { useEffect, useRef } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const LeafletMap = ({ locations }) => {
  const mapRef = useRef(null);

  useEffect(() => {
    const map = L.map(mapRef.current).setView([51.505, -0.09], 2);

    // Use OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors',
    }).addTo(map);

    locations.forEach(location => {
      L.marker([location.lat, location.lng]).addTo(map);
    });

    return () => map.remove(); // Cleanup on unmount
  }, [locations]);

  return <div ref={mapRef} style={{ height: '500px', width: '100%' }} />;
};

export default LeafletMap;

