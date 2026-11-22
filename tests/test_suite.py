from qa_tools.models import TestResult
from qa_tools.suite import TestSuite

def test_count_passed():
    actual = TestSuite()
    actual.add(TestResult("testname One","passed", 3.6))
    actual.add(TestResult("testname Two","failed", 4.6))
    actual.add(TestResult("testname Three","passed", 5.6))

    assert actual.count_passed() == 2

# 6. test_slowest_empty: пустой набор даёт None.
def test_slowest_empty():
    actual = TestSuite()

    assert actual.slowest() is None
