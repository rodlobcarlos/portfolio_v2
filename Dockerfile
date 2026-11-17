# Use an official Python runtime as a parent image
FROM python:3.12-slim as builder

# Set the working directory
WORKDIR /build

# Install system dependencies
RUN apt-get update && apt-get install -y unzip curl nodejs npm && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use a smaller base image for the final image
FROM python:3.12-slim as runtime

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y unzip curl nodejs npm && rm -rf /var/lib/apt/lists/*

# Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Set the entry point for the container
CMD ["reflex", "run"]