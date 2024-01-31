import os


file_path = "Codar-Fintech-Project/users_data.json"

with open(file_path, 'r') as user_json:
    data = user_json.read()
    print(len(data))