from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
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
    data = read(path)
    salary_all = set()
    for job in data:
        if job["max_salary"] != "" and job["max_salary"] != "invalid":
            if job["max_salary"].isnumeric():
                salary_all.add(int(job["max_salary"]))
    max_value = max(salary_all)
    return max_value


def get_min_salary(path: str) -> int:
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
    data = read(path)
    salary_all = set()
    for job in data:
        if job["min_salary"] != "" and job["min_salary"] != "invalid":
            if job["min_salary"].isnumeric():
                salary_all.add(int(job["min_salary"]))
    min_value = min(salary_all)
    return min_value


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
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
    try:
        min_salary = job["min_salary"]
        max_salar = job["max_salary"]

        if int(min_salary) > int(max_salar):
            raise ValueError
        return int(salary) >= int(min_salary) and int(salary) <= int(max_salar)

    except (KeyError, ValueError, TypeError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
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
    job_list = []

    for job in jobs:
        try:
            result = matches_salary_range(job, salary)
            if result:
                job_list.append(job)
        except ValueError:
            pass

    return job_list
