import {useState} from 'react'

export const App = () => {
  const [message, setMessage] = useState("");

  return (
    <div>
      <h1>StockManager</h1>
      <p>API Response: {message}</p>
    </div>
  );
}