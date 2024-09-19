import json
import pandas as pd


class DataExtractor:
    def __init__(self, config) -> None:
        self.path = config["data_path"]

    def load_data(self):
        data = 123
        csv = CSVExtractor()
        df = pd.read_csv(self.path, index_col=False)
        print(df.head())
        return data


class SQLQueryBuilder:
    def __init__(self) -> None:
        pass

    def build_from_json(self):
        pass

    def build_from_ini(self):

        pass


class CSVExtractor:
    def __init__(self) -> None:
        pass
