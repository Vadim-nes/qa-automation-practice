from qa_tools.suite import TestSuite
from qa_tools.models import TestResult

a = TestSuite()
# a.read_json()
# a.add(TestResult("testname One", "passed", 3.6))
# a.add(TestResult("testname Two", "failed", 4.6))
# a.add(TestResult("testname Three", "passed", 5.6))
a.save_report("data/report.json")




