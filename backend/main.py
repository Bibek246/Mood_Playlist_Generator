from backend.routes import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Initialize FastAPI app
app = FastAPI(
    title="AI-Powered Mood-Based Playlist Generator",
    description="Detects mood from facial expressions and generates a personalized Spotify playlist.",
    version="1.0.0"
)

# CORS settings (allow frontend to communicate with backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Mood-Based Playlist Generator API"}

# Run the server (if running standalone)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
