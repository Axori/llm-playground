"""
Main module for LLM Playground
"""

import os
from dotenv import load_dotenv


def main() -> None:
    """Main entry point for the application."""
    load_dotenv()

    print("Welcome to LLM Playground!")
    print(os.getenv("LLM_URL"))
    # Your application logic here


if __name__ == "__main__":
    main()
