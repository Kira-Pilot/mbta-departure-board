import React, { useState } from 'react';
import Table from 'react-bootstrap/Table';
import Moment from 'react-moment';
import useInterval from '../../hooks/useInterval';

function DepartureBoard() {
  const headers = ['Time', 'Destination', 'Train #', 'Track #', 'Status'];
  const nameRegex = /...(.+)/;

  const [departures, setDepartures] = useState([]);
  let [isLoaded, setIsLoaded] = useState(false);

  useInterval(
    () => {
      fetch(`http://localhost:8000/departures/place-north`)
        .then((res) => res.json())
        .then((response) => {
          console.log('RESPONSE', response);
          setDepartures(response);
          isLoaded = true;
        })
        .catch((error) => console.error(error));
    },
    setIsLoaded,
    isLoaded ? 60000 : null
  );

  return (
    <Table responsive striped variant="dark">
      <thead>
        <tr>
          {headers.map((header) => (
            <th key={header}>{header}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {departures.map((departure) => (
          <tr key={departure.train_no}>
            <td>
              <Moment format="h:mm A">{departure.departure_time}</Moment>
            </td>
            <td>{nameRegex.exec(departure.name)[1]}</td>
            <td>{departure.train_no}</td>
            <td>{departure.platform_code || 'TBD'}</td>
            <td>{departure.status}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
}

export default DepartureBoard;
