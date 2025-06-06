import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import Footer from './components/Footer';
import JobList from './components/JobList';

const App = () => {
  const jobs = [
    { id: 1, name: 'Email Extractor', status: 'Running' },
    { id: 2, name: 'Data Analyzer', status: 'Completed' },
    { id: 3, name: 'Report Generator', status: 'Running' }
  ];


  return (
    <div className="app">
      <Header />
      <JobList jobs={jobs} />
      <Footer />
    </div>
  );
};

export default App;
