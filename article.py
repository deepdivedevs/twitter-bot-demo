from dataclasses import dataclass

@dataclass
class Article:
    author: str
    link: str
    published: str
    summary: str
    title: str