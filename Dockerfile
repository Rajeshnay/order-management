# Use the official Python image from Docker Hub
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all the project files into the container
COPY . .

# Install required Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Command to run the app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT}"]

