import React from 'react';

const TicketInfo = ({ result, image, children }) => {
  return (
    <div className={`ticket-info ${result}`}>
      {children}
      <img src={image} alt="" />
    </div>
  );
};

export default TicketInfo;