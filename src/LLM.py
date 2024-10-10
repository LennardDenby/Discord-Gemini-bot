from secret import GEMINI_API_KEY
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import prompts as prompts

class LLM:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=prompts.default
        )
    
    def promptLLM(self, prompt: str, author: str) -> str:
        response = self.model.generate_content(
            f"{author}, {prompt}",
            safety_settings={
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            }
        )
        return response.text