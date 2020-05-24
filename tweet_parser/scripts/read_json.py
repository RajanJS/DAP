import json

with open('./files/person.json') as f:
    # with open('./dap_project/nys_tweets_filtered_2017_0.json') as f:
    data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)
