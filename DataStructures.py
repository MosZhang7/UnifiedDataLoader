from dataclasses import dataclass
from datetime import datetime, date
from enum import Enum, auto

from shapely import points

# 日期类型：普通工作日|周五|周末|节前一天|节假日
class DataType(Enum):
    WORKDAY = auto()
    WEEKEND = auto()
    HOLIDAY = auto()
    DAYBEFORE = auto()
    FRIDAY = auto()






# 一个数据点的所有属性
@dataclass
class DataPointProperties:
    def __init__(self, pflow_in, timestamp,
                 date_type, weather, operation_type, event_scale):
        self.pflow_in = pflow_in
        self.timestamp = timestamp
        self.date_type = date_type
        self.weather = weather
        self.operation_type = operation_type
        self.event_scale = event_scale
        
    # def p(self):
    #     # self.pflow_in........


# 包括一天的数据点，长度由时间粒度决定，粒度为一天，则长度为1，粒度为15分钟，则长度为96/72
@dataclass
class DailyRecord:
    points:list
    # freq:int



    # # 返回内部所有点位的属性的拼接
    # def ext():
    #     x = []
    #     for p in points:
    #     # return x;


