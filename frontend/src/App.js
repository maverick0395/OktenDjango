import {Route, Routes} from "react-router-dom";

import Home from "./components/Home/Home";
import {Header} from "./components/Header/Header";
import {Register} from "./components/Register/Register";
import Activation from "./components/Activation/Activation";

function App() {
    return (
        <div>
            <Routes>
                <Route path={'/'} element={<Header/>}>
                    <Route path={'/'} element={<Home/>}/>
                    <Route path={'register'} element={<Register/>}/>
                    <Route path={'activate/:activationToken'} element={<Activation/>}/>
                </Route>


            </Routes>
        </div>
    );
}

export default App;
