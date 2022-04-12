import {createAsyncThunk ,createSlice} from "@reduxjs/toolkit";
import {autoparkService} from "../services/autopark.service";

export const getAllAutoparks = createAsyncThunk(
    'autoparkSlice/getAllAutoparks',
    async(_, {rejectWithValue}) => {
        try {
            const autoparks = await autoparkService.getAll();
            return autoparks.data
        } catch (e) {
            console.log(e.message)
        }
    }
)

export const createCar = createAsyncThunk(
    'autoparkSlice/createCar',
    async({autoparkId, carData}, {dispatch}) => {
        try {
            const newCar = await autoparkService.create(autoparkId, carData);
            dispatch(addCar({autoparkId, newCar}))
        } catch (e) {
            console.log(e.message)
        }
    }
)

export const deleteAutoparkThunk = createAsyncThunk(
    'autoparkSlice/deleteAutopark',
    async (autoparkId, {dispatch}) => {
        try {
            await autoparkService.deleteById(autoparkId);
            dispatch(deleteAutopark({autoparkId}));
        } catch (e) {
            console.log(e.message)
        }
}

)

const autoparkSlice = createSlice({
    name: 'autoparkSlice',
    initialState: {
        autoparks: [],
        status: null,
        error: null
    },
    reducers: {
        addCar: (state, action) => {
            state.autoparks[state.autoparks.findIndex(autopark => autopark.id === action.payload.autoparkId)]['cars'].push(action.payload.newCar)
        },
        deleteAutopark: (state, action) => {
            state.autoparks = state.autoparks.filter(autopark => autopark.id !== action.payload.autoparkId)
        }
    },
    extraReducers: {
         [getAllAutoparks.pending]:
            (state, action) => {
                state.status = 'pending';
                state.error = null;
            },
        [getAllAutoparks.fulfilled]:
            (state, action) => {
                console.log(action.payload);
                state.status = 'fulfilled';
                state.autoparks = action.payload;
            },
        [getAllAutoparks.rejected]:
            (state, action) => {
                state.status = 'rejected';
                state.error = action.payload;

            },
    }
})

const autoparkReducer = autoparkSlice.reducer;

export const { deleteAutopark, addCar } = autoparkSlice.actions;

export default autoparkReducer