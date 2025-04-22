import requests
import sys,os,re,json
from langchain_core.messages import HumanMessage
#from src.prompts import fixer_prompt, LaTeX_prompt
from src.parameters import GraphState
from src.llm import llm
from pathlib import Path


def json_parser(text):
    """
    This function extracts the text between ```json ```
    """
    
    json_pattern = r"```json(.*)```"
    match = re.findall(json_pattern, text, re.DOTALL)
    json_string = match[0].strip()
    try:
        parsed_json = json.loads(json_string)
    except json.decoder.JSONDecodeError:
        try:
            json_string = json_string.replace("'", "\"")
            parsed_json = json.loads(json_string)
        except:
            raise Exception('Failed to extract json from text')
    return parsed_json


