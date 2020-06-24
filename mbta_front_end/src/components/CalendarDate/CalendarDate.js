import React, { useState, useEffect } from 'react';
import moment from 'moment';
import Moment from 'react-moment';
import styles from './CalendarDate.module.css';

export default function CalendarDate() {
  const [calendarDate, setCalendarDate] = useState(new Date());

  useEffect(() => {
    tick();
  }, []);

  function tick() {
    if (moment().format('D') !== moment(calendarDate).format('D')) {
      setCalendarDate(new Date());
    }
  }

  return (
    <div className={styles.DateContainer}>
      <Moment format="dddd">{calendarDate}</Moment>
      <Moment format="MMMM Do YYYY">{calendarDate}</Moment>
    </div>
  );
}
