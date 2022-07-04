import { useEffect, useState, useRef } from 'react';
import { useParams } from 'react-router-dom';
import './mainBlock.css';

import getBlog from '../../../api/blog'

const MainBlock = (props) => {

    const { content, display, color, clickButtonFunction } = props
    const blog = [
        {
            title: 'AAA',
            author: 'ssss',
            date: '02.03.2022'
        },
        {
            title: 'BBB',
            author: '3rr3',
            date: '02.07.2022'
        },
        {
            title: 'AAA',
            author: 'ssss',
            date: '02.03.2022'
        },
    ]

    const addPost = {
        title: 'iiii',
        author: 'ssss',
        date: '02.03.2022'
    }

    const divRef = useRef()

    const [number, setNumber] = useState(blog.length)
    const [posts, setPosts] = useState(blog)
    const [students, setStudents] = useState([])

    const names = ["Ivan", "Vasyl", "Dmytro", "Oleg"]

    let defColor = color == 'red' ? 'red' : '';
    if( color == 'red' ){
        defColor = 'red'
    }

    const plusNumber = () => {
        setNumber(number + 1)
        clickButtonFunction();
    }

    const minusNumber = () => {
        const newNumber = Math.max(number - 1, 0)
        // Math.min()
        // Math.round()
        // Math.round(newNumber/100)*100
        setNumber(newNumber)
    }

    useEffect(() => {
        const newBlog = [...blog]
        if( names.includes("Oleh") ){
            newBlog[2].title = 'oooo'
        }
        setPosts(newBlog)

        const text = document.getElementById('input_text').value
        // document.getElementById('text_div').innerText = 'aaaaaa'
        divRef.current.innerText = 'aaaaaa'

        console.log(text);

    }, [number])

    const params = useParams();
    console.log(params)

    useEffect(() => {
        getBlog().then((response) => {

            setStudents(response.students)
    
            console.log(response)
        });

    }, [])

    const htmlText = "<h2>ddddd</h2><div>ffff</div>";

    if( !display ){
        return '';
    }

    return (
        <div className={`main-block ${ color == 'red' ? 'red' : '' }`}>
            <div className="container" style={{ borderBottom: "5px solid red", borderTop: "10px solid green"}}>
                {content}
                <div onClick={plusNumber}>+</div>
                <div>{number}</div>
                <div onClick={minusNumber}>-</div>
                <button onClick={ clickButtonFunction }>Do it</button>
            </div>
            <div id="text_div" ref={divRef}>ssssss</div>

            <input type="text" id="input_text" />

            <img src="/images/logo192.png" />


            <div dangerouslySetInnerHTML={{__html:htmlText}}></div>


            {  posts.length ? posts.map(({ title, author }, i) => (
                <div className="test-array" key={i}>{ title } - { author }</div>
            )) : (
                <div></div>
            ) }


            { students.map((student) => (
                <div className="">{student.name}</div>
            )) }


        </div>
    )
}

export default MainBlock