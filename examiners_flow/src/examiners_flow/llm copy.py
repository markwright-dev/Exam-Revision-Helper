from crewai import LLM
from dotenv import load_dotenv
import os
load_dotenv()

class CrewAILLM():

    def client(self) -> LLM:
        try:
            model="gpt-4o"
            test=os.getenv("AZURE_OPENAI_API_KEY")
            return LLM(
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
                base_url=os.getenv("AZURE_OPENAI_API_ENDPOINT"),
                model=f"azure/{model}"
            )
        except KeyError as e:
            raise EnvironmentError(f"LLM connection not possible")