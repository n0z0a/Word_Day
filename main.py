import json

with open("words_meanings.json", "r") as file:
    data = json.load(file)  # Load JSON data

if "words" in data and isinstance(data["words"], list):
    first_five_words = [entry["word"] for entry in data["words"][:5]]
    print(first_five_words)
else:
    print("Invalid JSON structure.")