import pandas as pd
import DataStructureUtils as du


class DataExtractor:
    def __init__(self, config) -> None:
        self.data_path = config["data_path"]
        # self.weather_path = config["weather_path"]

    def load_data(self):
        cols = ["query_time", "inNums"]
        df = CSVExtractor(self.data_path).load(cols)
        print("get columns{} from [{}]".format(cols, self.data_path))

        # weather = CSVExtractor(self.path).load()
        # print("get columns{} from [{}]".format(cols, self.data_path))
        # operation_type = SQLQueryBuilder()
        # print("get [operation_type] by execute SQL {}".format(self.data_path))

        # if du.check_equal_length(time_series, pflow_series) == False:
        #     print("error source data lenth!")
        #     # 也可以选择在这里填充缺失的值
        #     exit()

        print("final df struct:*************")
        print(df.head())
        print("final df struct:*************")

        return df


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

    def load(self, cols):
        # 添加读取条件
        df = pd.read_csv(self.path, usecols=cols)
        # 添加过滤条件
        # ...
        return df
