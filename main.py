from qa_tools.suite import TestSuite

a = TestSuite()
a.read_json()
print(a.count_passed())
print(a.slowest())

