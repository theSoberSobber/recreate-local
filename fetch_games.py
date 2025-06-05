import json
import requests
import os

# Supabase credentials
SUPABASE_URL = "https://hqlgppguxhqeaonjzinv.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhxbGdwcGd1eGhxZWFvbmp6aW52Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzI2MjYwNDQsImV4cCI6MjA0ODIwMjA0NH0.4LuWk4qxp0NRZ5_erEIJq5BHq5qZiSE4zTUFS1ioZw8"

# Fetch games from Supabase using the RPC function
def fetch_games():
    url = f"{SUPABASE_URL}/rest/v1/rpc/get_apps_ordered_by_title"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching games: {response.status_code} - {response.text}")
        return []

# Main execution
if __name__ == "__main__":
    games = fetch_games()
    if games:
        # Create the recreate directory if it doesn't exist
        os.makedirs("recreate", exist_ok=True)
        with open("recreate/data.json", "w") as f:
            json.dump(games, f, indent=2)
        print("Games fetched and saved to data.json successfully!")
    else:
        print("No games fetched. Check your Supabase connection.") 