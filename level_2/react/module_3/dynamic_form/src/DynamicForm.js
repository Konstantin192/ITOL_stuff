import React, { useState } from 'react';

const DynamicForm = () => {
  // Initialize state here
  const [input, setInput] = React.useState("");
  const [charCount, setCharCount] = React.useState(0);

  const handleInputChange = (event) => {
    // Update state based on input change
    setInput(event.target.value);
    console.log(input);
    setCharCount(event.target.value.length);
  };

  const handleReset = () => {
    // Reset the input value
    setInput("");
    setCharCount(0);
  };

  return (
    <div>
      <h1>Dynamic Form</h1>
      <input
        type="text"
        value={input}
        onChange={handleInputChange}
        placeholder="Type something..."
      />
      <button onClick={handleReset}>Reset</button>
      <div>
        <h2>Current Input:</h2>
        <p>{input}</p>
        <h2>Character count: {charCount}</h2>
      </div>
    </div>
  );
};

export default DynamicForm;