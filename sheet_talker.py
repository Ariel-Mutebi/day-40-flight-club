import os
import requests
from dotenv import load_dotenv

load_dotenv()

# It talks to Sheety, so sheet-talker :)
class SheetTalker:
    def __init__(self):
        self.SHEETY_DESTINATIONS_ENDPOINT = os.environ.get("SHEETY_DESTINATIONS_ENDPOINT")

    def get_destinations(self):
        request = requests.get(self.SHEETY_DESTINATIONS_ENDPOINT)
        request.raise_for_status()
        response = request.json()
        return response["prices"]
