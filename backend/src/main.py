from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import auth_router, tasks_router
from .config import settings


def create_app():
    """
    Create and configure the FastAPI application
    """
    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        debug=settings.debug,
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, replace with specific origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routes
    app.include_router(auth_router)
    app.include_router(tasks_router)

    @app.get("/")
    def read_root():
        return {"message": "Todo API - Authentication & User Isolation"}

    return app


# Create the main application instance
app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )