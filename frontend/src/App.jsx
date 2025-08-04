import { useState } from 'react';
import './App.css';
import axios from 'axios';
import TimetableDashboard from './components/TimetableDashboard';
import AttendanceDashboard from './components/AttendanceDashboard';
import ProfilePage from './components/ProfilePage';

function App() {
  const [view, setView] = useState('login');
  const [user, setUser] = useState(null);

  const handleLogin = async (e, username, password) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/token/', {
        username,
        password,
      });

      const { role } = response.data;
      localStorage.setItem('access', response.data.access);
      localStorage.setItem('refresh', response.data.refresh);
      localStorage.setItem('role', role);
      localStorage.setItem('username', username);

      setUser({ username, role });
      setView('dashboard');
    } catch (err) {
      alert('Invalid credentials');
    }
  };

  const handleLogout = () => {
    localStorage.clear();
    setUser(null);
    setView('login');
  };

  if (view === 'login') {
    let username = '';
    let password = '';
    return (
      <div className="app login-layout">
        <div className="login-container">
          <div className="login-card">
            <h1 className="app-title">EDUDE</h1>
            <p className="app-subtitle">Education Management System</p>

            <form onSubmit={(e) => handleLogin(e, username, password)}>
              <div className="form-group">
                <label>Username</label>
                <input
                  type="text"
                  onChange={(e) => (username = e.target.value)}
                  placeholder="Enter your username"
                  required
                />
              </div>
              <div className="form-group">
                <label>Password</label>
                <input
                  type="password"
                  onChange={(e) => (password = e.target.value)}
                  placeholder="Enter your password"
                  required
                />
              </div>
              <button type="submit" className="login-btn">
                Login
              </button>
            </form>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="app dashboard-layout">
      {/* Header */}
      <header className="main-header">
        <h1>🎓 Edude</h1>
        <div className="user-controls">
          <span className={`role-badge role-${user?.role}`}>{user?.role}</span>
          <button onClick={handleLogout} className="btn-logout">Logout</button>
        </div>
      </header>

      {/* Sidebar */}
      <nav className="sidebar">
        <ul>
          <li onClick={() => setView('dashboard')}>🏠 Dashboard</li>
          <li onClick={() => setView('timetable')}>📅 Timetable</li>
          <li onClick={() => setView('attendance')}>📊 Attendance</li>
          <li onClick={() => setView('profile')}>👤 Profile</li>
        </ul>
      </nav>

      {/* Main Content */}
      <main className="main-content">
        {view === 'dashboard' && (
          <div className="dashboard-grid">
            <div className="card" onClick={() => setView('timetable')}>
              <h3>📅 Timetable</h3>
              <p>View your weekly schedule</p>
            </div>
            <div className="card" onClick={() => setView('attendance')}>
              <h3>📊 Attendance</h3>
              <p>Check your attendance stats</p>
            </div>
            <div className="card" onClick={() => setView('profile')}>
              <h3>👤 Profile</h3>
              <p>View and edit your info</p>
            </div>
          </div>
        )}

        {view === 'timetable' && <TimetableDashboard />}
        {view === 'attendance' && <AttendanceDashboard />}
        {view === 'profile' && <ProfilePage />}
      </main>
    </div>
  );
}

export default App;