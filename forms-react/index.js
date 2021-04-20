const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cors());
app.use(express.json());
app.post("/", async (req, res) => {
  console.log(req.body.name);
  res.status(200).send({ msg: "Success" });
});
app.listen(5000, () => console.log("Server Runnning"));
