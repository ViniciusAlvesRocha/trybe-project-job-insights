from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
        "tests/mocks/jobs.csv"
    """
    with open(path) as jobs:
        jobs_list = csv.DictReader(jobs)
        return [job for job in jobs_list]
