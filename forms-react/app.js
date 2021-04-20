import { useState } from "react";
import Axios from "axios";
function App() {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [city, setCity] = useState("");
  const post = async (e) => {
    console.log(age, city, name);
    e.preventDefault();
    const data = await Axios.post("http://localhost:5000", {
      name: name,
      age: age,
      city: city,
    });
    const res = await data;
    console.log(res);
  };
  return (
    <div className="App">
      Form Data
      <form>
        <input
          type="text"
          placeholder="Input Your Name"
          onChange={(e) => {
            setName(e.target.value);
          }}
        />
        <br />
        <input
          type="text"
          placeholder="Age"
          onChange={(e) => {
            setAge(e.target.value);
          }}
        />
        <br />
        <input
          type="text"
          placeholder="City"
          onChange={(e) => {
            setCity(e.target.value);
          }}
        />
        <br />
        <button
          onClick={(e) => {
            post(e);
          }}
        >
          Submit
        </button>
        {name}
      </form>
    </div>
  );
}

export default App;
