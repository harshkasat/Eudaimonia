import sys
import os
import requests
# Ensure the Notion directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Notion.GetPageDetail.get_image_n_prompt import GetPage
from Notion.UpdatePageDetail.update_detail import UpdateDetail
from LLM.Llm_endpoint.llm_get_content import RetrieveEndpoint

class CreateContent(GetPage):

    def __init__(self):
        super().__init__()
        self.url = f'https://api.notion.com/v1/databases/{self.notion_database_id}'


    def create_content(self):

        try:
            get_image_n_prompt_response = GetPage().get_page()

            retrieve_content = RetrieveEndpoint().retrieve_content(get_image_n_prompt_response)


            # This Part goona be last after post facebook content

            # update_content_in_notion = UpdateDetail().update_content_generation(new_content=retrieve_content,page_id= get_image_n_prompt_response['page_id'] )

            return retrieve_content
        
        except Exception as e:
            print(f'When trying to retrieve database information from notion database error found: {e}')


res = CreateContent().create_content()

print(res)