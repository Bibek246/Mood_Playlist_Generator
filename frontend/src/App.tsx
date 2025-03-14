import React, { useState } from "react";
import WebcamCapture from "./components/WebcamCapture";
import MoodDisplay from "./components/MoodDisplay";
import Playlist from "./components/Playlist";

const App: React.FC = () => {
  const [mood, setMood] = useState<string>("");

  return (
    <div>
      <h1>Mood-Based Playlist Generator</h1>
      <WebcamCapture onMoodDetected={setMood} />
      <MoodDisplay mood={mood} />
      <Playlist mood={mood} />
    </div>
  );
};

export default App;
