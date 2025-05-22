import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.SHEETY_API_ENDPOINT = os.environ.get("SHEETY_API_ENDPOINT")

    def get_destinations(self):
        request = requests.get(self.SHEETY_API_ENDPOINT)
        request.raise_for_status()
        response = request.json()
        return response["prices"]
