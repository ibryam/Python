# We’ll train a random forest classifier on the preprocessed data.

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load preprocessed data
X = pd.read_csv("west_ham_2023_features.csv")
y = pd.read_csv("west_ham_2023_target.csv").values.ravel()

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train random forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Save model
import joblib
joblib.dump(rf_model, "west_ham_rf_model.pkl")
print("Model trained and saved.")