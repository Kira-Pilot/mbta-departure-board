import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import Table from 'react-bootstrap/Table';
import Moment from 'react-moment';
import useInterval from '../../hooks/useInterval';

export default function DepartureBoard(props) {
  const { station } = props;
  const pollingDelay = 60000;
  const headers = ['Time', 'Destination', 'Train #', 'Track #', 'Status'];
  const nameRegex = /...(.+)/;

  const [departures, setDepartures] = useState([]);

  useEffect(() => {
    getDepartures(station, setDepartures);
  }, [station]);

  useInterval(() => {
    getDepartures(station, setDepartures);
  }, pollingDelay);

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
          <tr key={departure.train_no.concat(departure.name)}>
            <td>
              <Moment format="h:mm A">{departure.departure_time}</Moment>
            </td>
            <td>{nameRegex.exec(departure.name)[1]}</td>
            <td>{departure.train_no}</td>
            <td>{departure.platform_code || 'TBD'}</td>
            <td>{departure.status || 'Unknown'}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
}

DepartureBoard.propTypes = {
  station: PropTypes.string,
};

function getDepartures(station, setDepartures) {
  fetch(`http://localhost:8000/departures/${station}`)
    .then((res) => res.json())
    .then((response) => {
      setDepartures(response);
    })
    .catch((error) => console.error(error));
}
