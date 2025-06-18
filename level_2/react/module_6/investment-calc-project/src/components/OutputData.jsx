import React from 'react';
import { calculateInvestmentResults, formatter } from '../util/investments';
// import './OutputData.css'

const OutputData = ({ inputValue }) => {
    const resultData = calculateInvestmentResults(inputValue);

    return (
        <table id="result">
            <thead>
                <tr>
                    <th>Year</th>
                    <th>Investment Value</th>
                    <th>Interest (Year)</th>
                    <th>Total Interest</th>
                    <th>Invested Capital</th>
                </tr>
            </thead>
            <tbody>
                {resultData.map((yearData) => {
                    return (
                        <tr key={yearData.year}>
                            <td>{yearData.year}</td>
                            <td>{formatter.format(yearData.investmentValue)}</td>
                            <td>{formatter.format(yearData.interest)}</td>
                            <td>{formatter.format(yearData.totalInterest)}</td>
                            <td>{formatter.format(yearData.investedCapital)}</td>
                        </tr>
                    );
                })}
            </tbody>
        </table>
    );
};

export default OutputData;