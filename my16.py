import pandas as pd

students_grades = pd.read_excel('C:/Users/karen/Downloads/reading-and-writing-excel-files-in-python-with-pandas-grades.xlsx')
students_grades.head()
print(students_grades.head())

students_grades = pd.read_excel('C:/Users/karen/Downloads/reading-and-writing-excel-files-in-python-with-pandas-grades.xlsx', sheet_name='Grades', index_col='Grade')
print(students_grades.head())

cols = [0, 1, 3]
students_grades = pd.read_excel('C:/Users/karen/Downloads/reading-and-writing-excel-files-in-python-with-pandas-grades.xlsx', usecols=cols)
print(students_grades.head())