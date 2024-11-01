from dataclasses import dataclass


@dataclass
class ResultModel:
    prompt: str
    response: str