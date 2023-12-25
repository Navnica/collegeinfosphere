from src.server.database import models as database_models
from src.server.database import pydantic_models
from src.server.service import *

routers = (
    RouterManager(
        database_model=database_models.Visit,
        pydantic_model=pydantic_models.Visit
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Lesson,
        pydantic_model=pydantic_models.Lesson
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Mark,
        pydantic_model=pydantic_models.Mark
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Student,
        pydantic_model=pydantic_models.Student
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Staff,
        pydantic_model=pydantic_models.Staff
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Post,
        pydantic_model=pydantic_models.Post
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Miss,
        pydantic_model=pydantic_models.Miss
    ).fastapi_router,

    RouterManager(
        database_model=database_models.LessonTable,
        pydantic_model=pydantic_models.LessonTime
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Group,
        pydantic_model=pydantic_models.Group
    ).fastapi_router,
)


def find_router_by_tag(rt: list, tag: str):
    for r in rt:
        if r.tags[0] == tag:
            return r
