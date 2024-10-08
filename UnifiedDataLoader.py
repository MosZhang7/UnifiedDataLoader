import argparse
from DataExtractor import DataExtractor
from DataStructureUtils import *
from DataStructures import *
import time as TIME
import pandas as pd


"""
功能：
    1、能从csv里读取

    2、能从不同的数据库里读取
        （1）连接不同的数据库
        （2）SQL语句的拼接：写在不同函数里，不同类型的项目调用不同函数（要用一个单独的类处理）
        （3）执行SQL语句获取数据
    3、 1，2步骤得到方便处理的各种类(结构体)
"""


def main(config_name):
    config = choose_configuration(config_name)

    # DataExtractor需要根据一定条件提取出来需要的数据
    raw_data_df = DataExtractor(config).load_data()

    timecdr = TIME.time()
    # DailyRecord应提供一定的处理检查，例如根据时间排序、根据车站进行group，长度跟粒度有关，缺失的能够自己补充等
    daily_record_map = make_daily_record_map(raw_data_df)
    print("timecdr:", TIME.time() - timecdr)

    # 发现有pd.to_datetime函数，考虑全局替换掉
    # pd.to_datetime
    predict_time = parse_to_timestamp("2024-02-11")
    # date_ind = all_T.index(predict_time)
    date_type = get_data_type(predict_time)
    print("predict date type: ", date_type)

    if date_type == DataType.FRIDAY or date_type == DataType.HOLIDAY:
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
        his_len = 2  # 从配置文件获得
        # his_date_list = [
        #     predict_time - timedelta(days=i) for i in range(his_len, 0, -1)
        # ]
        result = []
        for i in range(his_len):
            target_date = predict_time - timedelta(days=i)
            result.extend(daily_record_map[target_date].concatenate())
        print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Choose a configuration in config.json"
    )
    parser.add_argument("name", type=str, help="configuration name in config.json")

    config_name = parser.parse_args().name
    main(config_name)
