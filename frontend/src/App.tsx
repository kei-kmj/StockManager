import {useEffect, useState} from 'react'

export const App = () => {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://localhost:8000/")
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
      .catch((error) => console.error("Error fetching data:", error));
  }, []);

  return (
    <div>
      <h1>StockManager</h1>
      <p>API Response: {message}</p>
    </div>
  );
}