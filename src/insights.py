import csv
from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    types_jobs = []
    jobs = read(path)
    for job in jobs:
        if not job["job_type"] in types_jobs:
            types_jobs.append(job["job_type"])

    return types_jobs


print(get_unique_job_types("src/jobs.csv"))


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    with open(path) as jobs:
        industries = []
        jobs_list = csv.DictReader(jobs)
        for job in jobs_list:
            if not job["industry"] in industries and job["industry"] != "":
                industries.append(job["industry"])
    return industries


# print(get_unique_industries("src/jobs.csv"))


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return [job for job in jobs if job["industry"] == industry]


# print(filter_by_industry("src/jobs.csv"))


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    with open(path) as jobs:
        max_salary = 0
        jobs_list = csv.DictReader(jobs)
        for job in jobs_list:
            if job["max_salary"].isdigit():
                if int(job["max_salary"]) > max_salary:
                    max_salary = int(job["max_salary"])
    return max_salary
#  print(get_max_salary("src/jobs.csv"))  # 383416


#  print(get_max_salary("tests/mocks/jobs_with_salaries.csv"))


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    with open(path) as jobs:
        jobs_list = csv.DictReader(jobs)
        min_salary = get_max_salary(path)
        for job in jobs_list:
            if job["min_salary"].isdigit():
                if int(job["min_salary"]) < min_salary:
                    min_salary = int(job["min_salary"])
    return min_salary


#  print(get_min_salary("src/jobs.csv"))
#  print(get_min_salary("tests/mocks/jobs_with_salaries.csv"))


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if (
        "max_salary" not in job or
        "min_salary" not in job or
        type(job["max_salary"]) != int or
        type(job["min_salary"]) != int or
        type(salary) != int or
        job["max_salary"] < job["min_salary"]
    ):
        raise ValueError

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
