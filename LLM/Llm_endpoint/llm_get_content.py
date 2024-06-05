import sys
import os
import requests
import json
# Ensure the Notion directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from LLM.Config.llm_config import ConfigLLM
from PIL import Image



class RetrieveEndpoint(ConfigLLM):

    def __init__(self):
        super().__init__()
    

    def download_image(self, url):

        try:
            # Send a GET request to the URL
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            response.raise_for_status()
            
            # Specify the path where you want to save the image
            save_path = "image_downloads/" + 'image.png'  # Change this to your desired path

            # Write the image content to a file
            with open(save_path, 'wb') as f:
                f.write(response.content)
            
            print("Image downloaded successfully.")
            return save_path
            
        except requests.exceptions.RequestException as e:
            print("Failed to download image:", e)
        except IOError as e:
            print("Error saving the image:", e)
        
    
    def retrieve_content_from_image(self, url):

        try:
            image_path = self.download_image(url= url)
            image = Image.open(image_path)

            response = self.gemini_pro_vision_models.generate_content(['Give me detail about image in breif', image])
            return response.text

        except Exception as e:
            print("Error When generating breif introduction from image using gemini pro vision model: ", e)

    
    def retrieve_content(self, content_json:json):

        try:
            url = content_json['image_path']
            custom_prompt = content_json['prompt_description']

            image_content = self.retrieve_content_from_image(url = url)

            prompt = f"""I have an image of {image_content}. Need a captivating caption for my Facebook post. 
            Can you craft something engaging that resonates with my audience? Please include relevant hashtags. Thanks!

            ** IMPORTANT NOTE**
            Use this Custom prompt {custom_prompt} given by user to use in content creation
            Make Post Like a Human is Posting and make orgainc growth post.

            Additional Information (Optional):

            Target Audience: Briefly describe your target audience or demographics for this image post.
            Tone/Style: Specify the tone or style you want for the caption (e.g., heartfelt, witty, informative).
            Call to Action: Indicate if you want to include a specific call to action (e.g., Like & Share, Comment your thoughts)."""

            response = self.llm.invoke(prompt)

            return response.content
        
        except Exception as e:
            print("Error When generating content from image using gemini pro model: ", e)


# if __name__ == '__main__':
#     res = RetrieveEndpoint().retrieve_content('https://prod-files-secure.s3.us-west-2.amazonaws.com/724e051f-9b72-47e1-9ca8-1f6cd3befad2/78af8418-1767-43d3-8aaf-bab6ae5f5cd1/Eudaimonia_background_pic.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240531T110241Z&X-Amz-Expires=3600&X-Amz-Signature=a4f9fea28894908d02d682fc9a77ec5b6016d43300e71a4ab3d1c98517019027&X-Amz-SignedHeaders=host&x-id=GetObject')
#     print(res)
