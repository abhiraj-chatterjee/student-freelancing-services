import React, { useState, useEffect } from 'react';
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
// import StudentRegister from './components/studentRegister';
// import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import './App.css';

function App() {
  // const [currentTime, setCurrentTime] = useState(0);

  // useEffect(() => {
  //   fetch('/time').then(res => res.json()).then(data => {
  //     setCurrentTime(data.time);
  //   });
  // }, []);

  return (
    <div className="intro">
      <div className="card mx-auto first-card">
        <div className="card-body">
          <h1 style={{fontFamily: "Times New Roman"}}>New Student</h1>
          <hr />
          <form>
            <div className="form-group">
              <label>Name</label>
              <input type="text" className="form-control" name="name" />
            </div>
            <div className="form-group">
              <label>Email Address</label>
              <input type="text" className="form-control" name="email" />
            </div>
            <div className="form-group">
              <label>Password</label>
              <input type="password" className="form-control" name="password" />
            </div>
            <div className="form-group">
              <label>Confirm Password</label>
              <input type="password" className="form-control" name="password2" />
            </div>
            <div className="form-group">
              <label>University</label>
              <input type="text" className="form-control" name="college" />
            </div>
            <div className="form-group">
              <label>Address</label>
              <input type="text" className="form-control" name="address" />
            </div>
            <div className="form-group">
              <label>Phone</label>
              <input type="text" className="form-control" name="phone" />
            </div>
            <button type="submit" className="btn btn-primary float-right">Sign Up</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default App;
