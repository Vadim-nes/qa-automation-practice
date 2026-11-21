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
        return max(valid, key = lambda r: r.duration).duration

    def failed(self):
        """Возвращает список тестов со статусом failed."""
        return sum(1 for result in self.result if result.status == "failed")

    def summary (self):
        dict_common = {}

        if not self.result:
            dict_common["total"] = 0.0
            dict_common["pass_rate"] = 0.0
            dict_common["slowest"] = None
            dict_common["passed"] = 0
            dict_common["failed"] = 0
            return dict_common

        else:
            dict_common["total"] = len(self.result)
            dict_common["passed"] = self.count_passed()
            dict_common["failed"] = self.failed()
            dict_common["pass_rate"] =  round(dict_common.get("passed") / dict_common.get("total") * 100,1)
            dict_common["slowest"] = self.slowest()
            return dict_common

    def save_report(self,path):
        payload = self.summary()

        with open (path, "w", encoding = "utf-8") as f:
            try:
                json.dump(payload, f, indent = 2, ensure_ascii= False)
            except OSError as ex:
                print(f"Ошибка записи файла {ex}")


if __name__ == "__main__":
        suite = TestSuite()
        suite.add(TestResult("t1", "passed", 1.0))
        suite.add(TestResult("t2", "failed", 2.0))

        assert suite.summary()  == {'total': 2, 'passed': 1, 'failed': 1, 'pass_rate': 50, 'slowest': 2.0}

        suite2 = TestSuite()
        suite2.summary()
        assert suite2.summary() == {'total': 0, 'passed': 0, 'failed': 0, 'pass_rate': 0.0, 'slowest': None}

        print(suite.summary())
        print(suite2.summary())

