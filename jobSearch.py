# jobSearch.py
from helper import preference
from queryBuilder import build_stripe_url
from scraper import JobScraper

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

    scraper = JobScraper()
    scraper.run_scraper(stripe_prefs)
