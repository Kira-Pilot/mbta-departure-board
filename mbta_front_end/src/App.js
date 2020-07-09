import React, { useState } from 'react';
import DepartureBoard from './components/DepartureBoard/DepartureBoard';
import Time from './components/Time/Time';
import CalendarDate from './components/CalendarDate/CalendarDate';
import 'bootstrap/dist/css/bootstrap.min.css';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import './App.css';

function App() {
  let [station, setStation] = useState('place-north');

  function updateStation(event) {
    setStation(event);
  }

  return (
    <div className="DepartureContainer">
      <DropdownButton
        id="station-button"
        title="Select a Station"
        onSelect={(event) => updateStation(event)}
        className="StationDropdown"
        variant="secondary"
        size="lg"
      >
        <Dropdown.Item
          eventKey="place-north"
          active={station === 'place-north'}
        >
          North Station
        </Dropdown.Item>
        <Dropdown.Item
          eventKey="place-sstat"
          active={station === 'place-sstat'}
        >
          South Station
        </Dropdown.Item>
      </DropdownButton>
      <div className="TimeContainer">
        <CalendarDate></CalendarDate>
        <Time></Time>
      </div>
      <DepartureBoard station={station}></DepartureBoard>
    </div>
  );
}

export default App;
