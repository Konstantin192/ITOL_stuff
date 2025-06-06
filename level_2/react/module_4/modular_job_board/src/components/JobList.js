import JobItem from './JobItem';
import { useState } from 'react';


const JobList = ({ jobs }) => {

  const [show, setShow] = useState(true);

  return (
    <div className="job-list">
      <button onClick={() => setShow(!show)}>Toggle</button>
      <ul>
        {show && jobs.map(job => 
        <li key={job.id}>
            <JobItem job={job} />
        </li>)}
      </ul>
    </div>
  );
};

export default JobList;