from Notion.GetPageDetail.get_image_n_prompt import GetPage
from LLM.Llm_endpoint.llm_get_content import RetrieveEndpoint
from Facebook.Post.creat_post import CreatePost
from Facebook.Update.update_facebook_detail import UpdateFacebook
from Notion.UpdatePageDetail.update_detail import UpdateDetail

try:
    get_image_n_prompt_response = GetPage().get_page()
    retrieve_content = RetrieveEndpoint().retrieve_content(get_image_n_prompt_response)
    post_id = CreatePost().post_image_and_message(message=retrieve_content)

    view_count = UpdateFacebook().view_count(post_id)
    like_count = UpdateFacebook().like_count(post_id)



    UpdateDetail().update_content_generation(post_id=post_id, view_on_post=view_count, like_on_post=like_count, new_content=retrieve_content, page_id=get_image_n_prompt_response['page_id'])

except Exception as e:
    print(e)