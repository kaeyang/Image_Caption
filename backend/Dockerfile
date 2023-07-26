# backend/Dockerfile

# set base image
FROM python:3.9

# set base path for backend portion
WORKDIR /app

RUN apt-get update
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

# Set the command to run the app
CMD ["python", "main.py"]