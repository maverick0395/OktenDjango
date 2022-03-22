import {useDispatch} from "react-redux";

import {deleteAutoparkThunk} from "../../store/autopark.slice";
import Form from "../Form/Form";
import {useState} from "react";

const Autopark = ({autopark}) => {
    const dispatch = useDispatch();
    const [formIsVisible, setFormIsVisible] = useState(false)


    return (
        <div>
            <h3>{autopark.name}</h3>
            {!formIsVisible ?
                <button onClick={() => setFormIsVisible(!formIsVisible)}>Add car</button> :
                <Form autoparkId={autopark.id}/>
            }
            <ul>
            {autopark.cars && autopark.cars.map(car => (
                <li key={car.id}>{car.brand} - {car.price} - {car.year}</li>
            ))}
            </ul>
            <button onClick={() => dispatch(deleteAutoparkThunk(autopark.id))}>Delete autopark</button>
        </div>
    );
};

export default Autopark;