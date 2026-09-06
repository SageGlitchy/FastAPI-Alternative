"""Shared fixtures for include_router defaults/overrides tests.

This module provides the common FastAPI app, routers, response classes,
dependencies, and callbacks used across the split test files.
"""

from fastapi import APIRouter, Depends, FastAPI, Response
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient


class ResponseLevel0(JSONResponse):
    media_type = "application/x-level-0"


class ResponseLevel1(JSONResponse):
    media_type = "application/x-level-1"


class ResponseLevel2(JSONResponse):
    media_type = "application/x-level-2"


class ResponseLevel3(JSONResponse):
    media_type = "application/x-level-3"


class ResponseLevel4(JSONResponse):
    media_type = "application/x-level-4"


class ResponseLevel5(JSONResponse):
    media_type = "application/x-level-5"


async def dep0(response: Response):
    response.headers["x-level0"] = "True"


async def dep1(response: Response):
    response.headers["x-level1"] = "True"


async def dep2(response: Response):
    response.headers["x-level2"] = "True"


async def dep3(response: Response):
    response.headers["x-level3"] = "True"


async def dep4(response: Response):
    response.headers["x-level4"] = "True"


async def dep5(response: Response):
    response.headers["x-level5"] = "True"


callback_router0 = APIRouter()


@callback_router0.get("/")
async def callback0(level0: str):
    pass  # pragma: nocover


callback_router1 = APIRouter()


@callback_router1.get("/")
async def callback1(level1: str):
    pass  # pragma: nocover


callback_router2 = APIRouter()


@callback_router2.get("/")
async def callback2(level2: str):
    pass  # pragma: nocover


callback_router3 = APIRouter()


@callback_router3.get("/")
async def callback3(level3: str):
    pass  # pragma: nocover


callback_router4 = APIRouter()


@callback_router4.get("/")
async def callback4(level4: str):
    pass  # pragma: nocover


callback_router5 = APIRouter()


@callback_router5.get("/")
async def callback5(level5: str):
    pass  # pragma: nocover


app = FastAPI(
    dependencies=[Depends(dep0)],
    responses={
        400: {"description": "Client error level 0"},
        500: {"description": "Server error level 0"},
    },
    default_response_class=ResponseLevel0,
    callbacks=callback_router0.routes,
)

router2_override = APIRouter(
    prefix="/level2",
    tags=["level2a", "level2b"],
    dependencies=[Depends(dep2)],
    responses={
        402: {"description": "Client error level 2"},
        502: {"description": "Server error level 2"},
    },
    default_response_class=ResponseLevel2,
    callbacks=callback_router2.routes,
    deprecated=True,
)
router2_default = APIRouter()
router4_override = APIRouter(
    prefix="/level4",
    tags=["level4a", "level4b"],
    dependencies=[Depends(dep4)],
    responses={
        404: {"description": "Client error level 4"},
        504: {"description": "Server error level 4"},
    },
    default_response_class=ResponseLevel4,
    callbacks=callback_router4.routes,
    deprecated=True,
)
router4_default = APIRouter()


@app.get(
    "/override1",
    tags=["path1a", "path1b"],
    responses={
        401: {"description": "Client error level 1"},
        501: {"description": "Server error level 1"},
    },
    deprecated=True,
    callbacks=callback_router1.routes,
    dependencies=[Depends(dep1)],
    response_class=ResponseLevel1,
)
async def path1_override(level1: str):
    return level1


@app.get("/default1")
async def path1_default(level1: str):
    return level1


@router2_override.get(
    "/override3",
    tags=["path3a", "path3b"],
    responses={
        403: {"description": "Client error level 3"},
        503: {"description": "Server error level 3"},
    },
    deprecated=True,
    callbacks=callback_router3.routes,
    dependencies=[Depends(dep3)],
    response_class=ResponseLevel3,
)
async def path3_override_router2_override(level3: str):
    return level3


@router2_override.get("/default3")
async def path3_default_router2_override(level3: str):
    return level3


@router2_default.get(
    "/override3",
    tags=["path3a", "path3b"],
    responses={
        403: {"description": "Client error level 3"},
        503: {"description": "Server error level 3"},
    },
    deprecated=True,
    callbacks=callback_router3.routes,
    dependencies=[Depends(dep3)],
    response_class=ResponseLevel3,
)
async def path3_override_router2_default(level3: str):
    return level3


@router2_default.get("/default3")
async def path3_default_router2_default(level3: str):
    return level3


@router4_override.get(
    "/override5",
    tags=["path5a", "path5b"],
    responses={
        405: {"description": "Client error level 5"},
        505: {"description": "Server error level 5"},
    },
    deprecated=True,
    callbacks=callback_router5.routes,
    dependencies=[Depends(dep5)],
    response_class=ResponseLevel5,
)
async def path5_override_router4_override(level5: str):
    return level5


@router4_override.get(
    "/default5",
)
async def path5_default_router4_override(level5: str):
    return level5


@router4_default.get(
    "/override5",
    tags=["path5a", "path5b"],
    responses={
        405: {"description": "Client error level 5"},
        505: {"description": "Server error level 5"},
    },
    deprecated=True,
    callbacks=callback_router5.routes,
    dependencies=[Depends(dep5)],
    response_class=ResponseLevel5,
)
async def path5_override_router4_default(level5: str):
    return level5


@router4_default.get(
    "/default5",
)
async def path5_default_router4_default(level5: str):
    return level5


router2_override.include_router(
    router4_override,
    prefix="/level3",
    tags=["level3a", "level3b"],
    dependencies=[Depends(dep3)],
    responses={
        403: {"description": "Client error level 3"},
        503: {"description": "Server error level 3"},
    },
    default_response_class=ResponseLevel3,
    callbacks=callback_router3.routes,
)

router2_override.include_router(
    router4_default,
    prefix="/level3",
    tags=["level3a", "level3b"],
    dependencies=[Depends(dep3)],
    responses={
        403: {"description": "Client error level 3"},
        503: {"description": "Server error level 3"},
    },
    default_response_class=ResponseLevel3,
    callbacks=callback_router3.routes,
)

router2_override.include_router(router4_override)

router2_override.include_router(router4_default)

router2_default.include_router(
    router4_override,
    prefix="/level3",
    tags=["level3a", "level3b"],
    dependencies=[Depends(dep3)],
    responses={
        403: {"description": "Client error level 3"},
        503: {"description": "Server error level 3"},
    },
    default_response_class=ResponseLevel3,
    callbacks=callback_router3.routes,
)

router2_default.include_router(
    router4_default,
    prefix="/level3",
    tags=["level3a", "level3b"],
    dependencies=[Depends(dep3)],
    responses={
        403: {"description": "Client error level 3"},
        503: {"description": "Server error level 3"},
    },
    default_response_class=ResponseLevel3,
    callbacks=callback_router3.routes,
)

router2_default.include_router(router4_override)

router2_default.include_router(router4_default)


app.include_router(
    router2_override,
    prefix="/level1",
    tags=["level1a", "level1b"],
    dependencies=[Depends(dep1)],
    responses={
        401: {"description": "Client error level 1"},
        501: {"description": "Server error level 1"},
    },
    default_response_class=ResponseLevel1,
    callbacks=callback_router1.routes,
)

app.include_router(
    router2_default,
    prefix="/level1",
    tags=["level1a", "level1b"],
    dependencies=[Depends(dep1)],
    responses={
        401: {"description": "Client error level 1"},
        501: {"description": "Server error level 1"},
    },
    default_response_class=ResponseLevel1,
    callbacks=callback_router1.routes,
)

app.include_router(router2_override)

app.include_router(router2_default)

client = TestClient(app)
