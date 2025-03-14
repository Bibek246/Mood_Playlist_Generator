import React, { useRef, useState } from "react";
import Webcam from "react-webcam";
import axios from "axios";

const WebcamCapture: React.FC<{ onMoodDetected: (mood: string) => void }> = ({ onMoodDetected }) => {
  const webcamRef = useRef<Webcam>(null);
  const [loading, setLoading] = useState(false);

  const captureAndSend = async () => {
    if (!webcamRef.current) return;
    
    const imageSrc = webcamRef.current.getScreenshot();
    if (!imageSrc) return;

    setLoading(true);
    
    try {
      const blob = await fetch(imageSrc).then(res => res.blob());
      const formData = new FormData();
      formData.append("file", blob, "snapshot.jpg");

      const response = await axios.post("http://127.0.0.1:8000/api/detect-mood/", formData);
      const detectedMood = response.data.mood;
      
      onMoodDetected(detectedMood);
    } catch (error) {
      console.error("Error detecting mood:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <Webcam ref={webcamRef} screenshotFormat="image/jpeg" />
      <button onClick={captureAndSend} disabled={loading}>
        {loading ? "Detecting..." : "Detect Mood"}
      </button>
    </div>
  );
};

export default WebcamCapture;
