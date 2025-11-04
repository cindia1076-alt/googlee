# get_fact.py

import requests
import json

def fetch_random_fact():
    """
    Connects to the uselessfacts API, fetches a random fact, and returns it.
    """
    # Define the API endpoint URL
    api_url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    try:
        # Send a GET request to the API
        response = requests.get(api_url)
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status() 
        
        # Parse the JSON response into a Python dictionary
        data = response.json()
        
        # Extract the fact text from the dictionary
        fact = data.get('text')
        
        if fact:
            return fact
        else:
            return "Error: Could not find the 'text' key in the API response."

    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, etc.
        return f"Error: Could not connect to the API. {e}"
    except json.JSONDecodeError:
        # Handle cases where the response is not valid JSON
        return "Error: Failed to decode the JSON response from the API."

# --- Main execution block ---
if __name__ == "__main__":
    print("Fetching a random fact... 🚀")
    random_fact = fetch_random_fact()
    print("\n✅ Here is your fact:")
    print(random_fact)