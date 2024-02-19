from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salarys = [
            int(job["max_salary"])
            for job in self.jobs_list
            if job["max_salary"].isdigit()
        ]
        return max(max_salarys) if max_salarys else 0

    def get_min_salary(self) -> int:
        min_salarys = [
            int(job["min_salary"])
            for job in self.jobs_list
            if job.get("min_salary", "").isdigit()
        ]
        return min(min_salarys) if min_salarys else 0

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        min_salary = job.get("min_salary", "")
        max_salary = job.get("max_salary", "")

        if (
            not isinstance(min_salary, (int, str))
            or not isinstance(max_salary, (int, str))
            or not str(min_salary).isdigit()
            or not str(max_salary).isdigit()
            or int(max_salary) <= int(min_salary)
            or not str(salary).lstrip("-").isdigit()
        ):
            raise ValueError("Invalid salary range or salary value")

        return int(min_salary) <= int(salary) <= int(max_salary)

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
