# backend/app.py

from fastapi import FastAPI, UploadFile
from model import *
import uvicorn

# Backend
# Server side with FastAPI
app = FastAPI(title="Seeing Out Loud",
              description="Image Caption Generator",
              version="0.1.0")


@app.get("/")
async def root():
    '''
    boilerplate home page
    '''
    return {"message": "Welcome to Seeing Out Loud"}


@app.post("/uploadfile")
async def create_upload_file(image_data: UploadFile):
    '''
    Post request from user, uploaded file is sent into model as bytes.
    The generated caption is then returned in JSON format
    '''
    if not image_data:
        return {"message": "No upload file sent"}
    else:
        caption = generate_caption(image_data.file.read())
        return {"Caption": f"{caption}."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
