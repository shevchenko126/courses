import { useState } from 'react';
import './mainBlock.css';

const MainBlock = ({ content, display, color, clickButtonFunction }) => {

    const [number, setNumber] = useState(549)
    if( !display ){
        return '';
    }


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

    return (
        <div className={`main-block ${ color == 'red' ? 'red' : '' }`}>
            <div className="container" style={{ borderBottom: "5px solid red", borderTop: "10px solid green"}}>
                {content} 
                <div onClick={plusNumber}>+</div>
                <div>{number}</div>
                <div onClick={minusNumber}>-</div>
                <button onClick={ clickButtonFunction }>Do it</button>
            </div>
        </div>
    )
}

export default MainBlock