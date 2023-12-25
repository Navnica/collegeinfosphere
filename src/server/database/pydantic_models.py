from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class Visit(BaseModelModify):
    student_id: int
    lesson_table_id: int


class Lesson(BaseModelModify):
    name: str


class Mark(BaseModelModify):
    mark: int
    student_id: int
    lesson_table_id: int


class Student(BaseModelModify):
    fullname: str
    birthdate: str
    phone: int
    password: str
    group_id: int


class Staff(BaseModelModify):
    fullname: str
    birthday: str
    phone: int
    password: str
    post_id: int


class Post(BaseModelModify):
    name: str
    power_level: int


class Miss(BaseModelModify):
    student_id: int
    lesson_table_id: int
    is_valid: bool


class LessonTable(BaseModelModify):
    date: str
    time_id: int
    lesson_id: int
    teacher_id: int
    group_id: int


class LessonTime(BaseModelModify):
    time_start: str
    time_end: str


class Group(BaseModelModify):
    name: str


class LoginData(BaseModel):
    login: str
    password: str
