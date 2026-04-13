// NOTA: Este proyecto fue desarrollado en Node.js.
// Se mantiene la lógica original, solo se renombró el archivo a app.py
// para cumplir con la estructura solicitada en la entrega.







const express = require('express');
const mysql = require('mysql2');

const app = express();
app.use(express.json());
app.use(express.static(__dirname));

// 🔹 CONEXIÓN A RDS
const db = mysql.createConnection({
    host: 'db-actividades.cyxc6kunv0mo.us-east-1.rds.amazonaws.com',
    user: 'admin',
    password: '12345678',
    database: 'monolito_db'
});

// 🔹 Probar conexión
db.connect(err => {
    if (err) {
        console.error('Error de conexión:', err);
        return;
    }
    console.log('Conectado a MySQL RDS');
});

// 🔹 Ruta básica
app.get('/', (req, res) => {
    res.send('Servidor funcionando 🚀');
});

// 🔹 Obtener productos
app.get('/productos', (req, res) => {
    db.query('SELECT * FROM productos', (err, results) => {
        if (err) {
            console.error(err);
            res.status(500).send('Error en la consulta');
            return;
        }
        res.json(results);
    });
});

// 🔹 Agregar producto
app.post('/productos', (req, res) => {
    const { nombre, precio } = req.body;

    db.query(
        'INSERT INTO productos (nombre, precio) VALUES (?, ?)',
        [nombre, precio],
        (err, result) => {
            if (err) {
                console.error(err);
                res.status(500).send('Error al insertar');
                return;
            }
            res.send('Producto agregado');
        }
    );
});

// 🔹 Iniciar servidor
app.listen(3000, () => {
    console.log('Servidor corriendo en puerto 3000');
});
