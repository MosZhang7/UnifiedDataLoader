import timeit
import pandas as pd

# 假设有两个长度为 10 万的 Series
ids = pd.Series(range(1, 100001))  # id 从 1 到 100000
scores = pd.Series([i % 100 for i in range(1, 100001)])  # 分数从 0 到 99 循环


# 定义学生类
class Student:
    def __init__(self, student_id, score):
        self.student_id = student_id
        self.score = score

    def __repr__(self):
        return f"Student(id={self.student_id}, score={self.score})"


# 使用 zip() 和列表生成式创建 10 万个 Student 对象
students = [Student(student_id, score) for student_id, score in zip(ids, scores)]

# 打印前 5 个学生对象
print(students[:5])


# 测试 zip 的性能
def zip_method():
    ids = list(range(3000000))
    scores = [i % 100 for i in range(3000000)]
    result = [Student(id, score) for id, score in zip(ids, scores)]


# 测试手动 for 循环的性能
def manual_for_loop():
    ids = list(range(3000000))
    scores = [i % 100 for i in range(3000000)]
    result = []
    for i in range(len(ids)):
        result.append(Student(ids[i], scores[i]))


# 测试 zip 的耗时
zip_time = timeit.timeit(zip_method, number=10)
print(f"使用 zip 的时间: {zip_time} 秒")

# 测试手动 for 循环的耗时
manual_time = timeit.timeit(manual_for_loop, number=10)
print(f"使用手动 for 循环的时间: {manual_time} 秒")
