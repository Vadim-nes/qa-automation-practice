class TestResult:
    def __init__(self, name, status, duration):
        self.status = status
        self.duration = duration
        self.name = name

    def is_passed(self):
        return self.status == "passed"

    def __str__(self):
        return f"{self.name}: {self.status} ({self.duration} s)"
    def __repr__(self):
        return f"name = {self.name}, status = {self.status}, duration = {self.duration} s)"

    def is_slow(self, limit=2.0):
        return self.duration > limit

class FailedResult(TestResult):

    def __init__(self, name, status, duration, error_message):
        super().__init__(name, status, duration)
        self.error_message= error_message

    def __str__(self):
        original = super().__str__()
        return  f"original: {original} + added a custom line {self.error_message}"