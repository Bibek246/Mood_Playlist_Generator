import cv2
import numpy as np
from fastapi import HTTPException
from io import BytesIO
from PIL import Image

def read_image(file):
    """
    Reads an uploaded image file and converts it into an OpenCV format.
    :param file: Uploaded image file (bytes)
    :return: OpenCV image (numpy array)
    """
    try:
        contents = file.read()
        np_arr = np.frombuffer(contents, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        return frame
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading image: {str(e)}")

def preprocess_image(image, target_size=(48, 48)):
    """
    Preprocess an image for mood detection.
    :param image: OpenCV image (numpy array)
    :param target_size: Target size for input model
    :return: Processed image (numpy array)
    """
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, target_size)
        return np.expand_dims(resized, axis=-1)  # Keep channel dimension
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error preprocessing image: {str(e)}")

def format_response(mood, playlist_url):
    """
    Formats the API response for better readability.
    :param mood: Detected mood (string)
    :param playlist_url: Spotify playlist URL (string)
    :return: JSON response
    """
    return {
        "mood": mood,
        "playlist": playlist_url,
        "message": f"We detected that you're feeling {mood}. Here's a playlist to match your mood!"
    }
