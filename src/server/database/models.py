import peewee
import settings

db: peewee.SqliteDatabase = peewee.SqliteDatabase(f'{settings.DATABASE_PATH}{settings.DATABASE_NAME}')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Group(BaseModel):
    name: peewee.CharField = peewee.CharField(default='')


class Student(BaseModel):
    fullname: peewee.CharField = peewee.CharField(default='')
    birthdate: peewee.CharField = peewee.CharField(default='')
    phone: peewee.IntegerField = peewee.IntegerField(default=0)
    password: peewee.CharField = peewee.CharField(default='')
    group_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Group, related_name='student_group_id', default=0)


class Lesson(BaseModel):
    name: peewee.CharField = peewee.CharField(default='')


class LessonTime(BaseModel):
    date_start: peewee.CharField = peewee.CharField(default='')
    date_end: peewee.CharField = peewee.CharField(default='')


class Post(BaseModel):
    name: peewee.CharField = peewee.CharField(default='')
    power_level: peewee.IntegerField = peewee.IntegerField(default=1)


class Staff(BaseModel):
    fullname: peewee.CharField = peewee.CharField(default='')
    birthdate: peewee.CharField = peewee.CharField(default='')
    phone: peewee.IntegerField = peewee.IntegerField(default=0)
    password: peewee.CharField = peewee.CharField(default='')
    post_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Post, related_name='staff_post_id', default=0)


class LessonTable(BaseModel):
    date: peewee.CharField = peewee.CharField(default='')
    time_id: peewee.ForeignKeyField = peewee.ForeignKeyField(LessonTime, related_name='lesson_table_time_id', default=0)
    lesson_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Lesson, related_name='lesson_table_lesson_id', default=0)
    teacher_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Lesson, related_name='lesson_table_teacher_id', default=0)
    group_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Group, related_name='lesson_table_group_id', default=0)


class Miss(BaseModel):
    student_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Student, related_name='miss_student_id', default=0)
    lesson_table_id: peewee.ForeignKeyField = peewee.ForeignKeyField(LessonTable, related_name='miss_lesson_table_id', default=0)
    is_valid: bool = peewee.BooleanField(default=False)


class Visit(BaseModel):
    student_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Student, related_name='visit_student_id', default=0)
    lesson_table_id: peewee.ForeignKeyField = peewee.ForeignKeyField(LessonTable, related_name='visit_lesson_table_id', default=0)


class Mark(BaseModel):
    mark: peewee.IntegerField = peewee.IntegerField(default=1)
    student_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Student, related_name='mark_student_id', default=0)
    lesson_table_id: peewee.ForeignKeyField = peewee.ForeignKeyField(LessonTable, related_name='mark_lesson_table_id', default=0)


db.create_tables([
    Group,
    Student,
    LessonTime,
    Lesson,
    LessonTable,
    Mark,
    Visit,
    Miss,
    Staff,
    Post
])
