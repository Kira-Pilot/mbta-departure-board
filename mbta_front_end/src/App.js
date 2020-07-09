import React, { useState } from 'react';
import DepartureBoard from './components/DepartureBoard/DepartureBoard';
import Time from './components/Time/Time';
import CalendarDate from './components/CalendarDate/CalendarDate';
import 'bootstrap/dist/css/bootstrap.min.css';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import './App.css';

function App() {
  const stationMap = {
    'place-north': {
      displayName: 'North Station',
      id: 'place-north',
    },
    'place-sstat': {
      displayName: 'South Station',
      id: 'place-sstat',
    },
  };

  let [stationId, setStation] = useState(stationMap['place-north'].id);

  function updateStation(event) {
    setStation(event);
  }

  return (
    <div className="DepartureContainer">
      <DropdownButton
        id="station-button"
        title={stationMap[stationId].displayName}
        onSelect={(event) => updateStation(event)}
        className="StationDropdown"
        variant="secondary"
        size="lg"
      >
        <Dropdown.Item
          eventKey="place-north"
          active={stationId === 'place-north'}
        >
          North Station
        </Dropdown.Item>
        <Dropdown.Item
          eventKey="place-sstat"
          active={stationId === 'place-sstat'}
        >
          South Station
        </Dropdown.Item>
      </DropdownButton>
      <div className="TimeContainer">
        <CalendarDate></CalendarDate>
        <Time></Time>
      </div>
      <DepartureBoard station={stationId}></DepartureBoard>
    </div>
  );
}

export default App;
