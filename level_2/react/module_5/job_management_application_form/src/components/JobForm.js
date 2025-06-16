import React from 'react';
import './JobForm.css';
import { useRef, useState } from 'react';

const JobForm = ( {addNewJob} ) => {

  // const inputRef = useRef();

  const [inputValue, setInputValue] = useState("");

  const preventFormRefresh = (e) => {
    setInputValue("");
    e.preventDefault();
  }

  return (
    <div className="form-header">
      <form onSubmit={preventFormRefresh}>
        <input type="text" value={inputValue} className="bot-input" placeholder="Enter the job" /*ref={inputRef}*/ onChange={(e) => setInputValue(e.target.value)}/>
        <button className="submit-data" onClick={() => addNewJob(inputValue)}>Add Job</button>

        {/* <div className="form-details">
            <div className="bottom-line">
                <button className='tag'>Read Emails</button>
                <button className='tag'>Web Parsing</button>
                <button className='tag'>Send Emails</button>
            </div>
        </div>

        <select className="job-status">
            <option value="start">Start Process</option>
            <option value="running">Running</option>
            <option value="completed">Completed</option>
            <option value="stopped">Stopped</option>
        </select> */}
      </form>
      {/* <button className="submit-data" onClick={() => addNewJob(inputRef.current.value)}>Add Job</button> */}
    </div>
  );
};

export default JobForm;