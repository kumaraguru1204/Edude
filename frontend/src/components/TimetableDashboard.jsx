import { useState, useEffect } from 'react';
import axios from 'axios';

function TimetableDashboard() {
  const [timetable, setTimetable] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedCell, setSelectedCell] = useState(null);
  const [feedback, setFeedback] = useState('');

  const userRole = localStorage.getItem('role');
  const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
  const periods = [1, 2, 3, 4, 5, 6];

  useEffect(() => {
    const fetchTimetable = async () => {
      try {
        const res = await axios.get('http://127.0.0.1:8000/api/timetable/?section=1');
        setTimetable(res.data);
      } catch (err) {
        console.error("Failed to load timetable");
      } finally {
        setLoading(false);
      }
    };
    fetchTimetable();
  }, []);

  const grouped = days.map(day => {
    const row = { day };
    periods.forEach(p => {
      row[p] = timetable.find(cell => cell.day === day && cell.period_number === p) || null;
    });
    return row;
  });

  const handleCellClick = (cell) => {
    if (!cell) return;
    setSelectedCell(cell);
  };

  const handleSubmitFeedback = () => {
    alert(`Feedback submitted for ${selectedCell.subject}`);
    setFeedback('');
    setSelectedCell(null);
  };

  return (
    <div>
      <h2>📅 Weekly Timetable</h2>
      {loading ? (
        <p>Loading timetable...</p>
      ) : (
        <table className="timetable-table">
          <thead>
            <tr>
              <th>Day</th>
              {periods.map(p => <th key={p}>Period {p}</th>)}
            </tr>
          </thead>
          <tbody>
            {grouped.map((row, idx) => (
              <tr key={idx}>
                <td className="day-cell">{row.day}</td>
                {periods.map(p => {
                  const cell = row[p];
                  return (
                    <td
                      key={p}
                      className={`timetable-cell ${cell ? 'clickable' : 'empty'}`}
                      onClick={() => handleCellClick(cell)}
                    >
                      {cell ? (
                        <div className="cell-content">
                          <strong>{cell.subject}</strong>
                          <small>{cell.classroom}</small>
                        </div>
                      ) : (
                        <span>—</span>
                      )}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {/* Modal */}
      {selectedCell && (
        <div className="modal-overlay" onClick={() => setSelectedCell(null)}>
          <div className="modal" onClick={e => e.stopPropagation()}>
            <h3>{selectedCell.subject}</h3>

            {userRole === 'student' && (
              <>
                <h4>📝 Provide Feedback</h4>
                <textarea
                  placeholder="Your feedback..."
                  value={feedback}
                  onChange={e => setFeedback(e.target.value)}
                  rows="4"
                />
                <div className="modal-actions">
                  <button onClick={() => setSelectedCell(null)}>Cancel</button>
                  <button onClick={handleSubmitFeedback}>Submit Feedback</button>
                </div>
              </>
            )}

            {userRole === 'faculty' && (
              <>
                <h4>👀 View Student Feedback</h4>
                <p>No feedback submitted yet.</p>
                <div className="modal-actions">
                  <button onClick={() => setSelectedCell(null)}>Close</button>
                </div>
              </>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default TimetableDashboard;