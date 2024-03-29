import sqlite3


class Cohort():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

class Instructor():

    def __init__(self, first, last, handle, specialty, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.specialty = specialty
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'


class Exercises():

    def __init__(self, exercise, programminglanguage):
        self.exercise = exercise
        self.programminglanguage = programminglanguage

    def __repr__(self):
        return f'{self.exercise} uses the programming language {self.programminglanguage}'

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'


class StudentExerciseReports():
    def __init__(self):
        self.db_path = "/Users/marywest/workspace/python/Student/se.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Student(
            row[1], row[2], row[3], row[5]
        )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)

    def all_instructors(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Instructor(
            row[1], row[2], row[3], row[5], row[6],
)

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.FirstName,
                i.LastName,
                i.SlackHandle,
                i.Specialty,
                i.CohortId,
                c.Name
            from Instructor i
            join Cohort c on i.CohortId = c.Id
            order by i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor)

    def all_cohorts(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Cohort(
            row[1],
        )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name
            from Cohort c
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)

    def all_exercises(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercises(
            row[1], row[2],
        )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Exercise,
                e.Programminglanguage
            from Exercises e
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

    def all_javascript(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercises(
            row[1], row[2],
        )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Exercise,
                e.Programminglanguage
            from Exercises e
            WHERE Programminglanguage = "Javascript"
            """)

            all_javascript = db_cursor.fetchall()

            for exercise in all_javascript:
                print(exercise)

    def all_python(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercises(
            row[1], row[2],
        )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Exercise,
                e.Programminglanguage
            from Exercises e
            WHERE Programminglanguage = "Python"
            """)

            all_python = db_cursor.fetchall()

            for exercise in all_python:
                print(exercise)

    def all_csharp(self):

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercises(
            row[1], row[2],
        )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Exercise,
                e.Programminglanguage
            from Exercises e
            WHERE Programminglanguage = "C#"
            """)

            all_csharp = db_cursor.fetchall()

            for exercise in all_csharp:
                print(exercise)

    def exercise_dic(self):

            with sqlite3.connect(self.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                select e.Id ExerciseId,
                    e.Exercise,
                    s.Id,
                    s.FirstName,
                    s.LastName
                from Exercises e
                join StudentExercise se on se.ExerciseId = e.Id
                join Student s on s.Id = se.StudentId
            """)

                dataset = db_cursor.fetchall()

                exercises = dict()

                for row in dataset:
                    exercise_id = row[0]
                    exercise_name = row[1]
                    student_id = row[2]
                    student_name = f'{row[3]} {row[4]}'

                    if exercise_name not in exercises:
                        exercises[exercise_name] = [student_name]
                    else:
                        exercises[exercise_name].append(student_name)

                for exercise_name, students in exercises.items():
                    print(exercise_name)
                    for student in students:
                        print(f'\t* {student}')


    def instrexercise_dic(self):

# Instructor exercise table created and formatted correctly

            with sqlite3.connect(self.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                select e.Id ExerciseId,
                    e.Exercise,
                    i.Id,
                    i.FirstName,
                    i.LastName
                from Exercises e
                join InstructorExercise ie on ie.ExerciseId = e.Id
                join Instructor i on i.Id = ie.InstructorId
            """)

                dataset = db_cursor.fetchall()

                instructors = dict()

                for row in dataset:
                    exercise_id = row[0]
                    exercise_name = row[1]
                    instructor_id = row[2]
                    instructor_name = f'{row[3]} {row[4]}'

                    if instructor_name not in instructors:
                        instructors[instructor_name] = [exercise_name]
                    else:
                        instructors[instructor_name].append(exercise_name)

                for instructors, exercises  in instructors.items():
                    print(instructors)
                    for exercise in exercises:
                         print(f'\t* {exercise}')


reports = StudentExerciseReports()


# reports.all_students()
# reports.all_cohorts()
# reports.all_exercises()
# reports.all_instructors()
# reports.all_javascript()
# reports.all_csharp()



# reports.exercise_dic()

reports.instrexercise_dic()


# reports.all_python()

# student = Student('Bart', 'Simpson', '@bart', 'Cohort 8')
# print(f'{student.first_name} {student.last_name} is in {student.cohort}')


# instructor = Instructor('Bart', 'Simpson', '@bart', 'Cohort 8','dad jokes')
# print(f'{instructor.first_name} {instructor.last_name} is in {instructor.cohort}')

# cohort = Cohort('Cohort 8')
# print(f'{cohort.name}')

# exercises = Exercises('Movie History','Javascript' )
# print(f'{exercises.exercise} {exercises.programminglanguage}')




