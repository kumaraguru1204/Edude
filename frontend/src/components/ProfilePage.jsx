function ProfilePage() {
  const user = {
    username: localStorage.getItem('username'),
    role: localStorage.getItem('role'),
    email: `${localStorage.getItem('username')}@edude.ac.in`,
  };

  return (
    <div>
      <h2>👤 My Profile</h2>
      <div style={{ background: 'white', padding: '30px', borderRadius: '12px', maxWidth: '500px', margin: '20px 0' }}>
        <p><strong>Username:</strong> {user.username}</p>
        <p><strong>Role:</strong> {user.role}</p>
        <p><strong>Email:</strong> {user.email}</p>
        <button style={{ marginTop: '20px', padding: '10px 20px', background: '#2563eb', color: 'white', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>
          Edit Profile
        </button>
      </div>
    </div>
  );
}

export default ProfilePage;