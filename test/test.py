from DataStructureUtils import *


def testD1_1():
    # 示例调用
    print(parse_to_timestamp("2024-09-10"))  # 输出：2024-09-10 (date对象)
    print(
        parse_to_timestamp("2024/09/10 06:00:00")
    )  # 输出：2024-09-10 06:00:00 (datetime对象)
    print(
        parse_to_timestamp("20240910060000")
    )  # 输出：2024-09-10 06:00:00 (datetime对象)
    print(
        parse_to_timestamp("2024-01-31 23:55:00")
    )  # 输出：2024-09-10 06:00:00 (datetime对象)
    # assert a == date(2024,9,10)


# testD1_1()


import pandas as pd
import time


# 定义学生类
class Student:
    def __init__(self, student_id, score):
        self.student_id = student_id
        self.score = score

    def __repr__(self):
        return f"Student(id={self.student_id}, score={self.score})"

ft = time.time()

ids = pd.Series(range(1, 1000001))  # id 从 1 到 100000
scores = pd.Series([i % 100 for i in range(1, 1000001)])  # 分数从 0 到 99 循环


# 计时开始
start_time = time.time()

# 使用 zip() 和列表生成式创建 10 万个 Student 对象
students = [Student(student_id, score) for student_id, score in zip(ids, scores)]

# 计时结束
end_time = time.time()

# 输出耗时
print(f"操作耗时: {start_time - ft} 秒")
print(f"操作耗时: {end_time - start_time} 秒")

# 打印前 5 个学生对象
print(students[:5])
