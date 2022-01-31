from src.sorting import sort_by

import pytest

jobs = [
    {"min_salary": 1, "max_salary": 2, "date_posted": "2021-01-20"},
    {"min_salary": 3, "max_salary": 4, "date_posted": "2021-01-19"},
    {"min_salary": 5, "max_salary": 6, "date_posted": "2021-01-18"},
]

min_salary = [
    {"min_salary": 1, "max_salary": 2, "date_posted": "2021-01-20"},
    {"min_salary": 3, "max_salary": 4, "date_posted": "2021-01-19"},
    {"min_salary": 5, "max_salary": 6, "date_posted": "2021-01-18"},
]

max_salary = [
    {"min_salary": 5, "max_salary": 6, "date_posted": "2021-01-18"},
    {"min_salary": 3, "max_salary": 4, "date_posted": "2021-01-19"},
    {"min_salary": 1, "max_salary": 2, "date_posted": "2021-01-20"},
]

date_posted = [
    {"min_salary": 1, "max_salary": 2, "date_posted": "2021-01-20"},
    {"min_salary": 3, "max_salary": 4, "date_posted": "2021-01-19"},
    {"min_salary": 5, "max_salary": 6, "date_posted": "2021-01-18"},
]


def test_sort_by_criteria():
    with pytest.raises(TypeError):
        sort_by(jobs, "test1", "test2")

    sort_by(jobs, "min_salary")
    assert jobs == min_salary

    sort_by(jobs, "max_salary")
    assert jobs == max_salary

    sort_by(jobs, "date_posted")
    assert jobs == date_posted
