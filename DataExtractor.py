import json
import pandas as pd
import DataStructureUtils as du


class DataExtractor:
    def __init__(self, config) -> None:
        self.data_path = config["data_path"]
        # self.weather_path = config["weather_path"]

    def load_data(self):
        time_series, pflow_series = CSVExtractor(self.data_path).load()
        print("read time_series | pflow_series from {}".format(self.data_path))
        # weather = CSVExtractor(self.path).load()
        # operation_type = SQLQueryBuilder()
        # return data, weather, operation_type
        return du.series_to_list(time_series, pflow_series)


class SQLQueryBuilder:
    def __init__(self) -> None:
        pass

    def load(self):
        pass

    def build_from_json(self):
        pass

    def build_from_ini(self):

        pass


class CSVExtractor:
    def __init__(self, path) -> None:
        self.path = path

    def load(self):
        # 添加读取条件
        df = pd.read_csv(self.path, index_col=False)
        time_series = df["query_time"]
        pflow_series = df["inNums"]
        return time_series, pflow_series
