import dspy 
from dotenv import load_dotenv
import os

load_dotenv()

dspy.configure(
    lm = dspy.LM("openai/gpt-4o-mini", api_key = os.getenv("OPENAI_API_KEY")
))