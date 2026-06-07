import os

from dotenv import load_dotenv
from openai import OpenAI

from utils.vector_memory import (
    vector_store
)

from prompts.qa_prompt import (
    build_qa_prompt
)

# load environment variables
load_dotenv()

# initialize Groq client
client = OpenAI(
    api_key=os.getenv(
        "GROQ_API_KEY"
    ),
    base_url=(
        "https://api.groq.com/openai/v1"
    )
)


def ask_repository(
    question
):
    """
    Repository Q&A pipeline.

    Flow:
    ----------
    question
        ↓
    semantic retrieval
        ↓
    prompt creation
        ↓
    LLM reasoning
        ↓
    answer
    """

    # -------------------
    # retrieve chunks
    # -------------------
    retrieved_chunks = (
        vector_store.search(
            query=question,
            top_k=5
        )
    )

    # -------------------
    # build prompt
    # -------------------
    prompt = (
        build_qa_prompt(
            question,
            retrieved_chunks
        )
    )

    print(
        "\nSending prompt to Groq..."
    )

    # -------------------
    # call model
    # -------------------
    response = (
        client.chat.completions.create(
            model=(
                "llama-3.3-70b-versatile"
            ),
            messages=[
                {
                    "role":
                        "system",
                    "content":
                        (
                            "You are a "
                            "senior software "
                            "architect."
                        )
                },
                {
                    "role":
                        "user",
                    "content":
                        prompt
                }
            ]
        )
    )

    answer = (
        response
        .choices[0]
        .message.content
    )

    return {
        "answer":
            answer,

        "retrieved_chunks":
            retrieved_chunks
    }