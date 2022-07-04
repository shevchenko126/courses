import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom'
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
      <Header />
      {/* { number > 3 ? (
          <div>
            sssss
          </div>
        ) : (
          <MainBlock clickButtonFunction={clickButtonFunction} content="Hello World!" number={number} display={true} color="green" />
        )
      } */}


      {/* <Router>
          <Routes>
            <Route path="/hello" children={(({ match }) => (
              <MainBlock {...props} clickButtonFunction={clickButtonFunction} content="Hello!" number={number} display={true} color="green" />
              )} />
            <Route path="/hello-world" children={(({ match }) => (
              <MainBlock {...props} clickButtonFunction={clickButtonFunction} content="Hello world!" number={number} display={true} color="green" />
              )} />
              <Route path="/:slug" children={(({ match }) => (
                <MainBlock match={match} clickButtonFunction={clickButtonFunction} content="Without content!" number={number} display={true} color="green" />
                )} />
          </Routes>
      </Router> */}


      <Router>


          <Routes>
            <Route path="/hello" element={(<MainBlock clickButtonFunction={clickButtonFunction} content="Hello world44!" number={number} display={true} color="green" />)} />
            <Route path="/dd/:slug" element={(<MainBlock clickButtonFunction={clickButtonFunction} content="Hello world!" number={number} display={true} color="green" />)} />
            <Route path="/dd/:slug/:ff" element={(<MainBlock clickButtonFunction={clickButtonFunction} content="Hello world!" number={number} display={true} color="green" />)} />
            {/* <Route path="/hello" exact element={(<MainBlock clickButtonFunction={clickButtonFunction} content="Hello worl1d!" number={number} display={true} color="green" />)} /> */}
            <Route path="/hello-world" component={(props) => (<MainBlock {...props} clickButtonFunction={clickButtonFunction} content="Hello!" number={number} display={true} color="green" />)} />
            <Route path="/dd/:slug" component={(props) => (<MainBlock {...props} clickButtonFunction={clickButtonFunction} content="Without content!" number={number} display={true} color="green" />)} />
          </Routes>
      </Router>



      
    </div>
  );
}


export default App;
