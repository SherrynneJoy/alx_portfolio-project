#!/usr/bin/python3
"""file for testing crud operations for user"""
# from models.user import User
from user_controllers import create_user, get_user_by_id # db_setup
# from db_setup import session


# 1. Create a User
create_user("test_user", "test@example.com", "password123")

# 2. Retrieve the User
user = get_user_by_id(1)  # Assuming the newly created user has an ID of 1

# Verify if the user was retrieved successfully
if user:
    print("User retrieved successfully:", user)
else:
    print("User not found.")

# 3. Update User Information (Optional)
if user:
    user.email = "new_email@example.com"
    session.commit()
    print("User information updated successfully.")

# 4. Delete User (Optional)
if user:
    session.delete(user)
    session.commit()
    print("User deleted successfully.")
