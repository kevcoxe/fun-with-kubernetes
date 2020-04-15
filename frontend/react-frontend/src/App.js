import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  const build_version = process.env.REACT_APP_BUILD_VERSION || 'unknown';

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          current build: <code>{ build_version }</code>
        </p>
      </header>
    </div>
  );
}

export default App;
