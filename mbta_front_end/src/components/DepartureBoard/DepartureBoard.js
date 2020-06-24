import React, { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table';
import Moment from 'react-moment';

function DepartureBoard() {
  const headers = ['Time', 'Destination', 'Train #', 'Track #', 'Status'];
  const nameRegex = /...(.+)/;
  const [departures, setDepartures] = useState([]);

  useEffect(() => {
    fetch(`http://localhost:8000/departures/place-north`)
      .then((res) => res.json())
      .then((response) => {
        console.log('RESPONSE', response);
        setDepartures(response);
      })
      .catch((error) => console.log(error));
  }, []);

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
  return <div>hello</div>;
}

export default DepartureBoard;
