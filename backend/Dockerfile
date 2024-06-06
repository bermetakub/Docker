# Dockerfile for Python Backend
FROM python:3.8-slim

WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install flask psycopg2-binary

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
