import argparse
from asyncio.windows_events import NULL
from hmac import new
from DataExtractor import DataExtractor
from DataStructureUtils import *
import DataStructureUtils as du
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


def main(config_name):

    config = du.choose_configuration(config_name)

    # DataExtractor需要根据一定条件提取出来需要的数据，例如根据时间排序、根据车站进行group
    raw_data_df = DataExtractor(config).load_data()

    timecdr = TIME.time()
    # 随后根据粒度转换为DailyRecord，且DailyRecord应提供一定的检查，例如长度跟粒度有关
    daily_record_map = du.make_daily_record_map(raw_data_df)
    print("timecdr:", TIME.time() - timecdr)

    print(daily_record_map)

    all_date_data_dict = {}  # 6 DailyRecord class instances

    # 发现有pd.to_datetime函数，考虑全局替换掉
    pd.to_datetime
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
    parser = argparse.ArgumentParser(description="Choose a configuration in config.json")
    parser.add_argument('name', type=str, help="configuration name in config.json")
    
    config_name = parser.parse_args().name
    main(config_name)
