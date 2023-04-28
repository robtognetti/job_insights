from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences('data/jobs.csv', 'python') == 1639
    assert count_ocurrences('data/jobs.csv', 'PyThoN') == 1639
    assert count_ocurrences('data/jobs.csv', 'PYTHON') == 1639
    assert count_ocurrences("data/jobs.csv", "Javascript") == 122
    assert count_ocurrences("data/jobs.csv", "javascript") == 122
    assert count_ocurrences("data/jobs.csv", "JAVASCRIPT") == 122
