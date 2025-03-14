import React from "react";

const MoodDisplay: React.FC<{ mood: string }> = ({ mood }) => {
  if (!mood) return null;
  
  return (
    <div>
      <h2>Detected Mood: {mood}</h2>
    </div>
  );
};

export default MoodDisplay;
