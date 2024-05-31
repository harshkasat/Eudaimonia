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

    def main(self, content_id, new_post_id, new_view_count, new_like_count, new_status):
        try:
            database = self.retrieve_databases()
            page_id = self.find_page_id_by_content_id(database, content_id)

            if not page_id:
                raise Exception(f"No page found with Content_id: {content_id}")
        except Exception as e:
            print(f'When trying to retrieve database information from notion database error found: {e}')
        

        try:
            update_data = {
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
                        "type": "rich_text",
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": new_view_count
                                }
                            }
                        ]
                    },
                    "Like on Post": {
                        "type": "rich_text",
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": new_like_count
                                }
                            }
                        ]
                    },
                    "Status": {
                        "type": "status",
                        "status": {
                            "name": new_status,
                         }
                    }
                }
            }

            updated_page = self.update_page(data = update_data, page_id = page_id)

        except Exception as e:
            print(f'When trying to retrieve database information from notion database error found: {e}')


# Example usage
if __name__ == "__main__":
    content_id = "2"  # Replace with the Content_id of the row you want to update
    new_post_id = "NEW_POST_ID"  # Replace with the new Post ID
    new_view_count = "NEW_VIEW_COUNT"  # Replace with the new View on Post
    new_like_count = "NEW_LIKE_COUNT"  # Replace with the new Like on Post
    new_status = "In Progress"  # Replace with the new Status

    UpdateDetail().main(content_id, new_post_id, new_view_count, new_like_count, new_status)

# res = UpdateDetail().main('1', '123', '1234r43', '12345876543', 'In Progress')