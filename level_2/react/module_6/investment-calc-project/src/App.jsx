import './App.css'
import React, { useState } from 'react';
import Header from './components/Header';
import UserInput from './components/UserInput';
import OutputData from './components/OutputData';
import { generatepdf } from './util/generatereport';
import { calculateInvestmentResults } from './util/investments';

function App() {
  const [userInput, setUserInput] = useState({
    initialInvestment: 10000,
    annualInvestment: 1200,
    expectedReturn: 6,
    duration: 10
  });

  const validateYearInput = userInput.duration >= 1;

    const [results, setResults] = useState(null);

  const handleInputChange = (inputIdentifier, newValue) => {
    setUserInput(prevInput => ({
      ...prevInput,
      [inputIdentifier]: +newValue
    }));
  };

  const handleCalculate = () => {
    const calculatedResults = calculateInvestmentResults(userInput);
    setResults(calculatedResults);
  };

  const handleGeneratePDF = () => {
    console.log("test")
    if (results) {
      generatepdf({ ...userInput, results });
    }
  };

  return (
    <>
      <Header />
      <UserInput userInput={userInput} onInputChange={handleInputChange} handleCalculate={handleCalculate} />
      <button onClick={handleCalculate}>Calculate</button>
      <button onClick={() => handleGeneratePDF()}>Download PDF report</button>
      {!validateYearInput && <p className='errorMessage'>Years invested must be greater than 0</p>}
      {validateYearInput && <OutputData inputValue={userInput} />}
    </>
  );
}

export default App;
