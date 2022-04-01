import {useForm} from "react-hook-form";
import {useState} from "react";

import {userService} from "../../services/user.service";
import css from './Register.module.css';


const Register = () => {
    const [response, setResponse] = useState({
        "okMessage": "",
        "errorMessage": ""
    })

    const {
        handleSubmit, register, reset
    } = useForm()


    const submit = async (formData) => {
        const userData = {
            "email": formData.email,
            "password": formData.password,
            "profile": {
                "name": formData.name,
                "surname": formData.surname,
                "birthdate": formData.birthdate,
                "phone": formData.phone
            }
        }
        try {
            await userService.createUser(userData).then(value => value.data)
            setResponse({okMessage: "User has been registered"})
        } catch (e) {
            setResponse({errorMessage: e.message})
        }
    }

    return (
        <div>
            {response.okMessage && <div className={css.okMessage}>{response.okMessage}</div>}
            {response.errorMessage && <div className={css.errorMessage}>{response.errorMessage}</div>}
            <form onSubmit={handleSubmit(submit)} className={css.form}>
                <p>
                    <label>Email: </label>
                    <input type="text" {...register('email')}/>
                </p>
                <p>
                    <label>Password: </label><input type="password" {...register('password')}/>
                </p>
                <p>
                    <label>Name: </label><input type="text" {...register('name')}/>
                </p>
                <p>
                    <label>Surname: </label><input type="text" {...register('surname')}/>
                </p>
                <p>
                    <label>Birthdate: </label><input type="text" {...register('birthdate')}/>
                </p>
                <p>
                    <label>Phone: </label><input type="text" {...register('phone')}/>
                </p>
                <button>Register</button>
            </form>
        </div>
    );
};

export {Register};