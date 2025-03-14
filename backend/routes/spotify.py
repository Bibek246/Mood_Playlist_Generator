from fastapi import APIRouter, HTTPException
import requests
from backend.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

router = APIRouter()

# Spotify API URLs
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_URL = "https://api.spotify.com/v1"

def get_spotify_token():
    """
    Get a fresh Spotify API access token.
    """
    print("🎵 Requesting fresh Spotify token...")  # Debugging

    response = requests.post(
        SPOTIFY_AUTH_URL,
        data={"grant_type": "client_credentials"},
        auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET),
    )

    print(f"🔍 Spotify API Response: {response.status_code}, {response.text}")  # Debugging

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Error fetching Spotify token: {response.text}")

    token_data = response.json()
    access_token = token_data.get("access_token")

    if not access_token:
        raise HTTPException(status_code=500, detail="Failed to retrieve Spotify access token.")

    return access_token


def get_playlist_by_mood(mood: str):
    """
    Fetches a Spotify playlist based on mood using valid Spotify category names.
    """
    mood_to_category = {
        "happy": "Pop",
        "sad": "Christian & Gospel",
        "angry": "Rock",
        "neutral": "Mood",
        "surprise": "Dance/Electronic",
        "fear": "Workout"
    }

    category_name = mood_to_category.get(mood.lower())
    if not category_name:
        raise HTTPException(status_code=400, detail=f"Invalid mood: {mood}")

    print(f"🎧 Fetching playlist for mood '{mood}' -> category '{category_name}'")  # Debugging

    token = get_spotify_token()
    headers = {"Authorization": f"Bearer {token}"}

    # 🔹 Search for playlists by category name
    search_url = f"https://api.spotify.com/v1/search?q={category_name}&type=playlist&limit=5"
    response = requests.get(search_url, headers=headers)

    print(f"🔎 Spotify Playlist Search Response: {response.status_code}, {response.text}")  # Debugging

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=f"Error fetching playlists: {response.text}")

    playlists = response.json().get("playlists", {}).get("items", [])

    # 🔹 Find the first valid (non-null) playlist
    valid_playlist = next((p for p in playlists if p is not None), None)

    if not valid_playlist:
        print(f"⚠️ No valid playlists found for category '{category_name}'.")
        raise HTTPException(status_code=404, detail=f"No playlists found for mood: {mood}")

    return valid_playlist["external_urls"]["spotify"]


@router.get("/get-playlist/{mood}")
def get_playlist(mood: str):
    """
    API endpoint to get a Spotify playlist based on mood.
    """
    try:
        print(f"🎵 Fetching playlist for mood: {mood}")  # Debugging
        playlist_url = get_playlist_by_mood(mood)
        print(f"✅ Playlist URL: {playlist_url}")  # Debugging
        return {"playlist_url": playlist_url}
    except HTTPException as http_error:
        print(f"❌ Error: {http_error.detail}")  # Debugging
        raise http_error
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")  # Debugging
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
