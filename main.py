# jobSearch.py
from helper import preference
from queryBuilder import build_stripe_url
from scraper import JobScraper
# ----- Constants -----
not_interested_words = [
    "manager", "director", "senior", "lead", "architect",
    "principal", "vp", "staff", "it", "head"
]


# ----- Execution -----

if __name__ == "__main__":

    stripe_prefs = preference(
        url=build_stripe_url(),
        companyName="Stripe",
        base_url="https://stripe.com",
        not_interested=not_interested_words
    )
    preferencelist = [stripe_prefs]

    for prefs in preferencelist:
        print(f"Searching for jobs at {prefs.companyName}...")
        scraper = JobScraper(prefs)
        scraper.run()
        