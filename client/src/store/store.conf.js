import {configureStore} from "@reduxjs/toolkit";

import autoparkReducer from "./autopark.slice";

const store = configureStore({
  reducer: {
    autoparkReducer
  }
})

export default store;