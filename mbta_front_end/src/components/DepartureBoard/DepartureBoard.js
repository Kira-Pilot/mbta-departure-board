import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import Table from 'react-bootstrap/Table';
import Moment from 'react-moment';
import useInterval from '../../hooks/useInterval';

function DepartureBoard(props) {
  const headers = ['Time', 'Destination', 'Train #', 'Track #', 'Status'];
  const nameRegex = /...(.+)/;

  const [departures, setDepartures] = useState([]);
  let [isLoaded, setIsLoaded] = useState(false);
  let [stationId, setStationId] = useState(props.station);

  useEffect(() => {
    setStationId(props.station);
    setIsLoaded(false);
  }, [props.station]);

  useInterval(
    () => {
      fetch(`http://localhost:8000/departures/${stationId}`)
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

export default DepartureBoard;
