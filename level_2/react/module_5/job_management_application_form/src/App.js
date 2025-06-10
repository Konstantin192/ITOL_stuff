import React, { useState } from 'react';
import JobColumn from './components/JobColumn';
import toDoIcon from './images/to-do-icon.png';
import inProgressIcon from './images/in-progress-icon.png';
import doneIcon from './images/done-icon.png';
import './App.css'

const App = () => {

  const [jobs, setJobs] = useState([
    { id: 1, title: 'Do the thing', status: 'Need to Start' },
    { id: 2, title: 'Do the other thing', status: 'In progress' },
    { id: 3, title: 'Do that thing', status: 'Done' }
  ]);

  const filterJobs = (column_status) => {
    return (jobs.filter(job => job.status === column_status));
  };

  return (
    <div className="app">
      {/* Other components */}
      <div className="job-columns">
        <JobColumn title="Need to Start" image={toDoIcon} alt="To-do icon" job_list={filterJobs("Need to Start")} />
        <JobColumn title="In progress" image={inProgressIcon} alt="In progress icon" job_list={filterJobs("In progress")}/>
        <JobColumn title="Done" image={doneIcon} alt="Done icon" job_list={filterJobs("Done")}/>
      </div>
    </div>
  );
};

export default App;