from bs4 import BeautifulSoup
import requests
from helper import Job, preference
from queryBuilder import build_stripe_url


class JobScraper(object):
    def __init__(self):
        pass

    def print_jobs(self, job):
        if not job:
            print("No jobs found.")
            return
        
        for j in job:
            print(j)
            print("-" * 40)
        
        print(f"Total jobs found for {job[0].company}: {len(job)}")
        print("-" * 40)


    def fetch_jobs(self, prefs):
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

            # Include if it contains "engineer" and excludes blocked words
            if "engineer" in title_lower and not any(word in title_lower for word in prefs.not_interested):
                jobs.append(Job(prefs.companyName, title, url, location, team))

        return jobs


# ----- Execution -----

if __name__ == "__main__":
    not_interested_words = [
        "manager", "director", "senior", "lead", "architect",
        "principal", "vp", "staff", "it", "head"
    ]

    stripe_prefs = preference(
        url=build_stripe_url(),
        companyName="Stripe",
        base_url="https://stripe.com",
        not_interested=not_interested_words
    )

    scraper= JobScraper()
    jobs = scraper.fetch_jobs(stripe_prefs)
    scraper.print_jobs(jobs)