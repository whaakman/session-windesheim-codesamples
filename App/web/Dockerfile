# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy only the necessary files into the container
COPY app.py /app
COPY static /app/static
COPY templates /app/templates

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV NAMESPACE_CONNECTION_STR="your_connection_string_here"
ENV QUEUE_NAME="your_queue_name_here"

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask to run in production
ENV FLASK_ENV=production

# Run app.py when the container launches
CMD ["python", "app.py"]
