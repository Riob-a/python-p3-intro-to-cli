#!/usr/bin/env python3
def create_grade_report(student_grades):
    #w = overwrite, a = append
    with open('lib/reports2.txt', 'a') as gr:
        for grade in student_grades:
             # add '\n' to write grades on separate lines
            gr.write(grade + '\n')

if __name__ == '__main__':
    student_grades = []

    grade = input("Student name, grade: ")
    while grade:
        student_grades.append(grade)
        #end when no grade is entered
        grade = input("Student name, grade: ")

    create_grade_report(student_grades)
