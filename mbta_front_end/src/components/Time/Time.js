import React, { useState, useEffect } from 'react';
import moment from 'moment';
import Moment from 'react-moment';
import styles from './Time.module.css';

export default function Time() {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const timeId = setInterval(() => tick(), 1000);
    return () => clearInterval(timeId);
  }, []);

  function tick() {
    if (moment().format('mm') !== moment(time).format('mm')) {
      setTime(new Date());
    }
  }

  return (
    <div className={styles.TimeContainer}>
      <div>Current Time</div>
      <Moment format="h:mm A">{time}</Moment>
    </div>
  );
}
