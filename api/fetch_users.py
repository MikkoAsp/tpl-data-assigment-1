import requests
from configuration import API_URL
from database.connection import session_local
from database.models import User
from sqlalchemy.exc import SQLAlchemyError
from data_protection.data_masking import name_masking, last_two_digits

#Fething users from the https://jsonplaceholder.typicode.com/users API
def fetch_users():
    try:
        response = requests.get(API_URL, timeout=15) #Timeout after 15 seconds -> don't wait for response forever
        response.raise_for_status() #Raise the HTTP error
        users = response.json()
        return users
    except requests.exceptions.Timeout:
        print("API didn't respond quick enough")
    except requests.exceptions.HTTPError as e:
        print("API returned HTTP error:", e)
    except requests.exceptions.JSONDecodeError:
        print("API didn't return JSON")
    except requests.exceptions.RequestException as e:
        print("API error:", e)

    return None



# Save users to the database. Existing users (same id) are updated, so no duplicates are created.
def save_users(users):
    try:
        with session_local() as session:
            for u in users:
                user = User(
                    id=u["id"],
                    name=name_masking(u["name"]),
                    username=u["username"],
                    email=u["email"],
                    phone=last_two_digits(u["phone"]),
                    website=u["website"],
                    city=u["address"]["city"],
                    company_name=u["company"]["name"]
                )
                session.merge(user)  # merge avoids duplicate key errors
            session.commit()
            return True
    except SQLAlchemyError as e:
        print("Database error, couldn't save users:", e)
        return False