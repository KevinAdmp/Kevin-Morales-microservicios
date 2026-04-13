const express = require('express');
const mysql = require('mysql2');
const axios = require('axios');

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const db = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME
});

app.get('/', (req, res) => {
  res.send(`
    <h1>Registro</h1>
    <form method="POST" action="/registrar">
      <input name="nombre" placeholder="Nombre"/>
      <button>Enviar</button>
    </form>
  `);
});

app.post('/registrar', async (req, res) => {
  const { nombre } = req.body;

  db.query('INSERT INTO usuarios (nombre) VALUES (?)', [nombre]);

  try {
    await axios.post('http://servicio_b:4000/procesar', { nombre });
    res.json({ mensaje: "Notificación enviada al Servicio B" });
  } catch (error) {
    res.json({ mensaje: "Servicio B en mantenimiento, pero registro guardado" });
  }
});

app.listen(3000, '0.0.0.0');
