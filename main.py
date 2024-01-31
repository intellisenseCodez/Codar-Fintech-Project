<<<<<<< HEAD
import fintech

print("ANALYSIS QUESTION")
print(f"1. The Total number of Users is {fintech.count_users()}")
=======
import os


file_path = "Codar-Fintech-Project/users_data.json"

with open(file_path, 'r') as user_json:
    data = user_json.read()
    print(len(data))
>>>>>>> Abisola-branch
