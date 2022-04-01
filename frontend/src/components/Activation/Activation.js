import css from './Activation.module.css';
import {useParams} from "react-router-dom";
import {userService} from "../../services/user.service";
import {useEffect, useState} from "react";

const Activation = () => {
    const [response, setResponse] = useState([])
    const {activationToken} = useParams();


    useEffect(() => {
        const activateUser = async (activationToken) => {
            try {
                await userService.activateUser(activationToken).then(value => value.data);
                setResponse("User has been activated");
            } catch (e) {
                setResponse("Token is invalid or expired");
            }
        }

        activateUser(activationToken);
    }, [])


    return (
        <div className={css.confirm}>
            {response && <p>{response}</p>}
        </div>
    );
};

export default Activation;