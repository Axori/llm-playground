import os
from prompts.tranings import TRAINING_SYSTEM_PROMPT
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()


def create_training_agent():
    llm_url = os.getenv("LLM_URL")
    llm_model = os.getenv("LLM_MODEL")

    assert llm_url, "LLM_URL is not set"
    assert llm_model, "LLM_MODEL is not set"

    model = ChatOpenAI(
        base_url=llm_url,
        model=llm_model,
        api_key="",
    )

    agent = create_agent(
        model,
        system_prompt=TRAINING_SYSTEM_PROMPT,
    )
    return agent
