import json
import os
from dotenv import load_dotenv
from groq import Groq, RateLimitError

load_dotenv()

class LLMClient:
    def __init__(self,model_name=None):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is missing. Set it in your .env file."
            )
    
        self.client=Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.model=model_name or os.getenv(
            "MODEL_NAME_A",
            "openai/gpt-oss-120b"
        )

    def generate(self,messages:list,tools:list|None=None):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=tools
        )
        return response.choices[0].message