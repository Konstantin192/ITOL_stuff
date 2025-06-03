// import profile_picture from './profile_picture.jpg';

const Profile_card = ({ image, name, jobTitle, bio }) => {
  return (
    <div className="profile-card">
      <img src={image} className="Profile_picture" alt="Profile picture"/>
      <h1>Name: {name}</h1>
      <h1>Title: {jobTitle}</h1>
      <p>Bio: {bio}</p>
    </div>
  );
};

export default Profile_card;
