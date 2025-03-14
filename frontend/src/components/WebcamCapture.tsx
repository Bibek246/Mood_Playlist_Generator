import React, { useRef, useState } from "react";
import Webcam from "react-webcam";
import { Button, Box } from "@mui/material";

interface WebcamCaptureProps {
    onCapture: (imageFile: File) => void;
}

const WebcamCapture: React.FC<WebcamCaptureProps> = ({ onCapture }) => {
    const webcamRef = useRef<Webcam>(null);
    const [capturedImage, setCapturedImage] = useState<string | null>(null);

    const captureImage = () => {
        const imageSrc = webcamRef.current?.getScreenshot();
        if (imageSrc) {
            setCapturedImage(imageSrc);

            fetch(imageSrc)
                .then((res) => res.blob())
                .then((blob) => {
                    const file = new File([blob], "captured.jpg", { type: "image/jpeg" });
                    onCapture(file);
                });
        }
    };

    return (
        <Box sx={{ textAlign: "center" }}>
            <Webcam audio={false} ref={webcamRef} screenshotFormat="image/jpeg" width={320} />
            <br />
            <Button variant="contained" color="secondary" onClick={captureImage} sx={{ mt: 2 }}>
                📸 Capture Mood
            </Button>

            {capturedImage && <img src={capturedImage} alt="Captured" width={320} style={{ marginTop: 20 }} />}
        </Box>
    );
};

export default WebcamCapture;
