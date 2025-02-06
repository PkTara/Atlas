from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/")
async def root():
    return {"message": "Hello World",
             "wallList" : [
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




@app.get("/getImage/2")
async def get_image():
    imagePath = Path("../assets/images/climbing2.jpeg")
    if not imagePath.is_file():
        return ({"Path not found!"})
    return FileResponse(imagePath)

