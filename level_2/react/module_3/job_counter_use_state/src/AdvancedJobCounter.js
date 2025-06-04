import React, { useCallback } from 'react';

const AdvancedJobCounter = () => {
  let [jobCount, setJobCount] = React.useState(0);
  let [jobMessage, setJobMessage] = React.useState("No jobs available");

//   const handleAddJob = () => {
//     jobCount++; // If I dont add this the button requires 2 clicks to increment by 1
//     setJobCount(jobCount++);
//   };

//   const handleRemoveJob = () => {
//     jobCount--; // If I dont add this the button requires 2 clicks to decrement by 1
//     setJobCount(jobCount--);
//   };

  // In addition to the above comments on weird behaviour. Every 2nd click of the add or remove buttons the state change is ignored for some reason.
  // E.g. if on the 2nd click the add button is pressed but on the 3rd click the decrement button is pressed the total change of the counter will be -1, not 0.
  // Further tested by trying a console log in both functions, it is activated on each press so it seems only the state change has this weird behaviour.
  // FIXED? It appears that this problem happens only when using the shorthand incrementation / decrementation e.g. it is not present when doing setJobCount(jobCount + 1).

  const handleAddJob = () => {
    setJobCount(jobCount + 1);
    jobCount++;
    changeJobMessage();
  };

  const handleRemoveJob = () => {
    setJobCount(jobCount - 1);
    jobCount--;
    changeJobMessage();
  };

  const handleResetJobs = () => {
    setJobCount(0);
    jobCount = 0;
    changeJobMessage();
  };

  const changeJobMessage = () => {
    if (jobCount === 0) {
        setJobMessage("No jobs available");
    }
    else if(jobCount > 0 && jobCount <= 5) {
        setJobMessage("Few jobs available");
    }
    else if (jobCount > 5){
        setJobMessage("Many jobs available");
    }
  }; 


//   const changeJobMessage = useCallback(() => {
//     if (jobCount === 0) {
//         setJobMessage("No jobs available");
//     }
//     else if(jobCount > 0 && jobCount <= 5) {
//         setJobMessage("Few jobs available");
//     }
//     else if (jobCount > 5){
//         setJobMessage("Many jobs available");
//     }
//   }, [jobCount]); 

// Same two click issue with this code block
//   const changeJobMessage = () => {
//     if (jobCount === 0) {
//         setJobMessage("No jobs available");
//     }
//     else if(jobCount > 0 && jobCount <= 5) {
//         setJobMessage("Few jobs available");
//     }
//     else if (jobCount > 5){
//         setJobMessage("Many jobs available");
//     }
//   }

  return (
    <div>
      <h1>Advanced Job Counter</h1>
      {/* Display current job count */}
      <p>Current Jobs: {jobCount}</p>
      
      {/* Add buttons for each action */}
      <button onClick={handleAddJob}>Add job</button>
      <button onClick={handleRemoveJob}>Remove job</button>
      <button onClick={handleResetJobs}>Reset jobs</button>
      
      {/* Display different messages based on job count */}
      <h1>{jobMessage}</h1>
    </div>
  );
};

export default AdvancedJobCounter;