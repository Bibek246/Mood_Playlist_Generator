import React, { useState } from "react";
import { Container, Typography, Button, CircularProgress, Card, CardMedia, CardContent, Box } from "@mui/material";
import axios from "axios";
import WebcamCapture from "./components/WebcamCapture";

const App: React.FC = () => {
    const [mood, setMood] = useState<string | null>(null);
    const [playlist, setPlaylist] = useState<{ name: string; image: string; url: string } | null>(null);
    const [loading, setLoading] = useState(false);

    const handleDetectMood = async (imageFile: File) => {
        setLoading(true);
        try {
            const formData = new FormData();
            formData.append("file", imageFile);

            // 🎭 Detect Mood
            const moodResponse = await axios.post("http://127.0.0.1:8000/api/detect-mood/", formData);
            const detectedMood = moodResponse.data.mood;
            setMood(detectedMood);
            console.log(`Detected Mood: ${detectedMood}`);

            // 🎵 Fetch Playlist
            const playlistResponse = await axios.get(`http://127.0.0.1:8000/api/get-playlist/${detectedMood}`);
            setPlaylist({
                name: `Your ${detectedMood} Playlist 🎵`,
                image: `https://source.unsplash.com/featured/?music,${detectedMood}`, // Random image
                url: playlistResponse.data.playlist_url
            });

        } catch (error) {
            console.error("Error:", error);
            alert("Something went wrong. Try again!");
        }
        setLoading(false);
    };

    return (
        <Container maxWidth="md" sx={{ textAlign: "center", mt: 5 }}>
            <Typography variant="h3" gutterBottom fontWeight="bold">
                🎭 AI Mood-Based Playlist Generator 🎶
            </Typography>
            <Typography variant="subtitle1" color="text.secondary">
                Detect your mood & get the perfect playlist from Spotify! 🚀
            </Typography>

            <Box mt={4}>
                <WebcamCapture onCapture={handleDetectMood} />
            </Box>

            {loading && <CircularProgress sx={{ mt: 3 }} />}

            {mood && (
                <Typography variant="h5" sx={{ mt: 4 }}>
                    Detected Mood: <strong>{mood.toUpperCase()}</strong> 🎭
                </Typography>
            )}

            {playlist && (
                <Card sx={{ maxWidth: 400, mt: 4, mx: "auto", boxShadow: 5 }}>
                    <CardMedia component="img" height="200" image={playlist.image} alt="Playlist Cover" />
                    <CardContent>
                        <Typography variant="h6" fontWeight="bold">
                            {playlist.name}
                        </Typography>
                        <Button
                            variant="contained"
                            color="primary"
                            href={playlist.url}
                            target="_blank"
                            sx={{ mt: 2 }}
                        >
                            🎧 Open on Spotify
                        </Button>
                    </CardContent>
                </Card>
            )}
        </Container>
    );
};

export default App;
