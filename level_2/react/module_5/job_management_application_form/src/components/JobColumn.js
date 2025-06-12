import React from 'react';
import './JobColumn.css';
import JobStatus from './JobStatus';

const JobColumn = ({ columnTitle, image, alt, job_list, delete_Job, update_status }) => {
  return (
    <div className="job-column">
      <h2 className="heading-status">
        {columnTitle}
        <img src={image} alt={alt} className="status-image" />
      </h2>
      <div className="job-list">
        {<ul>
            {job_list.map(job => 
            <li key={job.id}>
                <JobStatus jobTitle = {job.title} jobStatus={columnTitle} jobID={job.id} deleteJob={delete_Job} updateStatus={update_status} />
            </li>)}
        </ul>}
      </div>
    </div>
  );
};

export default JobColumn;