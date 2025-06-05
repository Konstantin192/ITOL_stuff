import React, { useState } from 'react';

const BotListManager = () => {
  const [bots, setBots] = useState([
    { id: 1, name: "Email Extractor", status: "Running", task: "Extracting emails" },
    { id: 2, name: "Notification Sender", status: "Completed", task: "Sending notifications" },
    { id: 3, name: "Data Analyzer", status: "Stopped", task: "Analyzing data" }
  ]);

  const triggerJob = (bot_id) => {
    // Implement this function to change the status of the bot    
    setBots(bots.map(bot => {
        if (bot.id === bot_id) {
            return {id:bot.id, name:bot.name, status:"Running", task:bot.task};
        }
        else {
            return bot;
        }
    }));
  };

  const statusColour = (status) => {
    if(status === "Running") {
        return "green";
    }
    else if(status === "Stopped") {
        return "red";
    }
    else{
        return "black";
    }
  }

  return (
    <div className="bot-list-manager">
      <h1>Bot List Manager</h1>
      <ul>
        {bots.map(bot => 
        <li key={bot.id}>
            <strong>ID: </strong>{bot.id}, 
            <strong> Name: </strong>{bot.name}, 
            {/* <strong> Status: </strong> <span style={{color:"green"}}>{bot.status}</span> */}
            <strong> Status: </strong> <span style={{color:statusColour(bot.status)}}>{bot.status}</span>
            <button onClick={()=>triggerJob(bot.id)}> Trigger Job</button>
        </li>)}
      </ul>
    </div>
  );
};

export default BotListManager;