import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI


class ConfigLLM(object):

    def __init__(self):

        try:
            self.gemini_api_key = os.environ.get('GEMINI_API_KEY')

            if self.gemini_api_key is None:
                raise ValueError ("Gemini API key is not given")
        except :
            raise ValueError("Gemini API key is not valid")
        
        # Configure the gemini pro Vision models
        try:
            genai.configure(api_key = self.gemini_api_key)

            self.gemini_pro_vision_models = genai.GenerativeModel('models/gemini-pro-vision')
        except Exception as e:
            print(f'When trying to configure the gemini pro vision model error found: {e}')

        # Configure the gemini pro model Content Creation
        try:
            
            self.llm = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=self.gemini_api_key)
        
        except Exception as e:
            print(f'When trying to configure the gemini pro model error found: {e}')
