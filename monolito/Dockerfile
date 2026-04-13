# Imagen base
FROM node:18

# Crear carpeta dentro del contenedor
WORKDIR /app

# Copiar archivos
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar todo el proyecto
COPY . .

# Exponer puerto
EXPOSE 3000

# Comando para iniciar app
CMD ["node", "app.js"]
