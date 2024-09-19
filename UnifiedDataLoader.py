from asyncio.windows_events import NULL
from hmac import new
from ConfigUtils import ConfigUtils
from DataExtractor import DataExtractor
from DataStructureUtils import *
import DataStructureUtils
from DataStructures import *
import time as TIME
import json
import pandas as pd

import DataStructures

# global MIN_NUM
# MIN_NUM = {function,
#            function}


class UnifiedDataLoader:
    """
    功能：
        1、能从csv里读取

        2、能从不同的数据库里读取
            （1）连接不同的数据库
            （2）SQL语句的拼接：写在不同函数里，不同类型的项目调用不同函数（要用一个单独的类处理）
            （3）执行SQL语句获取数据
        3、 1，2步骤得到方便处理的各种类(结构体)
    """

    def __init__(self):
        pass


def main():
    config = json.load(open("./config.json", "r"))
    configUtils = ConfigUtils(config)
    raw_data = DataExtractor(config).load_data()
    dp = MakeObject.make_DataPointProperties(raw_data,raw_data,raw_data)
    dr = MakeObject.make_DailyRecord()

    time_start = TIME.time()
    print("time consume:", TIME.time() - time_start)
    D = [
        [1, 2, 3, 4, 5, 6, 7],
        [2 + i for i in range(7)],
        [3 + i for i in range(7)],
        [4 + i for i in range(7)],
        [5 + i for i in range(7)],
        [6 + i for i in range(7)],
    ]
    T = [
        [datetime(2023, 3, 31, 6, 0) + timedelta(minutes=15 * i) for i in range(7)],
        [datetime(2023, 4, 1, 6, 0) + timedelta(minutes=15 * i) for i in range(7)],
        [datetime(2023, 4, 2, 6, 0) + timedelta(minutes=15 * i) for i in range(7)],
        [datetime(2024, 4, 3, 6, 0) + timedelta(minutes=15 * i) for i in range(7)],
        [datetime(2024, 4, 4, 6, 0) + timedelta(minutes=15 * i) for i in range(7)],
        [datetime(2024, 4, 5, 6, 0) + timedelta(minutes=15 * i) for i in range(7)],
    ]

    weather_info = [0, 2, 4, 1, 1, 3]

    date_type_info = [0, 1, 2, 0, 1, 2, 3, 2]
    all_T = [
        date(2023, 3, 31),
        date(2023, 4, 1),
        date(2023, 4, 2),
        date(2023, 4, 3),
        date(2023, 4, 4),
        date(2024, 4, 5),
        date(2024, 4, 6),
        date(2024, 4, 7),
    ]

    all_date_data_dict = {}  # 6 DailyRecord class instances

    for i in range(len(D)):
        daily_record = []
        for j in range(len(D[0])):
            data_point = DataPointProperties(
                D[i][j], T[i][j], date_type_info[i], weather_info[i], None, None
            )
            daily_record.append(data_point)
        daily_record_class = DailyRecord(daily_record)
        all_date_data_dict[T[i][0].date()] = daily_record_class

    # print(all_date_data_dict)

    predict_time = parse_to_timestamp("2024-04-06")
    date_ind = all_T.index(predict_time)
    date_type = date_type_info[date_ind]

    if date_type == 1 or date_type == 2:
        # 近期历史：14天
        # 历史节假日：节假日期间（？天）+节前历史14天

        # 历史年份的节假日日期及节前一天，
        # read from table

        his_date_list_tmp = [date(2023, 4, 1), date(2023, 4, 2)]

        # 遍历每年的节前一天，找到它的历史14天

        # 找到今年的节假日（预测日期）的历史14天
        # timedelta for计算

        # 以上组成key，value对，key为年份，value为年份对应的日期列表

        # 按照指定的历史年份排列，拼接对应的历史日期
        his_year_list = [2023, 2023, 2023, 2024]

    else:
        # 近期历史：90天
        his_len = 2
        his_date_list = [
            predict_time - timedelta(days=i) for i in range(his_len, 0, -1)
        ]
        for his_date in his_date_list:
            oneday = all_date_data_dict[his_date.date()]
            oneday.ext()


if __name__ == "__main__":
    main()
