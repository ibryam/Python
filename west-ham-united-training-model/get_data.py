# We’ll use the /matches endpoint to fetch West Ham United’s 2023 Premier League matches (competition ID: 2021 for PL).

import requests
import pandas as pd


API_TOKEN = "ADDYOURTOKEN"

# API setup
url = "https://api.football-data.org/v4/competitions/PL/matches"
headers = {"X-Auth-Token": API_TOKEN}  # Replace with your football-data.org API key
params = {
    "season": "2023",  # 2023 season
}
#---------------------------------------------------------------------------------------------------------------------#
                                        ### DATA GATHERING ###
#---------------------------------------------------------------------------------------------------------------------#

# Fetch matches
response = requests.get(url, headers=headers, params=params)
data = response.json()

# Filter for West Ham United matches ==> id = 563
matches = [m for m in data["matches"] if m["homeTeam"]["id"] == 563 or m["awayTeam"]["id"] == 563]
df = pd.DataFrame([{
    "date": m["utcDate"],
    "home_team": m["homeTeam"]["name"],
    "away_team": m["awayTeam"]["name"],
    "home_goals": m["score"]["fullTime"]["home"],
    "away_goals": m["score"]["fullTime"]["away"],
    "winner": m["score"]["winner"]  # "HOME_TEAM", "AWAY_TEAM", or "DRAW"
} for m in matches])

# Save raw data
df.to_csv("west_ham_2023_raw.csv", index=False)
print("Data gathered:", df.shape)