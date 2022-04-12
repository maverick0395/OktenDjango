import {useForm} from "react-hook-form";
import {useDispatch} from "react-redux";
import {joiResolver} from "@hookform/resolvers/joi";

import {createCar} from "../../store/autopark.slice";
import {carValidator} from "../../validators/car.validator";

const Form = ({autoparkId}) => {
    const {
        handleSubmit, register, reset, formState: {errors}
    } = useForm({resolver: joiResolver(carValidator), mode: "onTouched"})

    const dispatch = useDispatch();

    const submit = (carData) => {
        dispatch(createCar({autoparkId, carData}));
        reset();
    }

    return (
        <form onSubmit={handleSubmit(submit)} >
            {errors.id && <span>{errors.id.message}</span>}
            <label>Brand: <input type="text" {...register('brand')}/></label>
            {errors.model && <span>{errors.model.message}</span>}
            <label>Price: <input type="number" {...register('price')}/></label>
            {errors.price && <span>{errors.price.message}</span>}
            <label>Year: <input type="number" {...register('year')}/></label>
            {errors.year && <span>{errors.year.message}</span>}
            <button>Add Car</button>
        </form>

    );
};

export default Form;