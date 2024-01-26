from typing import List, Dict
import csv  

class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, newline='', encoding='utf-8') as readefile:
            reader = csv.DictReader(readefile)
            self.jobs_list = list(reader)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set(job.get('job_type') for job in self.jobs_list if 'job_type' in job)
        return list(unique_job_types)
    
    def filter_by_multiple_criteria(self, criteria: Dict) -> List[dict]:
        filter_job = []
        for job in self.jobs_list:
            if all(job.get(key) == value for key, value in criteria.items()):
                filter_job.append(job)
        return filter_job

if __name__ == "__main__":
    process_jobs = ProcessJobs()
    process_jobs.read("src/insights/jobs.py")

    unique_types = process_jobs.get_unique_job_types()
    print("Tipos únicos de trabalhos:", unique_types)
    
    criteria_to_filter = {'job_type': 'Full-time', 'location': 'Remote'}
    filtered_jobs = process_jobs.filter_by_multiple_criteria(criteria_to_filter)
    print("Trabalhos filtrados:", filtered_jobs)