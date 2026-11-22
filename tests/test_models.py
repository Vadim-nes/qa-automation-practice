import pytest

from qa_tools.models import TestResult
from qa_tools.models import FailedResult

def test_is_passed_true():
    assert TestResult("firstname", "passed", 33.6).is_passed() == True

def test_is_passed_false():
    assert TestResult("firstname", "False", 33.6).is_passed() == False

@pytest.mark.parametrize(
    ["a","result"],[
(1.0, False),
(2.0, False),
(2.1, True)
    ]
)
def test_is_slow(a, result):
    assert TestResult("vad", "passed",a).is_slow() == result
# В test_models.py:

def test_failed_result_str():
     assert "Execution error. Please retest..." in  str(FailedResult("test1", "failed",4.32, "Execution error. Please retest..."))