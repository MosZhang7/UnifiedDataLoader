import pandas as pd
import timeit

# 定义学生类
class Student:
    def __init__(self, student_id, score):
        self.student_id = student_id
        self.score = score

# 定义使用 pandas.Series 的方法
def series_method():
    ids = pd.Series(range(1000000))
    scores = pd.Series([i % 100 for i in range(1000000)])
    students = [Student(student_id, score) for student_id, score in zip(ids, scores)]

# 定义使用 Python 列表的同样方法
def list_method():
    ids = list(range(1000000))
    scores = [i % 100 for i in range(1000000)]
    students = [Student(student_id, score) for student_id, score in zip(ids, scores)]

# 使用 timeit 计时 pandas.Series 的耗时
series_time = timeit.timeit(series_method, number=10)
print(f"使用 pandas.Series 的时间: {series_time} 秒")

# 使用 timeit 计时 Python list 的耗时
list_time = timeit.timeit(list_method, number=10)
print(f"使用 Python list 的时间: {list_time} 秒")
