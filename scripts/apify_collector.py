import os
import sys
import json
import urllib.request

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN")

def check_account():
    if not APIFY_TOKEN:
        print("[Apify Notice] APIFY_API_TOKEN is not set in environment or .env file.")
        return None
    url = f"https://api.apify.com/v2/users/me?token={APIFY_TOKEN}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            return data.get("data", {})
    except Exception as e:
        print("Error checking Apify account:", e)
        return None

def fetch_actor_runs():
    if not APIFY_TOKEN:
        return []
    url = f"https://api.apify.com/v2/acts?token={APIFY_TOKEN}&desc=true&limit=10"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode()).get("data", {}).get("items", [])
    except Exception as e:
        print("Error fetching actors:", e)
        return []

if __name__ == "__main__":
    acc = check_account()
    if acc:
        print(f"[Apify Connected] User: {acc.get('email', 'Authenticated User')} | Plan: Active")
    else:
        print("[Apify Notice] Please configure APIFY_API_TOKEN in .env file to use scraping features.")
