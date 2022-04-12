import {axiosService} from "./axios.service";

import baseURL from "../constants/urls";

export const autoparkService = {
    getAll: () => axiosService.get(`${baseURL}/autoparks/`).then(value => value.data),
    getById: (id) => axiosService.get(`${baseURL}/autoparks/${id}`).then(value => value.data),
    deleteById: (id) => axiosService.delete(`${baseURL}/autoparks/${id}`),
    create: (autoparkId, car) => axiosService.post(`${baseURL}/autoparks/${autoparkId}/add_car/`, car).then(value => value.data),
    getCarsByAutoparkId: (autoparkId) => axiosService.get(`${baseURL}/cars?autopark=${autoparkId}`).then(value => value.data)
}