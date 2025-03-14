from fastapi import APIRouter
from .mood import router as mood_router
from .spotify import router as spotify_router

router = APIRouter()

# Include API routes
router.include_router(mood_router, prefix="/api")
router.include_router(spotify_router, prefix="/api")
