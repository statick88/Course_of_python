# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Install system dependencies for building mysqlclient
RUN apt-get update && apt-get install -y default-libmysqlclient-dev libmariadbclient-dev gcc pkg-config

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Start the Flask app
CMD ["flask", "run"]
