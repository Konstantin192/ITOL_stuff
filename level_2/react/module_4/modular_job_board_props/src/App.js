import React, { useState } from 'react';
import JobList from './components/JobList';
import './App.css';


const App = () => {
  const [jobs, setJobs] = useState([
    { id: 1, name: 'Email Extractor', status: 'running' },
    { id: 2, name: 'Data Analyzer', status: 'completed' },
    { id: 3, name: 'Report Generator', status: 'running' }
  ]);

  const handleDeleteJob = (id) => {
    // Implement delete functionality
    setJobs(jobs.filter(job => id !== job.id));
  };

  return (
    <div className="app">
      <h1>Job Board</h1>
      <JobList jobs={jobs} onDeleteJob={handleDeleteJob} />
    </div>
  );
};

export default App;