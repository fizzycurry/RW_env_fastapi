from fastapi import FastAPI, UploadFile, HTTPException # type: ignore
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
DEBUG = getEnvironmentVariable("DEBUG", bool, False) 
# make sure path exists
if not path.exists(FILEPATH):
    makedirs(FILEPATH)


@app.post("/port")
async def port()->dict:
    return {"PORT": PORT}

@app.post("/upload/")
async def uploadFile(file: UploadFile)-> dict:
    try:
        filepath = path.join(FILEPATH, file.filename) 
        with open(filepath, "wb") as f:
            while chunk := file.file.read(1024*1024):
                f.write(chunk)
        return {"message": "File uploaded successfully", "filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=400, detail="File could not be uploaded")
    finally:
        file.file.close()


@app.get("/view/", response_class=FileResponse)
async def serveFile(filename: str) -> FileResponse:
    filepath = path.join(FILEPATH, path.basename(filename))

    if not path.exists(filepath) or not path.isfile(filepath):
        raise HTTPException(status_code=404, detail="File not found")
    
    mime_type, _ = mimetypes.guess_type(filepath)
    if mime_type is None:
        raise HTTPException(status_code=400, detail="Unsupported or unknown file type")
    
    return FileResponse(filepath, media_type=mime_type)

if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, reload=DEBUG) #getting values from environment variables
