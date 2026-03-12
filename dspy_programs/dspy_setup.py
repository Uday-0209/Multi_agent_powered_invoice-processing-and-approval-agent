import os
import dspy 
from dotenv import load_dotenv

load_dotenv()

def configure_dspy():
    lm = dspy.LM("openai/gpt-4o-mini",
                 api_key = os.getenv("OPENAI_API_KEY"))
    dspy.configure(lm = lm)