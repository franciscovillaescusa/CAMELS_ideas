from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage, AIMessage


def idea_prompt(state):

    prompt = f"""Your task is to generate an idea for a breakthrough project involving data from the CAMELS simulations. Below you can find a detailed description about the CAMELS data.

CAMELS data description:
{state['CAMELS']}
    
Respond in **valid JSON format** as follows:

```json
{{
  "title": "Title of the idea",
  "description": "Brief explanation of the idea",
}}
```
"""

    return [HumanMessage(content=prompt)]
