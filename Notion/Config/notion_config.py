import os


class ConfigDatabase(object):

    def __init__(self):

        try:

            try:
                self.notion_access_token = os.environ.get('NOTION_ACCESS_TOKEN')
                # self.notion_access_token = None
                # self.notion_database_id = None
                self.notion_database_id = os.environ.get('NOTION_DATABASE_ID')

                if self.notion_access_token is None and self.notion_database_id is None:
                    raise ValueError ("Notion access token and database ID is not given")
            except:
                raise ValueError ("Notion access token and database ID is invalid")
        
            self.headers = {
                "Authorization": "Bearer " + self.notion_access_token,
                "Content-Type": "application/json",
                "Notion-Version": "2022-06-28"
            }
        except:
            print("Notion access token or database id not found.")
