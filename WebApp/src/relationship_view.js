import React, { useEffect, useRef } from 'react';
import cytoscape from 'cytoscape';

const NetworkGraphComponent = ({ relationships }) => {
  const cyRef = useRef(null);

  useEffect(() => {
    const cy = cytoscape({
      container: cyRef.current,
      elements: relationships,
      style: [
        {
          selector: 'node',
          style: {
            'background-color': '#666',
            'label': 'data(label)'
          }
        },
        {
          selector: 'edge',
          style: {
            'width': 2,
            'line-color': '#ccc',
            'target-arrow-color': '#ccc',
            'target-arrow-shape': 'triangle'
          }
        }
      ],
      layout: {
        name: 'grid',
        rows: 1
      }
    });

    return () => cy.destroy(); // Cleanup when component unmounts
  }, [relationships]);

  return <div ref={cyRef} style={{ height: '500px', width: '100%' }} />;
};

export default NetworkGraphComponent;

