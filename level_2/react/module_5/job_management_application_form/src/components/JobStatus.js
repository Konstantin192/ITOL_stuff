import React from 'react'

export default function JobStatus({ jobTitle, jobID, deleteJob }) {
  return (
    <div>
      {jobTitle} <button>Update Job</button> <button onClick={() => deleteJob(jobID)}>Delete Job</button>
    </div>
  )
}
