from datetime import datetime, date, time, timedelta
import re
from typing import Union


class MakeObject:
    def __init__(self) -> None:
        pass

    def make_DataPointProperties():
        pass

    def make_DailyRecord(self, DataPointProperties):
        pass


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
