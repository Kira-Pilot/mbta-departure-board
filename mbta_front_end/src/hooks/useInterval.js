import { useEffect, useRef } from 'react';

export default function useInterval(callback, setIsLoaded, delay) {
  const savedCallback = useRef();

  useEffect(() => {
    savedCallback.current = callback;
  });

  useEffect(() => {
    function tick() {
      if (delay === null) {
        callback();
        setIsLoaded(true);
        return;
      }

      savedCallback.current();
    }

    let id = setInterval(tick, delay);
    return () => clearInterval(id);
  }, [delay]);
}
