import React from 'react';

const JobCounter = () => {
//   let jobCount = 0;
  let [jobCount, setJobCount] = React.useState(0);

  const handleAddJob = () => {
    // Implement this function
    // It should increment jobCount and log the new value to the console
    jobCount++;
    console.log(jobCount);
    setJobCount(jobCount++);
  }

  return (
    <div>
      <h1>Job Counter</h1>
      <p>Current Jobs: {jobCount}</p>
      <button onClick={handleAddJob}>Add Job</button>
    </div>
  );
};

export default JobCounter;