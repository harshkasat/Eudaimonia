import sys
import os
# Ensure the Notion directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Notion.Config.notion_config import ConfigDatabase
import requests
import json


class GetPage(ConfigDatabase):

    def __init__(self):
        super().__init__()
        self.url = f'https://api.notion.com/v1/databases/{self.notion_database_id}/query'

    def get_page(self):

        try:

            req = requests.post(url=self.url, headers=self.headers)

            result = req.json()
            # print(result['results'][0]['properties']['Prompt'])

            # For Facebook Post
            image_path = result['results'][0]['properties']['Files & media']['files'][0]['file']['url']
            prompt_description = result['results'][0]['properties']['Prompt']['rich_text'][0]['text']['content']

            # Facebook log and Status

            date_of_post = result['results'][0]['properties']['Date of Post']['last_edited_time']
            post_status = result['results'][0]['properties']['Status']['status']['name']
            post_id = result['results'][0]['properties']['Post Id']['rich_text'][0]['text']['content']
            view_on_post = result['results'][0]['properties']['View on Post']['rich_text'][0]['text']['content']
            like_on_post = result['results'][0]['properties']['Like on Post']['rich_text'][0]['text']['content']
            content_id = result['results'][0]["properties"]["Content_id"]["title"][0]["text"]["content"]

            json_response = json.dumps({"image_path": image_path,
                      "prompt_description": prompt_description})
            

            return json_response
        
        except Exception as e:
            print(f'When trying to retrieve database information from notion database error found: {e}')





res = GetPage().get_page()
print(res)
