import logo from '../logo.svg';

const Header = () => {
  return (
    <header>
      <h1>Job Board</h1>
      <img src={logo} style={{width:'5%'}} alt="" />
    </header>
  );
};

export default Header;