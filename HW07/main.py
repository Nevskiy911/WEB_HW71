from sqlalchemy import func
from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session


def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    result = (
        session.query(Student)
        .join(Grade)
        .group_by(Student)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
        .all()
    )

    return result


def select_2(discipline_name):
    # Знайти студента із найвищим середнім балом з певного предмета.
    result = (
        session.query(Student, func.avg(Grade.grade).label('avg_grade'))
        .join(Grade)
        .join(Discipline)
        .filter(Discipline.name == discipline_name)
        .group_by(Student)
        .order_by(func.avg(Grade.grade).desc())
        .first()
    )
    return result


def select_3(discipline_name):
    # Знайти середній бал у групах з певного предмета.
    result = (
        session.query(Group, func.avg(Grade.grade).label('avg_grade'))
        .join(Student)
        .join(Grade)
        .join(Discipline)
        .filter(Discipline.name == discipline_name)
        .group_by(Group)
        .all()
    )
    return result


def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    result = session.query(func.avg(Grade.grade).label('avg_grade')).scalar()
    return result


def select_5(teacher_id):
    # Знайти, які курси читає певний викладач.
    result = (
        session.query(Discipline)
        .filter(Discipline.teacher_id == teacher_id)
        .all()
    )
    return result


def select_6(group_id):
    # Знайти список студентів у певній групі.
    result = (
        session.query(Student)
        .filter(Student.group_id == group_id)
        .all()
    )
    return result


def select_7(group_id, discipline_id):
    # Знайти оцінки студентів в окремій групі з певного предмета.
    result = (
        session.query(Grade)
        .join(Student)
        .join(Discipline)
        .filter(Student.group_id == group_id, discipline_id == discipline_id)
        .all()
    )
    return result


def select_8(teacher_id):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    result = (
        session.query(func.avg(Grade.grade).label('avg_grade'))
        .join(Discipline)
        .filter(Discipline.teacher_id == teacher_id)
        .scalar()
    )
    return result


def select_9(student_id):
    # Знайти список курсів, які відвідує певний студент.
    result = (
        session.query(Discipline)
        .join(Grade)
        .join(Student)
        .filter(Student.id == student_id)
        .all()
    )
    return result


def select_10(student_id, teacher_id):
    # Список курсів, які певному студенту читає певний викладач.
    result = (
        session.query(Discipline)
        .join(Grade)
        .join(Student)
        .join(Teacher)
        .filter(Student.id == student_id, Teacher.id == teacher_id)
        .all()
    )
    return result


if __name__ == '__main__':
    # print(select_1())
    # print(select_2('Вища математика'))
    print(select_10(1, 1))
