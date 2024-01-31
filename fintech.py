
file_path = "fintech-data/users_data.json"
file_path = "fintech-data/cards_data.json"

# 1. The Total number of Users (Master)
def count_users():
    """count the numbers of user details in the file"""
    with open(file_path, 'r') as user_json:
            data = user_json.read()
            
    return len(data)

# 2. The Total number of Unique Users (Abisola)
print('a test')

# 3. Average Score of all users (Pholasade)

# 4. The Total number of Cards (Emmanuel)

# 5. The Total number of Unique Cards (Lanre)


