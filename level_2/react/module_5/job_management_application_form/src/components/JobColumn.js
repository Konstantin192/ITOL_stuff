import React from 'react';
import './JobColumn.css';
import JobStatus from './JobStatus';

const JobColumn = ({ title, image, alt, job_list, delete_Job }) => {
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
                <JobStatus jobTitle = {job.title} jobID={job.id} deleteJob={delete_Job} />
            </li>)}
        </ul>}
      </div>
    </div>
  );
};

export default JobColumn;