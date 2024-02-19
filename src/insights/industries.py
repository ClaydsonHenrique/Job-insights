from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unique_industries = set()
        for job in self.jobs_list:
            industry = job.get("industry")
            if industry:
                unique_industries.add(industry)
        return list(unique_industries)
