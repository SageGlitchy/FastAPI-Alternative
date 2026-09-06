"""Health endpoint example for a FastAPI application.

Demonstrates a /health endpoint suitable for container orchestrators,
load balancers, and monitoring systems.
"""

from fastapi import APIRouter, FastAPI

router = APIRouter(tags=["observability"])


@router.get("/health")
async def health_check():
    """Health check endpoint.

    Returns a simple status response indicating the service is running.
    Container orchestrators (e.g., Kubernetes) and load balancers can
    poll this endpoint to determine service availability.
    """
    return {"status": "ok"}


app = FastAPI()
app.include_router(router)
