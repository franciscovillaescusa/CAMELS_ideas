from langchain_core.runnables import RunnableConfig
import sys,os,re,base64
from pathlib import Path
from tqdm import tqdm
import asyncio
from functools import partial
import random

from src.parameters import GraphState
from src.prompts import *
from src.llm import llm
from src.tools import json_parser



def idea_agent(state: GraphState, config: RunnableConfig):
    """
    This agent generates an idea given the CAMELS context
    """

    for i in range(10):
    
        PROMPT = idea_prompt(state)
        result = llm.invoke(PROMPT).content
    
        # Get the abstract
        parsed_json = json_parser(result)
        title       = parsed_json["title"]
        description = parsed_json["description"]

        print(f'{i:02d}: {title}')

    
