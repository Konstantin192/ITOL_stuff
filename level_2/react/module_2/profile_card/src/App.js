import profile_picture from './profile_picture.jpg';
import ProfileCard from './Profile_card';

const App = () => {
  const profiles = [
    {
      image: "https://example.com/image1.jpg",
      name: "John Doe",
      jobTitle: "Frontend Developer",
      bio: "Passionate about creating user-friendly web applications."
    },
    {
      image: profile_picture,
      name: "Moon Moon",
      jobTitle: "Headpat collector",
      bio: "Collects head pats."
    },
    {
      image: profile_picture,
      name: "Noom Noom",
      jobTitle: "Impersonator",
      bio: "MoonMoon's twin."
    }
  ];

  return (
    <div className="app">
      <h1>Team Profiles</h1>
      {/* {profiles.map(profiles, profile => ProfileCard(profile.image, profile.name, profile.jobTitle, profile.bio))} */}

      {/* {profiles.map((profile) => ({ProfileCard(profile.image, pro)}))} */}
      
      {/* {profiles.map(profile => (
        <ul>{ProfileCard(profile.image, profile.name, profile.jobTitle, profile.bio)}</ul>
      ))} */}


      {profiles.map(profile => (
        <ProfileCard image={profile.image} name={profile.name} jobTitle={profile.jobTitle} bio={profile.bio}/>
      ))}


    </div>
  );
};

export default App;