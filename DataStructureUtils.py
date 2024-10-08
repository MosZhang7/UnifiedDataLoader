from collections import defaultdict
from datetime import datetime, date, time, timedelta
import json
import re
from typing import Union
import pandas as pd

from DataStructures import DailyRecord, DataPointProperties, DataType


def choose_configuration(config_name):
    config_file = json.load(open("./config.json", "r"))
    configurations = config_file["configurations"]
    print("\nUnifiedDataLoader version[{}] Start!\n".format(config_file["version"]))
    for config in configurations:
        if config["name"] == config_name:
            print("Using config [{}]".format(config_name))
            return config
    print("Can not find config [{}], use the first config!".format(config_name))
    return configurations[0]


"""
    返回time前days天的日期序列
"""

"""
    用于把时间戳字符串转换成datetime/date类型，使用单正则表达式匹配
"""


def parse_to_timestamp(timestamp_str: str) -> Union[datetime, date, time]:
    # 定义一个正则表达式，匹配日期和可选时间
    date_pattern = re.compile(
        r"(?P<year>\d{4})[-/]?"  # 年份，支持 - 或 /
        r"(?P<month>\d{2})[-/]?"  # 月份，支持 - 或 /
        r"(?P<day>\d{2})"  # 日期
        r"(?:[\sT]?"  # 可选的时间分隔符 (空格 或 T)
        r"(?P<hour>\d{2}):?"  # 小时 (可选)，支持 HH:
        r"(?P<minute>\d{2}):?"  # 分钟 (可选)，支持 MM:
        r"(?P<second>\d{2})?)?"  # 秒 (可选)，支持 SS
    )

    match = date_pattern.match(timestamp_str)

    if match:
        # 提取年、月、日
        year = int(match.group("year"))
        month = int(match.group("month"))
        day = int(match.group("day"))

        # 提取时间部分（如果存在）
        hour = match.group("hour")
        minute = match.group("minute")
        second = match.group("second")

        if year and month and day and hour and minute and second:
            # 如果匹配到了时间部分，返回 datetime 对象
            return datetime(year, month, day, int(hour), int(minute), int(second))
        elif year and month and day:
            # 如果没有时间部分，只返回 date 对象
            return date(year, month, day)
        else:
            return time(hour, minute, second)

    # 如果无法匹配，返回 None
    return None


# 传入可变数量的list，判断长度是否全部相等
def check_equal_length(*lists):
    if not lists:
        return False  # 如果没有传入任何列表，返回 True（空输入视为长度相等）

    # 获取第一个列表的长度
    first_length = len(lists[0])

    # 判断所有列表的长度是否与第一个列表相同
    return all(len(lst) == first_length for lst in lists)


def series_to_list(*series: pd.Series):
    return [s.tolist() for s in series]


# 使用原始数据的DataFrame转换为DailyRecordMap
# 为了方便程序最终的输出，data_type这种本应属于`DailyRecord`的也被添加到`DataPointProperties`，
# 后续如果需要考虑内存、性能因素，可以在`DataExtractor.load()`处针对dp和dr分别返回`DataFrame`
def make_daily_record_map(dataframe: pd.DataFrame):

    dp_prop = dataframe.columns.tolist()
    # 按日期分组
    dataframe["date"] = pd.to_datetime(dataframe["query_time"]).dt.date
    grouped = dataframe.groupby("date")

    # 筛选、填充等操作
    # ...
    daily_record_map = defaultdict(DailyRecord)

    for group_day, group in grouped:
        # data_type这种本应该属于DailyRecord的属性可以为了方便，全都加到DataPointProperties里
        data_points = [
            DataPointProperties(**{prop: row[i] for i, prop in enumerate(dp_prop)})
            for row in group[dp_prop].values
        ]
        daily_record_map[group_day].data_points.extend(data_points)

    return daily_record_map


# 计算返回日期类型，如节假日，工作日等
def get_data_type(predict_time):
    return DataType.WORKDAY
