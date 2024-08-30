import sys
import os
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Facebook.Config.refresh_facebook_token import ConfigFacebook 

class UpdateFacebook(ConfigFacebook):

    def __init__(self):
        super().__init__()

    def like_count(self, post_id):
        """
        This function retrieves the number of likes for a given Facebook post.

        Parameters:
        access_token (str): The access token for the Facebook Graph API.
        post_id (str): The ID of the Facebook post.

        Returns:
        int: The number of likes for the post. If the post has no likes, returns 0.

        Raises:
        requests.exceptions.RequestException: If there is an error with the HTTP request.
        """

        url = f'https://graph.facebook.com/{post_id}?fields=likes.summary(true)&access_token={self.ACCESS_TOKEN}'
        response = requests.get(url)
        data = response.json()

        return (0 if data is None else len(data['likes']['data']))

    def view_count(self, post_id):
        """
        This function retrieves the number of unique views for a given Facebook post.

        Parameters:
        access_token (str): The access token for the Facebook Graph API.
        post_id (str): The ID of the Facebook post.

        Returns:
        int: The number of unique views for the post. If the post has no views, returns 0.

        Raises:
        requests.exceptions.RequestException: If there is an error with the HTTP request.
        """

        # Construct the URL for the Graph API endpoint to retrieve post impressions
        url = f'https://graph.facebook.com/{post_id}/insights/post_impressions_unique?access_token={self.ACCESS_TOKEN}'
        
        # Send a GET request to the Graph API endpoint
        response = requests.get(url)
        
        # Parse the response as JSON
        data = response.json()

        # If the data is not empty, return the number of unique views
        # Otherwise, return 0
        return (0 if len(data['data']) < 1 else data['data'][0]['values'][0]['value'])
