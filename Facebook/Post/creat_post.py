import os
import sys
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Facebook.Config.refresh_facebook_token import ConfigFacebook
from LLM.Llm_endpoint.llm_get_content import RetrieveEndpoint
from Notion.GetPageDetail.get_image_n_prompt import GetPage


class CreatePost(ConfigFacebook):

    def __init__(self):
        self.image_path = "image_downloads/" + 'image.png'
        ConfigFacebook().refresh_token()
        super().__init__()

    
    def post_image_and_message(self, message):

        try:
            url = 'https://graph.facebook.com/v11.0/me/photos'

            file = open(self.image_path, 'rb')
            image_file = {
                'image_path':file,
            }

            data = {
                'access_token':self.ACCESS_TOKEN,
                'message':f"""{message}""",
            }

            response = requests.post(url=url, data=data, files=image_file)
            response_json = (response.json())

            if 'id' in response_json:
                print(f"Post created successfully with ID: {response_json['id']}")
            else:
                raise Exception(f"Error posting image and message: {response_json}")
            
            return response_json['id']
        
        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            file.close()
            os.remove(self.image_path)
            print("Image file deleted successfully.")
