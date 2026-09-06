"""Structured logging configuration for a FastAPI application.

Demonstrates how to set up Python's standard logging with JSON-formatted
output, suitable for production log aggregation systems.
"""

import logging
import logging.config

from fastapi import FastAPI, Request

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "format": '{"time": "%(asctime)s", "level": "%(levelname)s", "name": "%(name)s", "message": "%(message)s"}',
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": "ext://sys.stdout",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
    "loggers": {
        "uvicorn": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "app": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}

logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger("app")

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(
        "Request started: %s %s",
        request.method,
        request.url.path,
    )
    response = await call_next(request)
    logger.info(
        "Request completed: %s %s status=%d",
        request.method,
        request.url.path,
        response.status_code,
    )
    return response


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    logger.debug("Fetching item %d", item_id)
    return {"item_id": item_id, "name": f"Item {item_id}"}
