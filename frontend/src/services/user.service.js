import {axiosService} from "./axios.service";

import baseURL from "../constants/urls";

export const userService = {
    createUser: (userData) => axiosService.post(`${baseURL}/users/`, userData),
    activateUser: (activationToken) => axiosService.get(`${baseURL}/authentication/activate/${activationToken}`)
}