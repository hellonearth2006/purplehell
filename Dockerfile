# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in pyproject.toml
RUN pip install poetry && poetry install --no-dev

# Run main.py when the container launches
CMD ["poetry", "run", "python", "main.py"]
