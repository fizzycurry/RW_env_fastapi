from http.client import HTTPException
from fastapi import FastAPI, UploadFile # type: ignore
from fastapi.responses import FileResponse # type: ignore
from dotenv import load_dotenv # type: ignore
from getENV import getEnvironmentVariable
from os import makedirs, path
import mimetypes
import uvicorn # type: ignore

load_dotenv()

app = FastAPI()

PORT = getEnvironmentVariable("PORT", int, 8000)
FILEPATH = getEnvironmentVariable("FILEPATH", str, "uploads/")

# make sure path exists
if not path.exists(FILEPATH):
    makedirs(FILEPATH)


@app.post("/port")
async def port():
    return {"PORT": PORT}

@app.post("/upload/")
async def uploadFile(file: UploadFile):
    try:
        filepath = path.join(FILEPATH, file.filename) 
        with open(filepath, "wb") as f:
            while chunk := file.file.read(1024*1024):
                f.write(chunk)
        return {"message": "File uploaded successfully", "filename": file.filename}
    
    except Exception as e:
        print(e)
        return {"message": "File could not be  uploaded"}


@app.get("/view/", response_class=FileResponse)
async def serveFile(filename: str):
    filepath = path.join(FILEPATH, path.basename(filename))

    if not path.exists(filepath) or not path.isfile(filepath):
        raise HTTPException(status_code=404, detail="File not found")
    
    mime_type, _ = mimetypes.guess_type(filepath)
    if mime_type is None:
        raise HTTPException(status_code=400, detail="Unsupported or unknown file type")
    
    return FileResponse(filepath, media_type=mime_type)

if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, reload=True) #getting values from environment variables
