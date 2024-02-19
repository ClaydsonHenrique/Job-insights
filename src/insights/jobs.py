from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, encoding="utf-8") as readefile:
            reader = csv.DictReader(readefile)
            self.jobs_list = list(reader)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set(
            job.get("job_type") for job in self.jobs_list if "job_type" in job
        )
        return list(unique_job_types)

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], criteria: Dict
    ) -> List[dict]:
        if not isinstance(criteria, dict):
            raise TypeError("O filtro deve ser um dicionário")

        filtered_jobs = []
        for job in jobs:
            if all(job.get(key) == value for key, value in criteria.items()):
                filtered_jobs.append(job)
        return filtered_jobs
