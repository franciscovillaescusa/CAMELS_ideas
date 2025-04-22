from langchain_core.runnables import RunnableConfig
import sys,os
from pathlib import Path

from src.parameters import GraphState


def preprocess_node(state: GraphState, config: RunnableConfig):
    """
    This agent reads the input files, clean up files, and set the name of some files
    """

    state['files'] = {}
    state['files']['CAMELS'] = 'src/CAMELS.md'

    path = Path(state['files']['CAMELS'])
    with path.open("r", encoding="utf-8") as f:
        state['CAMELS'] = f.read()
        
    return state

