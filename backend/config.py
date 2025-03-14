import os
from dotenv import load_dotenv

# Load .env variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Read Spotify credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Debugging: Print values to confirm they're loaded
print(f"🎵 SPOTIFY_CLIENT_ID: {SPOTIFY_CLIENT_ID}")
print(f"🔒 SPOTIFY_CLIENT_SECRET: {'HIDDEN' if SPOTIFY_CLIENT_SECRET else 'NOT LOADED'}")
