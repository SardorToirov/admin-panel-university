from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def table_exists(table_name):
    """ Jadval bazada mavjudligini tekshiradi """
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=%s;", [table_name])
        return cursor.fetchone() is not None


def get_faculties():
    if table_exists("adminapp_faculty"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM adminapp_faculty")
            return dictfetchall(cursor)
    return []


def get_kafedra():
    if table_exists("adminapp_kafedra"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM adminapp_kafedra")
            return dictfetchall(cursor)
    return []


def get_guruh():
    if table_exists("adminapp_guruh"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM adminapp_guruh")
            return dictfetchall(cursor)
    return []


def get_subject():
    if table_exists("adminapp_subject"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM adminapp_subject")
            return dictfetchall(cursor)
    return []


def get_teacher():
    if table_exists("adminapp_teacher"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM adminapp_teacher")
            return dictfetchall(cursor)
    return []


def get_student():
    if table_exists("adminapp_student"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM adminapp_student")
            return dictfetchall(cursor)
    return []
