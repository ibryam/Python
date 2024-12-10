import requests

parameters = {
    "amount": 999999,
    "type": "boolean",
    "difficulty": "easy"
}
response = requests.get("https://opentdb.com/api.php?", params = parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

print(question_data)