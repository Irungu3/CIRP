import requests
import json
from bs4 import BeautifulSoup

class ReconFetch:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def linkedin_scrape(self, profile_url):
        """Scrape public LinkedIn profiles."""
        response = requests.get(profile_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract public profile details
        name = soup.find("title").text if soup.find("title") else "Not found"
        return {"profile_url": profile_url, "name": name}

    def save_results(self, data, filename="results.json"):
        """Save results to a JSON file."""
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    recon = ReconFetch()
    
    # Example usage
    linkedin_data = recon.linkedin_scrape("https://www.linkedin.com/in/example/")
    
    results = {"linkedin": linkedin_data}
    recon.save_results(results)
    print("Results saved to results.json")

