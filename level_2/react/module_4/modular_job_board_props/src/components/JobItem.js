import React from 'react';

const JobItem = ({ job, onDelete }) => {
  return (
    <div className={`job-item ${job.status}`}>
      {<span>ID: {job.id}, Name: {job.name}, Status: {job.status}</span>}
      <button onClick={() => onDelete(job.id)}>Delete Job</button>
    </div>
  );
};

export default JobItem;