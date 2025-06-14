# scraper.py
import os
import json
import requests
from bs4 import BeautifulSoup
from helper import Job
from mailer import Mailer

class JobScraper(object):
    def __init__(self, prefs, seen_file="jobs.json"):
        self.prefs = prefs
        self.seen_file = f"./jobsFound/{prefs.companyName.lower()}_{seen_file}"
        self.seen_jobs = self._load_seen_jobs()

    def _load_seen_jobs(self):
        if os.path.exists(self.seen_file):
            with open(self.seen_file, "r") as f:
                return json.load(f)
        return {}

    def _save_seen_jobs(self):
        with open(self.seen_file, "w") as f:
            json.dump(self.seen_jobs, f, indent=2)

    def _update_seen(self, newJobs=None):
        if newJobs:
            for job in newJobs:
                self.seen_jobs[job.url] = job.to_dict()
        self._save_seen_jobs()

    def _get_new_jobs(self, jobs):
        new_jobs = []
        for job in jobs:
            if job.url not in self.seen_jobs:
                new_jobs.append(job)
        return new_jobs

    def print_jobs(self, job_list):
        if not job_list:
            print("No jobs found.")
            return

        for j in job_list:
            print(j)
            print("-" * 40)

        print(f"Found {len(job_list)} new jobs at {self.prefs.companyName}:\n")
        print("-" * 40)

    def _fetch_jobs(self, prefs):
        response = requests.get(prefs.url)
        if response.status_code != 200:
            print(f"Failed to retrieve jobs: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = []

        for row in soup.find_all('tr', class_='TableRow'):
            title_tag = row.find('a', class_='Link JobsListings__link')
            if not title_tag:
                continue

            title = title_tag.get_text(strip=True)
            url = prefs.base_url + title_tag['href']

            location_tag = row.find('span', class_='JobsListings__locationDisplayName')
            location = location_tag.get_text(strip=True) if location_tag else "N/A"

            team_tag = row.find('li', class_='JobsListings__departmentsListItem')
            team = team_tag.get_text(strip=True) if team_tag else "N/A"

            title_lower = title.lower()

            if "engineer" in title_lower and not any(word in title_lower for word in prefs.not_interested):
                jobs.append(Job(prefs.companyName, title, url, location, team))

        return jobs

    def _format_job(self, job):
        return f"{job.title}\n{job.location} | {job.team}\n{job.url}\nFirst seen: {job.detected_at}\n"


    def _sendmail(self, new_jobs):
            body = "\n\n".join([self._format_job(job) for job in new_jobs])
            subject = f"Job Scraper: [{self.prefs.companyName}] {len(new_jobs)} new job(s) posted!"
            
            mailer = Mailer()
            mailer.send_email_notification(subject, body)
            print("✅ Email notification sent!")

    def run(self):
        jobs = self._fetch_jobs(self.prefs)
        new_jobs = self._get_new_jobs(jobs)

        if new_jobs:
            print(f"\n📬 {len(new_jobs)} NEW jobs found!\n")
            self.print_jobs(new_jobs)
            self._update_seen(new_jobs)
            self._sendmail(new_jobs)

        else:
            print(f"No new jobs found today for {self.prefs.companyName}.")
            self._sendmail([])  # Send an email even if no new jobs found, to keep the user informed
        
