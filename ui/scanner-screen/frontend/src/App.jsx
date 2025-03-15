import {useState} from 'react';
import './App.css';
import {Greet} from "../wailsjs/go/main/App";
import Gradient from './components/gradient';
import Greeter from './components/greeter/greeter';

function App() {
    const [resultText, setResultText] = useState("Please enter your name below 👇");
    const [name, setName] = useState('');
    const updateName = (e) => setName(e.target.value);
    const updateResultText = (result) => setResultText(result);

    function greet() {
        Greet(name).then(updateResultText);
    }

    return (
        <div className="App">
            <Greeter/>
            <Gradient/>
        </div>
    )
}

export default App
