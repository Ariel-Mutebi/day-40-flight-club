import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

# It talks to Sheety, so sheet-talker :)
class SheetTalker:
    def __init__(self):
        self._USERNAME = os.environ.get("SHEETY_USERNAME")
        self._PASSWORD = os.environ.get("SHEETY_PASSWORD")
        self._AUTHORISATION = HTTPBasicAuth(self._USERNAME, self._PASSWORD)
        self._DESTINATIONS_ENDPOINT = os.environ.get("SHEETY_DESTINATIONS_ENDPOINT")
        self._USERS_ENDPOINT = os.environ.get("SHEETY_USERS_ENDPOINT")

    def get_destinations(self):
        request = requests.get(self._DESTINATIONS_ENDPOINT, auth=self._AUTHORISATION)
        request.raise_for_status()
        response = request.json()
        return response["destinations"]

    def get_users_emails(self):
        request = requests.get(self._USERS_ENDPOINT, auth=self._AUTHORISATION)
        request.raise_for_status()
        response = request.json()
        users = response["users"]
        emails = []
        for user in users:
            emails.append(user["what'sYourEmail?"])
        return emails