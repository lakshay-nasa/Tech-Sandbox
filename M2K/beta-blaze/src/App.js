import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <img src="https://move2kube.konveyor.io/assets/images/move2kube.png" className="App-logo" alt="m2k-logo" />
        <p>
          BetaBlaze
        </p>
        <a
          className="App-link"
          href="https://konveyor.io/move2kube"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn Move2Kube
        </a>
      </header>
    </div>
  );
}

export default App;
