from datetime import datetime

class Job:
    """A class to represent a job posting."""
    def __init__(self, company, title, url, location=None, team=None, detected_at=None):
        self.company = company
        self.title = title
        self.url = url
        self.location = location if location else "N/A"
        self.team = team if team else "N/A"
        self.detected_at = detected_at or datetime.utcnow().isoformat()

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"URL: {self.url}\n"
            f"Location: {self.location}\n"
            f"Team: {self.team}\n"
            f"Detected At: {self.detected_at}\n"
        )

    def to_dict(self):
        """Convert job to dictionary (e.g., for JSON storage)."""
        return {
            "title": self.title,
            "url": self.url,
            "location": self.location,
            "team": self.team,
            "detected_at": self.detected_at
        }

class preference:
    """A class to represent user/company-specific job board preferences."""
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
