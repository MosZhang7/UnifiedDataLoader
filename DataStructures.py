from enum import Enum, auto
from typing import List


# 日期类型：普通工作日|周五|周末|节前一天|节假日
class DataType(Enum):
    WORKDAY = auto()
    WEEKEND = auto()
    HOLIDAY = auto()
    DAYBEFORE = auto()
    FRIDAY = auto()


# 一个数据点的所有属性
class DataPointProperties:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)  # 动态添加成员变量

    def concatenate_members(self):
        return list(self.__dict__.values())


# 包括一天的数据点，长度由时间粒度决定，粒度为一天，则长度为1，粒度为15分钟，则长度为96/72
class DailyRecord:

    def __init__(self):
        # self.time = time
        self.data_points: List[DataPointProperties] = []

    # 返回内部所有点位的属性的拼接
    def concatenate(self):
        daily_result = []
        for point in self.data_points:
            daily_result.extend(point.concatenate_members())
        return daily_result
