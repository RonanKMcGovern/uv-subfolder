"""Simple script to fetch data using requests."""
import requests

def fetch_random_user():
    """Fetch a random user from the RandomUser API."""
    try:
        response = requests.get('https://randomuser.me/api/', timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        user_data = response.json()
        
        # Extract and print some user information
        user = user_data['results'][0]
        print(f"Name: {user['name']['first']} {user['name']['last']}")
        print(f"Email: {user['email']}")
        print(f"Country: {user['location']['country']}")
        
        return user
    except requests.RequestException as e:
        print(f"Error fetching user data: {e}")
        return None

def main():
    """Main function to run the script."""
    print("Fetching a random user...")
    fetch_random_user()