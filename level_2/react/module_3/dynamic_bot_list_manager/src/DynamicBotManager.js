import React, { useState } from 'react';

const DynamicBotManager = () => {
  const [bots, setBots] = useState([
    { id: '1', name: 'Email Bot', status: 'Active' },
    { id: '2', name: 'Data Bot', status: 'Inactive' }
  ]);

  const [newBot, setNewBot] = useState({ id: '', name: '', status: '' });

  const handleInputChange = (e) => {
    // Implement input change handler
    if (e.target.name === 'bot_id') {
        setNewBot({...newBot, id:e.target.value});
    }
    else if (e.target.name === 'bot_name') {
        setNewBot({...newBot, name:e.target.value});
    }
    else {
        setNewBot({...newBot, status:e.target.value});
    }
  };

  const addBotToList = () => {
    // Implement add bot functionality
    setBots([...bots, newBot]);
    setNewBot({id:"", name:"", status:""});
  };

  const deleteBot = (id) => {
    // Implement delete bot functionality
    setBots(bots.filter(bot => id !== bot.id));
  };

  return (
     <div className='dynamic-bot-manager'>
       <h1>Dynamic Bot Manager </h1>

      {/* Add input fields for new bot */}

      {/* Add button to add new bot */}

      {/* Display list of bots */}
       <ul>
        {bots.map(bot => 
        <li key={bot.id}>
            <strong>ID: </strong>{bot.id}, 
            <strong> Name: </strong>{bot.name}, 
            <strong> Status: </strong> {bot.status}
            <button onClick={()=>deleteBot(bot.id)}> Delete Bot</button>
        </li>)}
       </ul>
       {/* <input type="number" placeholder='Bot ID' value={newBot.id} onChange={((e) => setNewBot({...newBot, id:e.target.value}))} />
       <input type="text" placeholder='Bot Name' value={newBot.name} onChange={(e) => setNewBot({...newBot, name:e.target.value})}/>
       <input type="text" placeholder='Bot Status' value={newBot.status} onChange={(e) => setNewBot({...newBot, status:e.target.value})}/> */}
       <input type="number" placeholder='Bot ID' name='bot_id' value={newBot.id} onChange={handleInputChange} />
       <input type="text" placeholder='Bot Name' name='bot_name' value={newBot.name} onChange={handleInputChange}/>
       <input type="text" placeholder='Bot Status' name='bot_status' value={newBot.status} onChange={handleInputChange}/>
       <button onClick={()=>addBotToList()}>Add bot</button>
     </div>
  );
};

export default DynamicBotManager;