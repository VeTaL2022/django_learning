import {useEffect, useState} from "react";
import axios from "axios";

export const App = () => {
    const [cars, setCars] = useState([]);

    useEffect(() => {
        axios.get('/api/v1/cars').then(value => setCars(value.data))
    }, []);


    return (
        <div>
            <h1>Hello, Jack!</h1>
            {cars.map(car => <div key={car.id}>{car.brand}</div>)}
            {JSON.stringify(cars)}
        </div>
    );
};