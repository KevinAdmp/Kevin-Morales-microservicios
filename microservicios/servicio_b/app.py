const express = require('express');
const mysql = require('mysql2');

const app = express();
app.use(express.json());

const db = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME
});

app.post('/procesar', (req, res) => {
  const { nombre } = req.body;

  setTimeout(() => {
    db.query('INSERT INTO logs (nombre) VALUES (?)', [nombre]);
  }, 3000);

  res.json({ status: "ok" });
});

app.listen(4000, '0.0.0.0');
