import sqlite3

class Student():

    def __init__(self, fname, lname, slack, cohort):
        self.fname = fname
        self.lname = lname
        self.slack = slack
        self.cohort = cohort

    def __repr__(self):
        return f'Name: {self.fname} {self.lname}, Slack: {self.slack}, Cohort: {self.cohort}'

class Report():

    def __init__(self):
        self.db_path = "/Users/zanebliss/workspace/back-end/exercises/book-2/StudentExercises/student_exercises.db"

    def make_report(self):

        with sqlite3.connect(self.db_path) as conn:

            exercises = dict()

            cursor = conn.cursor()

            cursor.execute("""
            SELECT
                e.Id as ExerciseId,
                e.exercise_name,
                s.id as StudentId,
                s.first_name,
                s.last_name
            FROM Exercise e
            JOIN Student_Exercise as se on se.exercise_id = e.id
            JOIN Student as s on s.id = se.student_id;
            """)
        
            data_coll = cursor.fetchall()

            for row in data_coll:
                exercise_name = row[1]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]

                else:
                    exercises[exercise_name].append(student_name)
                
            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')
            

reports = Report()
reports.make_report()