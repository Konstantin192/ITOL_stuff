import React from 'react';
import JobItem from './JobItem';

const JobList = ({ jobs, onDeleteJob }) => {
  return (
    <div className="job-list">
      {<ul>
        {jobs.map(job => 
        <li key={job.id}>
            <JobItem job={job} onDelete={onDeleteJob} />
        </li>)}
      </ul>}
    </div>
  );
};

export default JobList;