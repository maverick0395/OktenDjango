import React, {useEffect} from 'react';
import { useDispatch, useSelector} from "react-redux";

import Autopark from "../Autopark/Autopark";
import { getAllAutoparks } from "../../store/autopark.slice";

const Home = () => {
    const {autoparks, status, error} = useSelector(state => state['autoparkReducer']);
    const dispatch = useDispatch();


    useEffect(() => {
        dispatch(getAllAutoparks());
    }, [])

    return (
        <div>
            {status === 'pending' && <h1>Loading</h1>}
            {status === 'rejected' && <h1>{error}</h1>}
            {autoparks.map(autopark => <Autopark key={autopark.id} autopark={autopark}/>)}
        </div>
    );
};

export default Home;