import json
import requests
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class WebSearchTool(BaseTool):
    name: str="""Access the internet"""
    description: str="This tool allows you too find websites with relevant information only when a website URL is passed as a string"
    def _run(self, website: str) -> str:
        response = requests.get(website)

        return json.dumps(response.text)