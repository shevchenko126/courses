import logo from './logo.svg';
import './App.css';
import {courseObject,plusTwo} from './data/course'
import Header from './components/Header'
import MainBlock from './components/contentBlock/mainBlock'

const App = () => {

  const { courseName, courseTeacher } = courseObject

  const number = 2
  console.log( plusTwo(number) )
  
  const clickButtonFunction = () => {
    console.log('ssssssssssss')
  }

  return (

    <div className="App">
      <Header />
      { number > 3 ? (
          <div>
            sssss
          </div>
        ) : (
          <MainBlock clickButtonFunction={clickButtonFunction} content="Hello World!" number={number} display={true} color="green" />
        )
      }
      
      
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload. { courseName }
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React { courseTeacher }
        </a>
      </header>
    </div>
  );
}


export default App;
