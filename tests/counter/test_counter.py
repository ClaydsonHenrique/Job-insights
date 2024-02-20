from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    expected_javascript_count = 122
    lowercase_javascript = "javascript"
    upper_case_javascript = "JAVASCRIPT"
    expected_python_count = 1639
    lowercase_python = "python"
    uppercase_python = "PYTHON"

    assert (
        count_ocurrences(path, lowercase_javascript)
        == expected_javascript_count
    )

    assert (
        count_ocurrences(path, upper_case_javascript)
        == expected_javascript_count
    )

    assert count_ocurrences(path, uppercase_python) == expected_python_count
    assert count_ocurrences(path, lowercase_python) == expected_python_count
