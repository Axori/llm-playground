"""
Main module for LLM Playground
"""

import asyncio
from langchain_core.messages import HumanMessage
from llm.connector import create_training_agent


def main() -> None:
    """Main entry point for the application."""
    training_agent = create_training_agent()
    result = training_agent.ainvoke(
        {
            "messages": [
                HumanMessage(
                    "Create a 3-day calisthenics workout plan for an intermediate athlete who wants to improve core strength and learn basic gymnastics skills."
                )
            ]
        }
    )

    import pprint

    pprint.pprint(asyncio.run(result).get("messages", [])[-1].content)


if __name__ == "__main__":
    main()
