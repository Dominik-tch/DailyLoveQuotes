import requests

REPO = "dominik-tch/DailyLoveQuotes"
BRANCH = "main"

def get_remote_commit():
    url = f"https://api.github.com/repos/{REPO}/commits/{BRANCH}"
    response = requests.get(url)
    print(response.json()["sha"])
    if response.status_code == 200:
        return response.json()["sha"]
    else:
        raise Exception("Fehler beim Abrufen des Remote-Commits.")
    
get_remote_commit()