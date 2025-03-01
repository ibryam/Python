# We’ll clean the data and engineer features like "points scored vs. opponent defense strength."

import pandas as pd
import numpy as np

# Load raw data
df = pd.read_csv("west_ham_2023_raw.csv")

#---------------------------------------------------------------------------------------------------------------------#
                                        ### PREPROCESSING AND CLEANING WITH PANDAS ###
#---------------------------------------------------------------------------------------------------------------------#

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# The date field becomes 2024-05-19 15:00:00+00:00
#                        2024-05-19T15:00:00Z

# Handle missing values (e.g., games not yet played)
df = df.dropna(subset=["home_goals", "away_goals", "winner"])


# Create target variable: 1 if West Ham wins, 0 otherwise
df["west_ham_win"] = np.where(
    ((df["home_team"] == "West Ham United FC") & (df["winner"] == "HOME_TEAM")) |
    ((df["away_team"] == "West Ham United FC") & (df["winner"] == "AWAY_TEAM")), 1, 0
)


# Feature Engineering
# Goals scored by West Ham
df["west_ham_goals"] = np.where(df["home_team"] == "West Ham United FC", df["home_goals"], df["away_goals"])

# Opponent goals conceded (proxy for defense strength)
df["opponent_goals"] = np.where(df["home_team"] == "West Ham United FC", df["away_goals"], df["home_goals"])

# Rolling average of West Ham goals scored (last 5 games)
df["wh_goals_rolling"] = df["west_ham_goals"].rolling(window=5, min_periods=1).mean().shift(1)

# Rolling average of opponent defense strength (goals conceded by opponent in last 5 games)
df["opp_defense_rolling"] = df["opponent_goals"].rolling(window=5, min_periods=1).mean().shift(1)

# Feature: Points scored vs. opponent defense strength
df["wh_vs_opp_defense"] = df["wh_goals_rolling"] / (df["opp_defense_rolling"] + 1)  # Add 1 to avoid division by zero

# Select features and target
features = ["wh_goals_rolling", "opp_defense_rolling", "wh_vs_opp_defense"]
X = df[features].dropna()
y = df.loc[X.index, "west_ham_win"]

# Save preprocessed data
X.to_csv("west_ham_2023_features.csv", index=False)
y.to_csv("west_ham_2023_target.csv", index=False)
print("Preprocessed data:", X.shape, y.shape)