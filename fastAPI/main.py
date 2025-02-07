from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import sys

from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = logging.getLogger("uvicorn.error")
# logger.setLevel(logging.DEBUG)

def log(message):
    with open("log.txt", "a") as file:
        file.write(message + "\n")



wallList = [
                 {
                    "id" : "1",
                    "title" : "Baby Ladder",
                    "grade" : "V1"
                 },
                 {
                    "id" : "4",
                    "title" : "Skin Ripper",
                    "grade" : "V8"
                 },
             ]

@app.get("/")
async def root():
    logger.debug("hey there!")
    

    return {"message": "Hello World",
             "wallList" : wallList
             
             }

images = Path("./wallPhotos/")

@app.get("/getImage/1")
async def get_image():
    imagePath = images + Path("climbing3.jpg")
    if not imagePath.is_file():
        return ({"Path not found!"})
    return FileResponse(imagePath)



@app.get("/getImage/")
async def get_image(id: str=1):
    imagePath = Path("./processing/processed_images/" + id + ".jpg")
    if not imagePath.is_file():
        return ({"Path not found!"})
    return FileResponse(imagePath)



# =========== POSTING =============

@app.post("/upload/")
async def upload(data):
    # Do something with the received data
    log(f"Received: {data}")

    wallList.append({
                    "id" : "5",
                    "title" : "Skin Ripper",
                    "grade" : "V8"
                 },)
    
    # Example: Processing and returning a response
    return {"message" : "Data Recieved!"}
