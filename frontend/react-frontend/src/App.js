import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  const build_version = process.env.REACT_APP_BUILD_VERSION || 'unknown';
  const build_version_test = process.env.REACT_APP_BUILD_VERSION_TEST || 'unknown';

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          current build: <code>{ build_version }</code>
        </p>
        <p>
          current build passed in: <code>{ build_version_test }</code>
        </p>
      </header>
    </div>
  );
}

export default App;
