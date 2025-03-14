from fastapi import APIRouter, File, UploadFile, HTTPException
import cv2
import numpy as np
from backend.models.mood_detection import MoodDetector

router = APIRouter()

# Initialize MoodDetector
mood_detector = MoodDetector()

@router.post("/detect-mood/")
async def detect_mood(file: UploadFile = File(...)):
    """
    API endpoint to detect mood from an uploaded image.
    :param file: Image file uploaded by the user
    :return: Detected mood as JSON response
    """
    try:
        # Read the uploaded file as a numpy array
        contents = await file.read()
        np_arr = np.frombuffer(contents, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Detect mood
        mood = mood_detector.detect_mood(frame)

        return {"mood": mood}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error detecting mood: {str(e)}")
