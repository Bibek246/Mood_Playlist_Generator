import React, { useEffect, useState } from "react";
import axios from "axios";

const Playlist: React.FC<{ mood: string }> = ({ mood }) => {
  const [playlistUrl, setPlaylistUrl] = useState<string | null>(null);

  useEffect(() => {
    if (!mood) return;

    axios.get(`http://127.0.0.1:8000/api/get-playlist/${mood}`)
      .then(response => {
        setPlaylistUrl(response.data.playlist_url);
      })
      .catch(error => {
        console.error("Error fetching playlist:", error);
      });
  }, [mood]);

  if (!playlistUrl) return null;

  return (
    <div>
      <h3>Recommended Playlist</h3>
      <a href={playlistUrl} target="_blank" rel="noopener noreferrer">Listen on Spotify</a>
    </div>
  );
};

export default Playlist;
