import React from 'react';
import './JobColumn.css';

const JobColumn = ({ title, image, alt, job_list }) => {
  return (
    <div className="job-column">
      <h2 className="heading-status">
        {title}
        <img src={image} alt={alt} className="status-image" />
      </h2>
      <div className="job-list">
        {<ul>
            {job_list.map(job => 
            <li key={job.id}>
                {job.title}
            </li>)}
        </ul>}
      </div>
    </div>
  );
};

export default JobColumn;