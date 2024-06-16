import requests

class Quotes:
    def __init__(self):
        self.base_url = 'https://api.quotable.io/random'
    
    def get_quotes(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()  # Raise an HTTPError on bad status
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
