#File: AutomaticTests.py

from CustomFunctions import *
from os import system


def fibonacci_test_exception(n, error_type):
    error_raised = False
    try:
        fibonacci(n)
    except error_type:
        error_raised = True
    except Exception:
        pass
    if not error_raised:
        print("Test fibonacci({}) failed. Expected error: {}."
              .format(n, error_type))


def fibonacci_test_normal(n, expected_output):
    try:
        actual_output = fibonacci(n)
        assert actual_output == expected_output
    except AssertionError:
        failure_description = "Test fibonacci({}) failed."\
            + " Expected output: {}; actual output: {}."
        print(failure_description.format(n, expected_output, actual_output))


def run_fibonacci_tests():
    fibonacci_test_exception(-1, ValueError)
    fibonacci_test_normal(0, 0)
    fibonacci_test_normal(1, 1)
    fibonacci_test_normal(2, 1)
    fibonacci_test_normal(3, 2)
    fibonacci_test_normal(10, 55)


def float_to_string_test_normal(float_number, precision, expected_output):
    try:
        actual_output = floatNumberToString(float_number, precision)
        assert actual_output == expected_output
    except AssertionError:
        failure_description = "Test floatNumberToString({}, {}) failed."\
            + " Expected output: {}; actual output: {}."
        print(failure_description
              .format(float_number, precision, expected_output, actual_output))


def run_float_to_string_tests():
    float_to_string_test_normal(7.123456, -1, "7")
    float_to_string_test_normal(-7.123456, 0, "-7")
    float_to_string_test_normal(7.123456, 1, "7.1")
    float_to_string_test_normal(-7.123456, 2, "-7.12")
    float_to_string_test_normal(7, 3, "7")
    float_to_string_test_normal(11.0, 0, "11")
    float_to_string_test_normal(11.0, 1, "11.0")
    float_to_string_test_normal(11.0, 2, "11.0")


def gcd_test_exception(a, b, error_type):
    error_raised = False
    try:
        greatestCommonDivisor(a, b)
    except error_type:
        error_raised = True
    except Exception:
        pass
    if not error_raised:
        failure_description = "Test greatestCommonDivisor({}, {})"\
            + " failed. Expected error: {}."
        print(failure_description.format(a, b, error_type))


def gcd_test_normal(a, b, expected_output):
    try:
        actual_output = greatestCommonDivisor(a, b)
        assert actual_output == expected_output
    except AssertionError:
        failure_description = "Test greatestCommonDivisor({}, {})"\
            + " failed. Expected output: {}; actual output: {}."
        print(failure_description
              .format(a, b, expected_output, actual_output))


def run_gcd_tests():
    gcd_test_exception(7.123456, 2, ValueError)
    gcd_test_exception(2, 7.123456, ValueError)
    gcd_test_normal(-1, 2, 1)
    gcd_test_normal(2, -1, 1)
    gcd_test_normal(0, 7, -1)
    gcd_test_normal(7, 0, -1)
    gcd_test_normal(1, 8, 1)
    gcd_test_normal(8, 1, 1)
    gcd_test_normal(23, 19, 1)
    gcd_test_normal(36, 32, 4)


def lcm_test_normal(a, b, expected_output):
    try:
        actual_output = leastCommonMultiple(a, b)
        assert actual_output == expected_output
    except AssertionError:
        failure_description = "Test leastCommonMultiple({}, {})"\
            + " failed. Expected output: {}; actual output: {}."
        print(failure_description.format(a, b, expected_output, actual_output))


def run_lcm_tests():
    lcm_test_normal(-1, 3, 3)
    lcm_test_normal(3, -1, 3)
    lcm_test_normal(0, 5, -1)
    lcm_test_normal(5, 0, -1)
    lcm_test_normal(6, 4, 12)


def leap_year_test_exception(year, expected_error):
    error_raised = False
    try:
        isLeapYear(year)
    except expected_error:
        error_raised = True
    except Exception:
        pass
    if not error_raised:
        print("Test isLeapYear({}) failed. Expected error: {}."
              .format(year, expected_error))


def leap_year_test_normal(year, expected_output):
    try:
        actual_output = isLeapYear(year)
        assert actual_output == expected_output
    except AssertionError:
        failure_description = "Test isLeapYear({}) failed."\
            + " Expected output: {}; actual output: {}."
        print(failure_description.format(year, expected_output, actual_output))


def run_leap_year_tests():
    leap_year_test_exception(0, ValueError)
    leap_year_test_normal(-400, True)
    leap_year_test_normal(-100, False)
    leap_year_test_normal(-4, True)
    leap_year_test_normal(-1, False)
    leap_year_test_normal(1, False)
    leap_year_test_normal(4, True)
    leap_year_test_normal(100, False)
    leap_year_test_normal(400, True)


def run_tests():
    run_fibonacci_tests()
    run_float_to_string_tests()
    run_gcd_tests()
    run_lcm_tests()
    run_leap_year_tests()


if __name__ == "__main__":
    print("The tests will begin.")
    run_tests()
    print("The tests are done.")
    system("pause")
