import json
from pathlib import Path
from qa_tools.models import TestResult


class TestSuite:
    PATH_TO_FILE = "data/results.json"

    def __init__(self):
        self.result = []



    def add(self, results: TestResult):
        """Добавляет один TestResult в набор."""
        self.result.append(results)



    def read_json(self):
        """Читает JSON и добавляет в набор объекты TestResult."""
        pathlib_link = Path(__file__).parent.parent /  self.PATH_TO_FILE

        try:
            with open (pathlib_link, "r", encoding = "utf-8") as f:
                data = json.load(f)


        except FileNotFoundError as error:
            print(f"file not found in {pathlib_link.resolve()} . Error: {error}")
            return

        except json.JSONDecodeError as error:
            print(f"file is broken  in {pathlib_link.resolve()} . Error: {error}")
            return

        for item in data:
            self.add(TestResult(
                name=item.get("name"),
                status=item.get("status"),
                duration=item.get("duration"),
            ))

    def count_passed(self):
        """Возвращает число пройденных тестов."""
        return sum(1 for i in self.result if i.is_passed())



    def slowest(self):
        """ Этот метод Возвращает самый долгий тест или None, если подходящих нет."""
        valid = [i for i in self.result if isinstance(i.duration, (int, float))]
        if not valid:
            return None
        return max(valid, key = lambda r: r.duration)

if __name__ == "__main__":
        suite = TestSuite()
        suite.read_json()
        print(suite.count_passed())
        print(suite.slowest())