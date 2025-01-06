import React, { useRef, useEffect } from 'react';
import { DataSet, Timeline } from 'vis-timeline/standalone';
import 'vis-timeline/styles/vis-timeline-graph2d.min.css';

const TimelineComponent = ({ events }) => {
  const timelineRef = useRef(null);

  useEffect(() => {
    const container = timelineRef.current;
    const items = new DataSet(events);

    const options = {
      width: '100%',
      height: '150px',
    };

    new Timeline(container, items, options);
  }, [events]);

  return <div ref={timelineRef}></div>;
};

export default TimelineComponent;

