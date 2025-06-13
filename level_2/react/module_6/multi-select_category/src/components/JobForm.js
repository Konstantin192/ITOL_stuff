import React, { useState } from 'react';
import './JobForm.css'

const JobForm = () => {
  const [jobDetails, setJobDetails] = useState({
    title: '',
    status: 'To Start',
    categories: []
  });

  const categoryOptions = ['Read Emails', 'Web Parsing', 'Send Emails'];

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setJobDetails(prev => ({ ...prev, [name]: value }));
  };

  const handleCategoryToggle = (category) => {
    // Implement category toggle functionality
    if(jobDetails.categories.some(item => item === category)) {
        const filterCategory = jobDetails.categories.filter(item => item!== category);
        setJobDetails(prev => {
            return{...prev, categories:filterCategory}
        })
    }
    else {
        setJobDetails(prev => {
            return{...prev, categories:[...prev.categories, category]}
        })
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Submitted job details:', jobDetails);
  };

  const handleActiveCategory = (category) => {
    if(jobDetails.categories.some(item => item === category)) {
        return "categoryActive";
    }
    else {
        return "";
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="title"
        value={jobDetails.title}
        onChange={handleInputChange}
        placeholder="Enter job title"
      />
      
      <select
        name="status"
        value={jobDetails.status}
        onChange={handleInputChange}
      >
        <option value="To Start">To Start</option>
        <option value="In Progress">In Progress</option>
        <option value="Completed">Completed</option>
      </select>

      <div>
        {categoryOptions.map(category => (
          <button
            key={category}
            type="button"
            onClick={() => handleCategoryToggle(category)}
            // Add styling based on selection state
            className={handleActiveCategory(category)}
          >
            {category}
          </button>
        ))}
      </div>

      <ul>
        {jobDetails.categories.map(category =>
            <li key={category}>
                {category}
            </li>
        )}
      </ul>

      <button type="submit">Add Job</button>
    </form>
  );
};

export default JobForm;