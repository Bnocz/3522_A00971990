from enum import Enum
import json

class FileExtensions(Enum):
    TXT = 1
    JSON = 2


class FileHandler:

    @staticmethod
    def load_data(path):
        with open(path, "r", encoding='utf-8') as json_data:
            json_dict = json.load(json_data)
            return json_dict
    @staticmethod
    def write_lines(path, lines):
        with open(path, "a", encoding="utf-8") as prev_queries:
            prev_queries.writeline(lines)
