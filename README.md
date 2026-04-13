# Proyecto: Sistema de Registro con Microservicios

**Alumno:** Kevin Adrian Morales Palomo
**Materia:** Diseño y Arquitectura de Software
**Fecha:** Abril 2026

---

## ¿Qué problema resuelve mi aplicación?

La aplicación permite registrar usuarios en una base de datos y ejecutar una tarea adicional después del registro. Esto simula sistemas reales donde se realizan procesos adicionales como notificaciones o validaciones después de guardar info.

---

## ¿Cuál era el problema del monolito?

Cuando ejecuté la prueba con Apache Benchmark, el sistema monolítico no pudo completar todas las peticiones. Se presentaron errores de timeout cuando aumentó la cantidad de usuarios concurrentes. Esto demuestra que el monolito no soporta alta carga y su rendimiento disminuye bajo muchas solicitudes.

---

## ¿Qué responsabilidad tiene cada microservicio?

**Servicio A:**
Recibe el registro del usuario, guarda la información en la base de datos y envía una solicitud al Servicio B.

**Servicio B:**
Procesa una tarea adicional relacionada con el registro y guarda la información en otra tabla.

---

## ¿Cómo se comunican los servicios?

Los servicios se comunican mediante HTTP usando el nombre del contenedor dentro de Docker Compose. El Servicio A llama al Servicio B usando su nombre como hostname, lo que funciona porque ambos están en la misma red interna.

---

## Tablas en la base de datos

| Tabla    | Servicio dueño | Qué guarda              |
| -------- | -------------- | ----------------------- |
| usuarios | Servicio A     | Información del usuario |
| tareas   | Servicio B     | Procesamiento adicional |

---

## ¿Qué pasa si el Servicio B se cae?

Cuando el Servicio B se detiene, el Servicio A sigue funcionando. El registro del usuario se guarda correctamente, pero se muestra un mensaje indicando que el servicio está en mantenimiento. Esto demuestra que el sistema es resiliente.

---

## Cómo levantar el proyecto

```bash
# 1. Clonar el repositorio
git clone https://github.com/KevinAdmp/Kevin-Morales-microservicios

# 2. Entrar a la carpeta
cd kevin-morales-microservicios/microservicios

# 3. Configurar variables de entorno en docker-compose.yml
(cambiar DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

# 4. Levantar servicios
docker-compose up --build -d

# 5. Abrir en navegador
http://34.207.142.19:5000
```

---

## Reflexión Final

Lo más difícil fue configurar la comunicación entre microservicios y manejar errores cuando uno de ellos fallaba. Aprendí que dividir un sistema en microservicios permite que una parte falle sin afectar todo el sistema. Esto es útil en aplicaciones grandes donde la disponibilidad es importante.

---

## Checklist de Autoevaluación

MONOLITO
[✔] Código del monolito incluido
[✔] Dockerfile funcional
[✔] Captura docker build
[✔] Captura docker run
[✔] Captura Apache Benchmark

README
[✔] Explica el problema
[✔] Explica monolito
[✔] Define microservicios
[✔] Explica comunicación
[✔] Incluye comandos
[✔] Incluye reflexión
