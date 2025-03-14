import cv2
from deepface import DeepFace

class MoodDetector:
    def __init__(self):
        self.model = "Emotion"  # DeepFace supports 'Emotion' model for mood detection

    def detect_mood(self, frame):
        """
        Detects mood from an input frame using DeepFace.
        :param frame: Image frame (numpy array)
        :return: Detected mood (string)
        """
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            mood = result[0]['dominant_emotion']
            return mood
        except Exception as e:
            print(f"Error in mood detection: {e}")
            return "unknown"

    def process_image(self, image_path):
        """
        Processes an image file and detects mood.
        :param image_path: Path to the image file
        :return: Detected mood (string)
        """
        frame = cv2.imread(image_path)
        return self.detect_mood(frame)
