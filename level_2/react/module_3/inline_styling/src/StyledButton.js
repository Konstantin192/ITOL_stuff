const StyledButton = () => {
  let isDisabled = Math.floor(Math.random() * 2) === 0 ? false : true;
  const headingStyle = {
    textAlign:'center',
    color:'red',
    backgroundColor: 'green'
  }
  const buttonStyle = {
    color:'blue',
    padding: '5%',
    backgroundColor: 'green',
    borderStyle: 'dashed',
    borderWidth: 'thick',
    borderRadius: '10%'
  }

  return (
    <div>
      <h1 style={headingStyle}>Some text</h1>
      <button className='buttonClass' style={buttonStyle} disabled={isDisabled} /*disabled={true}*/>Some text</button>
    </div>
  );
};

export default StyledButton;