import sys
import os
# Ensure the Notion directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Notion.Config.notion_config import ConfigDatabase
import requests
import json



class UpdateDetail(ConfigDatabase):

    def __init__(self):
        super().__init__()
        self.url = f'https://api.notion.com/v1/databases/{self.notion_database_id}'
    

    def retrieve_databases(self):

        url = self.url + '/' + 'query'

        response = requests.post(url=url, headers=self.headers)

        if response.status_code != 200:
            raise Exception(f'Failed to retrieve databases: {response.status_code}')
        
        return response.json()
    

    def update_page(self, data:json, page_id:str):

        url = f"https://api.notion.com/v1/pages/{page_id}"
        try:
            response = requests.patch(url=url, headers=self.headers, data=json.dumps(data))
            if response.status_code != 200:
                raise Exception(f"Error updating page: {response.status_code}\n{response.text}")
            
            print("Page updated successfully")
            return response.json()
        except Exception as e:
            print(f'When trying to retrieve database information from notion database error found: {e}')
    

    def find_page_id_by_content_id(self, database, content_id):

        try:
            for page in database['results']:
                if page["properties"]["Content_id"]["title"][0]["text"]["content"] == content_id:
                    return page['id']
        except Exception as e:
            print(f'When trying to retrieve database content_id from notion database error found: {e}')
        
        return None


    def find_page_id_by_post_status(self, database):

        try:
            for page in database['results']:
                if page["properties"]['Status']['status']['name'] == 'Not Started':
                    return page['id']
            return None
        except Exception as e:
            print(f'When trying to retrieve database content_id from notion database error found: {e}')


    def update_content_generation(self, post_id, view_on_post, like_on_post, new_content, page_id):

        new_post_id = post_id
        new_view_count = view_on_post
        new_like_count = like_on_post
        new_status = 'Success'

        update_content = update_data = {
                "properties": {
                    "Post Id": {
                        "type": "rich_text",
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": new_post_id
                                }
                            }
                        ]
                    },
                    "View on Post": {
                        "number": new_view_count
                    },
                    "Like on Post": {
                        "number": new_like_count
                    },
                    "Status": {
                        "type": "status",
                        "status": {
                            "name": new_status,
                         }
                    },
                    'Content Generator':{
                        "type": "rich_text",
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": new_content
                                }
                            }
                        ]
                    }
                }
            }
        
        updated_page = self.update_page(data = update_content, page_id = page_id)