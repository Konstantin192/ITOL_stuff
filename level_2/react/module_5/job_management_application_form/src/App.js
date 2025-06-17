import React, { useState, useEffect } from 'react';
import JobColumn from './components/JobColumn';
import toDoIcon from './images/to-do-icon.png';
import inProgressIcon from './images/in-progress-icon.png';
import doneIcon from './images/done-icon.png';
import './App.css'
import JobForm from './components/JobForm';

const App = () => {

  const [isFirstPageRender, setIsFirstPageRender] = useState(true);
  
  // const [jobs, setJobs] = useState([
  //   { id: 1, title: 'Do the thing', status: 'Need to Start' },
  //   { id: 2, title: 'Do the other thing', status: 'In progress' },
  //   { id: 3, title: 'Do that thing', status: 'Done' }
  // ]);

  const [jobs, setJobs] = useState(() => {
    const savedJobs = localStorage.getItem('jobs');
    return savedJobs ? JSON.parse(savedJobs) : [
      { id: 1, title: 'Do the thing', status: 'Need to Start' },
      { id: 2, title: 'Do the other thing', status: 'In progress' },
      { id: 3, title: 'Do that thing', status: 'Done' }
    ];
    
  });

  const [newJob, setNewJob] = useState({ id: -1, title: '', status: '' });

  const filterJobs = (column_status) => {
    return (jobs.filter(job => job.status === column_status));
  };

  const deleteJob = (id) => {
    setJobs(jobs.filter(job => id !== job.id));
  };

  const updateJobStatus = (id, newStatus) => {
    
    // setJobs(jobs.map(job => {
    //   if(job.id === id) {
    //     job.status = newStatus;
    //   }}
    // ));

    setJobs(jobs.map(job => (job.id === id ? {...job, status: newStatus} : job))); 
  };

  const addNewJob = (title) => {
    setNewJob({ id:newJobID(), title:title, status:'Need to Start' });
    // setJobs([...jobs, newJob]);
  };

  const newJobID = () => {
    let lastJob = jobs.slice(jobs.length - 1);
    let newJobID = lastJob[0].id + 1;

    return newJobID;
  }

  // IMPORTANT - Helps addNewJob function by avoiding batching of updates e.g the updates of the new job getting 
  // batched with the updates of the list and so the new job gets added to the job list before it has its details updated
  useEffect(() => {
    if(!isFirstPageRender) {
      setJobs(prevJobs => [...prevJobs, newJob]);
    }
    else {
      setIsFirstPageRender(false);
    }
  }, [newJob]);

  useEffect(() => {
    localStorage.setItem('jobs', JSON.stringify(jobs));
  }, [jobs])


  return (
    <div className="app">
      {/* Other components */}
      <JobForm addNewJob={addNewJob}/>
      <div className="job-columns">
        <JobColumn 
          columnTitle="Need to Start" 
          image={toDoIcon} alt="To-do icon" 
          job_list={filterJobs("Need to Start")} 
          delete_Job={deleteJob} 
          update_status={updateJobStatus}
        />
        <JobColumn 
          columnTitle="In progress" 
          image={inProgressIcon} 
          alt="In progress icon" 
          job_list={filterJobs("In progress")} 
          delete_Job={deleteJob}
          update_status={updateJobStatus}
        />
        <JobColumn 
          columnTitle="Done" 
          image={doneIcon} 
          alt="Done icon" 
          job_list={filterJobs("Done")} 
          delete_Job={deleteJob}
          update_status={updateJobStatus}
        />
      </div>
    </div>
  );
};

export default App;