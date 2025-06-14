# helper.py
from datetime import datetime
import pytz

class Job:
    def __init__(self, company, title, url, location="N/A", team="N/A", detected_at=None):
        self.company = company
        self.title = title
        self.url = url
        self.location = location
        self.team = team
        eastern = pytz.timezone("US/Eastern")
        detected_at = datetime.now(eastern).strftime("%Y-%m-%d %I:%M %p %Z")
        self.detected_at = detected_at

    def __str__(self):
        return (
            f"[{self.company}] {self.title}\n"
            f"Location: {self.location} | Team: {self.team}\n"
            f"URL: {self.url}\n"
            f"First seen: {self.detected_at}"
        )

    def to_dict(self):
        return {
            "company": self.company,
            "title": self.title,
            "url": self.url,
            "location": self.location,
            "team": self.team,
            "detected_at": self.detected_at
        }

class preference:
    def __init__(self, url, companyName, not_interested=None, keywords=None, base_url=None):
        self.url = url
        self.companyName = companyName
        self.base_url = base_url or ""
        self.keywords = keywords if keywords else []
        self.not_interested = not_interested if not_interested else []

    def __str__(self):
        return (
            f"Company: {self.companyName}\n"
            f"Base URL: {self.base_url}\n"
            f"Keywords: {self.keywords}\n"
            f"Not Interested: {self.not_interested}\n"
        )
