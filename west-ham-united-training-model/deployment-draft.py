# We’ll use football-data.org’s live data endpoint (/matches?status=LIVE) for real-time updates.
#
# from flask import Flask, jsonify
# import pandas as pd
# import requests
# import joblib
#
# app = Flask(__name__)
# model = joblib.load("west_ham_rf_model.pkl")
# headers = {"X-Auth-Token": "YOUR_API_KEY_HERE"}
#
# def fetch_live_stats():
#     url = "https://api.football-data.org/v4/matches"
#     params = {"status": "LIVE"}
#     response = requests.get(url, headers=headers, params=params)
#     data = response.json()["matches"]
#     for match in data:
#         if match["homeTeam"]["id"] == 65 or match["awayTeam"]["id"] == 65:
#             return {
#                 "west_ham_goals": match["score"]["fullTime"]["home"] if match["homeTeam"]["id"] == 65 else match["score"]["fullTime"]["away"],
#                 "opp_goals": match["score"]["fullTime"]["away"] if match["homeTeam"]["id"] == 65 else match["score"]["fullTime"]["home"]
#             }
#     return None
#
# @app.route("/predict", methods=["GET"])
# def predict():
#     live_stats = fetch_live_stats()
#     if not live_stats:
#         return jsonify({"error": "No live West Ham game"}), 404
#
#     historical = pd.read_csv("west_ham_2023_features.csv").tail(5)
#     live_df = pd.DataFrame([live_stats])
#     features = pd.concat([historical.drop(columns=historical.columns[2:]), live_df]).tail(5)
#
#     wh_goals_rolling = features["west_ham_goals"].mean()
#     opp_defense_rolling = features["opp_goals"].mean()
#     wh_vs_opp_defense = wh_goals_rolling / (opp_defense_rolling + 1)
#
#     X_live = pd.DataFrame([[wh_goals_rolling, opp_defense_rolling, wh_vs_opp_defense]],
#                          columns=["wh_goals_rolling", "opp_defense_rolling", "wh_vs_opp_defense"])
#     prob = model.predict_proba(X_live)[0][1]
#
#     return jsonify({"west_ham_win_probability": float(prob)})
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)


# Deployment Steps
# Database: Store historical data locally (e.g., CSV or SQLite) to compute rolling averages.
# Polling: Use a scheduler (e.g., schedule library) to check for live games every 6 seconds (within 10 calls/minute limit).
# Betting Integration: Connect to a betting platform’s API or frontend to act on predictions.
# Limits: Free tier restricts live updates; a paid plan (€25/month) offers more calls and competitions.
# Challenges:
#
# No odds data in the free tier; profit estimates are hypothetical without a secondary source.
# Live updates are limited to 10 calls/minute, sufficient for periodic checks but not high-frequency betting.

# Summary
# API: Switched to football-data.org, free with no credit card required.
# Data: Fetched West Ham’s 2023 Premier League matches.
# Preprocessing: Engineered features like "points scored vs. opponent defense strength."
# Modeling: Trained a random forest model.
# Backtest: Evaluated on 2023 data, estimating profit (e.g., $400 at 55% accuracy).
# Deployment: Built a Flask app for live predictions.