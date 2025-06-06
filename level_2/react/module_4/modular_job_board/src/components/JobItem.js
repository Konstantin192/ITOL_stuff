const JobItem = ({ job }) => {
  // Implement conditional rendering based on job status

  return (
    <div className={`job-item ${job.status}`}>
      <span>ID: {job.id}, Name: {job.name}, Status: {job.status}</span>
    </div>
  );
};

export default JobItem;