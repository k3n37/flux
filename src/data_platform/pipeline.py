from dataclasses import dataclass


@dataclass(slots=True)
class PipelineJob:
    name: str
    source: str
    destination: str


def build_daily_jobs() -> list[PipelineJob]:
    return [
        PipelineJob(name="project_metrics", source="postgres", destination="warehouse"),
        PipelineJob(name="document_activity", source="postgres", destination="analytics-index"),
    ]


if __name__ == "__main__":
    for job in build_daily_jobs():
        print(f"{job.name}: {job.source} -> {job.destination}")
