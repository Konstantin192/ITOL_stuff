const JobBoard = () => {
    const companyName = "TechCorp";
    const jobCount = 69; // You can change this value to test different scenarios
	
    const getJobMessage = () => {
        // Implement this function
        // If jobCount is 0, return "No jobs to schedule today"
        // Otherwise, return "Jobs running today from bot: {jobCount}"
        return jobCount === 0 ? `No jobs to schedule today` : `Jobs running today from bot: ${jobCount}` // if else statement shorthand
    }

    return (
        <div>
        <h1>{companyName}</h1>
        <p>{getJobMessage()}</p>
        </div>
    );
}

export default JobBoard;