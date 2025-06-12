import React from 'react'

export default function JobStatus({ jobTitle, jobStatus, jobID, deleteJob, updateStatus }) {

  const handleChange = (e) => {
    updateStatus(jobID, e.target.value);
  }

  return (
    <div>
      {jobTitle} 
      <select className="job-status" value={jobStatus} onChange={handleChange}>
        <option value="Need to Start">Need to Start</option>
        <option value="In progress">In progress</option>
        <option value="Done">Done</option>
      </select> 
      <button onClick={() => deleteJob(jobID)}>Delete Job</button>
    </div>
  )
}
