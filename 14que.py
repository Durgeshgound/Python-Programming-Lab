#Write a program to perform dictionary operations (add, update,delete).

# 1. Create a dictionary
info = {
    "Name": "Durgesh",
    "Age": 19,
    "City": "Sagar"
}
print(f"Initial: {info}")

# 2. Add a new key-value pair
info["Email"] = "bca@example.com"
print(f"After Adding: {info}")

# 3. Update an existing value
info["Age"] = 20
print(f"After Update: {info}")

# 4. Delete a key-value pair
del info["City"]
print(f"After Delete: {info}")

