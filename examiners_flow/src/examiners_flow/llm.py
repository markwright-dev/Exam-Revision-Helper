from crewai import LLM
from dotenv import load_dotenv
import os
load_dotenv()

class CrewAILLM():

    def client(self) -> LLM:
        try:
            return LLM(
                api_key=os.getenv("GEMINI_API_KEY"),
                model='gemini/gemini-1.5-flash',
            )
        except KeyError as e:
            raise EnvironmentError(f"LLM connection not possible")