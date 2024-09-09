from DataStructureUtils import *


def testD1_1():
    # 示例调用
    a = parse_to_timestamp("2024-09-10")          # 输出：2024-09-10 (date对象)
    b = parse_to_timestamp("2024/09/10 06:00:00") # 输出：2024-09-10 06:00:00 (datetime对象)
    c = parse_to_timestamp("20240910060000")      # 输出：2024-09-10 06:00:00 (datetime对象)
    # assert a == date(2024,9,10)
    print('testD1_1 OK')