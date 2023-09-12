# Usamos la imagen oficial de Python
FROM python:3.8

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos los archivos necesarios al contenedor
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install -r requirements.txt

# Copiamos todo el contenido del proyecto al contenedor
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
