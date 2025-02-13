from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
from pydantic import BaseModel
import json
import datetime

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


def log(message):
    with open("log.txt", "a") as file:
        file.write(str(datetime.datetime.now()) +   ": " + message + "\n")



with open("wallList.json", 'r') as file:
    wallList = json.load(file)
    no_walls = wallList["no_walls"]

@app.get("/")
async def root():

    

    return {"message": "Hello World",
             "wallList" : wallList["walls"]
             }

@app.get("/getWallInfo")
async def get_wall_info(id: str):

    log(str(id))
    for wall in wallList["walls"]: # yes, this is horribly inefficient... But I don't want to rewrite the json and break everything, so this'll have to do until I implement an actual database
        if wall["id"] == id:
            return(wall)

    else:
        raise HTTPException(status_code=404, detail="No wall with that ID found in database") # Ayyy, my first 404 !


@app.get("/getImage/")
async def get_image(id: str=1):
    imagePath = Path("./processing/processed_images/" + id + ".jpg")
    if not imagePath.is_file():
        imagePath = Path("./wallPhotos/climbing3.jpg") # Gives a default image
        # return ({"Path not found!"})

    return FileResponse(imagePath)



# =========== POSTING =============

class wallInfoData(BaseModel):
    title: str
    notes: str
    rating: str
    grade: str
    isSent: bool

class formData(BaseModel):
    user_id: int
    username: str
    data: wallInfoData
    # where data will have .title, .grade
    # .. dunno how to mandate it having a .title/.grade

@app.post("/upload/")
async def upload(data: wallInfoData):
    # Do something with the received data

    wallInfo = data

    log(f"Received: {wallInfo.title}")

    log("Attempting to write!")

    # wallList["walls"].append(f'''{{
    #                 "id" : {no_walls},
    #                 "title" : {wallInfo.title},
    #                 "grade" : {wallInfo.grade}
    #                 }}''')
    # no_walls += 1
    wallList["no_walls"] += 1
    wallList["walls"].append({
        "id" : str(no_walls),
        "title" : wallInfo.title,
        "grade" : wallInfo.grade,
        "rating": wallInfo.rating,
        "notes": wallInfo.notes
    })
    with open("wallList.json", 'w') as file:
        file.write(json.dumps(wallList))
    
    # Example: Processing and returning a response
    return {"message" : "Data Recieved!"}
