# Image Caption Generator

This application utilizes the BLIP Vision-Language Multimodal model from HuggingFace to generate descriptive captions for uploaded images. It comes with a fully-built client and server side, allowing you to easily try it out. The frontend and backend are neatly separated into Docker containers, seamlessly orchestrated by Docker Compose.

Frontend:
The frontend of this application is developed using Streamlit in Python. To interact with the backend API and model, the Python requests library is utilized. Users are presented with a file uploader on the page, allowing them to easily upload their own images and generate captions.

Backend:
The backend of this application is built using FastAPI in Python. It handles the file upload POST request from the user, processes the uploaded image, and feeds it into the model. The model then produces a descriptive caption for the image. <br /><br />



### To start

In your terminal:
```bash
$ docker-compose up -d --build
```

After the Docker image is created and the containers are running, go to http://localhost:8501/ <br /><br />



### To close down
In your terminal:
```bash
$ docker compose stop
```
