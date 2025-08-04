import { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

function AttendanceDashboard() {
  const [view, setView] = useState('loading');
  const [attendance, setAttendance] = useState([]);
  const [students, setStudents] = useState([]);
  const [formData, setFormData] = useState({});
  const [selectedDate, setSelectedDate] = useState(new Date().toISOString().split('T')[0]);

  const userRole = localStorage.getItem('role');
  const token = localStorage.getItem('access');

  useEffect(() => {
    const fetchData = async () => {
      try {
        if (userRole === 'student') {
          const res = await axios.get('http://127.0.0.1:8000/api/attendance/my/', {
            headers: { 'Authorization': `Bearer ${token}` }
          });
          setAttendance(res.data);
          setView('student');
        } else {
          const res = await axios.get('http://127.0.0.1:8000/api/classes/students/', {
            headers: { 'Authorization': `Bearer ${token}` }
          });
          setStudents(res.data);
          const initialData = {};
          res.data.forEach(s => initialData[s.id] = 'present');
          setFormData(initialData);
          setView('faculty');
        }
      } catch (err) {
        console.error("Failed to load data", err);
        setView('error');
      }
    };

    fetchData();
  }, [userRole, token]);

  const handleStatusChange = (studentId, status) => {
    setFormData(prev => ({ ...prev, [studentId]: status }));
  };

  const handleSubmit = async () => {
  const today = selectedDate;
  const cellId = 1; // Replace with real timetable cell ID

  const payload = Object.keys(formData).map(studentId => ({
    student: parseInt(studentId),
    cell: cellId,
    status: formData[studentId],
    date: today
  }));

  try {
    const response = await axios.post(
      'http://127.0.0.1:8000/api/attendance/mark/',
      payload,
      {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
      }
    );

    if (response.data.created?.length) {
      alert(`Attendance marked for ${response.data.created.length} students!`);
    }
    if (response.data.errors.length) {
      console.error("Failed to mark for some students", response.data.errors);
    }
  } catch (err) {
    console.error("API Error", err.response?.data || err.message);
    alert('Failed to save attendance. Check console.');
  }
};

  // Calculate stats for student
  const total = attendance.length;
  const present = attendance.filter(a => a.status === 'present').length;
  const absent = total - present;
  const percentage = total ? ((present / total) * 100).toFixed(1) : 0;

  const barData = [{ name: 'Present', value: present }, { name: 'Absent', value: absent }];
  const pieData = [
    { name: 'Present', value: present, fill: '#10B981' },
    { name: 'Absent', value: absent, fill: '#EF4444' }
  ];

  if (view === 'loading') return <p>Loading attendance data...</p>;
  if (view === 'error') return <p>Failed to load attendance.</p>;

  return (
    <div>
      {userRole === 'student' && (
        <div className="attendance-page">
          <h2>📊 Your Attendance</h2>
          <div className="attendance-stats">
            <div>Total: {total}</div>
            <div>Present: {present}</div>
            <div>Absent: {absent}</div>
            <div className="percentage">Attendance: <strong>{percentage}%</strong></div>
          </div>

          <div className="charts">
            <div className="chart">
              <h3>Bar Chart</h3>
              <ResponsiveContainer width="100%" height={200}>
                <BarChart data={barData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="value" fill="#3b82f6" />
                </BarChart>
              </ResponsiveContainer>
            </div>

            <div className="chart">
              <h3>Pie Chart</h3>
              <ResponsiveContainer width="100%" height={200}>
                <PieChart>
                  <Pie
                    data={pieData}
                    cx="50%"
                    cy="50%"
                    outerRadius={80}
                    fill="#8884d8"
                    dataKey="value"
                    label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                  >
                    {pieData.map((item, index) => (
                      <Cell key={`cell-${index}`} fill={item.fill} />
                    ))}
                  </Pie>
                </PieChart>
                <Tooltip />
              </ResponsiveContainer>
            </div>
          </div>
        </div>
      )}

      {userRole !== 'student' && (
        <div className="mark-attendance-form">
          <h3>📝 Mark Attendance</h3>
          <div style={{ marginBottom: '20px' }}>
            <label>Date: </label>
            <input
              type="date"
              value={selectedDate}
              onChange={(e) => setSelectedDate(e.target.value)}
            />
          </div>

          <p>Select status for each student:</p>
          {students.length === 0 ? (
            <p>No students found in your classes.</p>
          ) : (
            students.map(student => (
              <div className="student-row" key={student.id}>
                <div className="student-name">{student.name}</div>
                <select
                  className="status-select"
                  value={formData[student.id] || 'present'}
                  onChange={(e) => handleStatusChange(student.id, e.target.value)}
                >
                  <option value="present">Present</option>
                  <option value="absent">Absent</option>
                  <option value="late">Late</option>
                </select>
              </div>
            ))
          )}

          <button className="save-btn" onClick={handleSubmit}>
            Save Attendance
          </button>
        </div>
      )}
    </div>
  );
}

export default AttendanceDashboard;