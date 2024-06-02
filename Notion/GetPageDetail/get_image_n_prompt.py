import sys
import os
# Ensure the Notion directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Notion.UpdatePageDetail.update_detail import UpdateDetail
import requests
import json


class GetPage(UpdateDetail):

    def __init__(self):
        super().__init__()
        self.url = f'https://api.notion.com/v1/databases/{self.notion_database_id}'

    def get_page(self):

        try:

            database = self.retrieve_databases()
            page_id = self.find_page_id_by_post_status(database)

            if not page_id:
                raise Exception(f"No page found with Failed Status:")

            url = f"https://api.notion.com/v1/pages/{page_id}"

            try:
                response = requests.get(url=url, headers=self.headers)

                if response.status_code != 200:
                    raise Exception(f"Error updating page: {response.status_code}\n{response.text}")

                response = (response).json()
                
                image_path = response['properties']['Files & media']['files'][0]['file']['url']
                prompt_description = response['properties']['Prompt']['rich_text'][0]['text']['content']

                result = {"image_path": image_path, 
                "prompt_description": prompt_description,
                "page_id":page_id}

                return (result)

            except Exception as e:
                print(f'When trying to retrieve database information from notion database error found: {e}')
        except Exception as e:
            print(f'When trying to retrieve database information from notion database error found: {e}')
