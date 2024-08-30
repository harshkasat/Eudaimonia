import requests
from dotenv import load_dotenv, set_key
import os
import time

# Load environment variables from .env file
load_dotenv()

class ConfigFacebook(object):

    def __init__(self) -> None:

        try:
            self.APP_ID = os.getenv('FACEBOOK_APP_ID')
            self.APP_SECRET = os.getenv('FACEBOOK_APP_SECRET')
            self.ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN')
            self.GRAPH_API_VERSION = 'v11.0'
            self.token_created_time = float(os.getenv('TOKEN_CREATED_TIME', 0))  # Retrieve last token creation time


            if self.ACCESS_TOKEN is None or self.APP_ID is None or self.APP_SECRET is None:
                raise ValueError ("Facebook access token, app id or app secret is not given")

        except ValueError:
            raise ValueError ("Facebook access token, app id or app secret is invalid")
    
    def get_long_lived_token(self, short_lived_token):
        url = f'https://graph.facebook.com/{self.GRAPH_API_VERSION}/oauth/access_token'
        params = {
            'grant_type': 'fb_exchange_token',
            'client_id': self.APP_ID,
            'client_secret': self.APP_SECRET,
            'fb_exchange_token': short_lived_token
        }
        response = requests.get(url, params=params)
        return response.json()

    def refresh_token(self):
        # Check if 40 minutes have passed since the last token creation
        current_time = time.time()
        if current_time - self.token_created_time >= 40 * 60:
            long_lived_token_response = self.get_long_lived_token(self.ACCESS_TOKEN)
            if 'access_token' in long_lived_token_response:
                new_token = long_lived_token_response['access_token']
                # Update the .env file with the new token
                set_key('.env', 'FACEBOOK_ACCESS_TOKEN', new_token)
                set_key('.env', 'TOKEN_CREATED_TIME', str(current_time))
                self.ACCESS_TOKEN = new_token  # Update current token
                self.token_created_time = current_time # Update token creation time
                return new_token
            else:
                raise Exception('Error refreshing token: ' + str(long_lived_token_response))
        else:
            print("Token refresh not required yet. Using the existing token.")
            return self.ACCESS_TOKEN
