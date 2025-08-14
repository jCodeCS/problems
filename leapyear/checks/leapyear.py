import check50
import check50.python

@check50.check()
def exists():
    """leapyear.py exists"""
    check50.exists("leapyear.py")

@check50.check(exists)
def has_function():
    """is_leap_year function is defined"""
    student = check50.python.import_("leap_year.py")
    if not hasattr(student, "is_leap_year"):
        raise check50.Failure("Function 'is_leap_year' is not defined.")

@check50.check(has_function)
def test_true_2024():
    """is_leap_year(2024) returns True"""
    student = check50.python.import_("leap_year.py")
    assert student.is_leap_year(2024) is True, "Expected True for 2024"

@check50.check(has_function)
def test_false_1900():
    """is_leap_year(1900) returns False"""
    student = check50.python.import_("leap_year.py")
    assert student.is_leap_year(1900) is False, "Expected False for 1900"

@check50.check(has_function)
def test_true_1600():
    """is_leap_year(1600) returns True"""
    student = check50.python.import_("leap_year.py")
    assert student.is_leap_year(1600) is True, "Expected True for 1600"

@check50.check(has_function)
def test_true_2000():
    """is_leap_year(2000) returns True"""
    student = check50.python.import_("leap_year.py")
    assert student.is_leap_year(2000) is True, "Expected True for 2000"

@check50.check(has_function)
def test_false_2019():
    """is_leap_year(2019) returns False"""
    student = check50.python.import_("leap_year.py")
    assert student.is_leap_year(2019) is False, "Expected False for 2019"

@check50.check(has_function)
def test_true_2400():
    """is_leap_year(2400) returns True"""
    student = check50.python.import_("leap_year.py")
    assert student.is_leap_year(2400) is True, "Expected True for 2400"

@check50.check(has_function)
def test_false_2100():
    """is_leap_year(2100) returns False"""
    student = check50.python.import_("leap_year.py")
    assert student.is_leap_year(2100) is False, "Expected False for 2100"
