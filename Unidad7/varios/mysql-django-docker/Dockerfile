# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=myapp.settings

# Install system dependencies for building mysqlclient
RUN apt-get update && apt-get install -y default-libmysqlclient-dev libmariadbclient-dev gcc pkg-config

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the Django project code into the container
COPY . .

# Expose port 8000 for the Django development server
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
