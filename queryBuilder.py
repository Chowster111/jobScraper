from urllib.parse import urlencode
def build_stripe_url():
    base_url = "https://stripe.com/jobs/search"
    
    params = {
        "query": "Engineer",
        "teams": [
            "Banking as a Service", "Climate", "Connect", "Crypto", "Data & Data Science",
            "Data Platform", "Infrastructure & Corporate Tech", "Mobile",
            "Money Movement and Storage", "New Financial Products", "Payments",
            "Platform", "Professional Services", "Revenue & Financial Automation",
            "Security", "Stripe Tax", "Tech Programs", "Terminal", "University"
        ],
        "remote_locations": [
            "North America--Canada Remote", "North America--Mexico Remote", "North America--US Remote"
        ],
        "office_locations": [
            "North America--Atlanta", "North America--Chicago", "North America--Mexico City",
            "North America--New York", "North America--San Francisco Bridge HQ",
            "North America--Seattle", "North America--South San Francisco",
            "North America--Toronto", "North America--Washington DC"
        ]
    }
    
    return f"{base_url}?{urlencode(params, doseq=True)}"