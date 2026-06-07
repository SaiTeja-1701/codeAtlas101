import os

from openai import OpenAI
from dotenv import load_dotenv

from prompts.docs_prompt import (
    build_docs_prompt
)

from utils.vector_memory import (
    vector_store
)

from utils.repository_memory import (
    repository_state
)

# load env
load_dotenv()

# Groq client
client = OpenAI(
    api_key=os.getenv(
        "GROQ_API_KEY"
    ),
    base_url=(
        "https://api.groq.com/openai/v1"
    )
)


def save_document(
    filename,
    content
):
    """
    Save markdown file.
    """

    output_path = (
        os.path.join(
            "generated_docs",
            filename
        )
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)

    print(
        f"Saved: {filename}"
    )


def generate_docs():
    """
    Generate repository docs.

    Flow:
    ----------
    get repo state
        ↓
    retrieve chunks
        ↓
    build prompt
        ↓
    LLM generates docs
        ↓
    save markdown files
    """

    # get repo metadata
    repo_analysis = (
        repository_state[
            "analysis"
        ]
    )

    # retrieve broad repo context
    retrieved_chunks = (
        vector_store.search(
            query="project architecture authentication api database routes components",
            top_k=15
        )
    )

    # build prompt
    prompt = (
        build_docs_prompt(
            repo_analysis,
            retrieved_chunks
        )
    )

    print(
        "\nGenerating docs..."
    )

    # call Groq
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
                            "technical "
                            "documentation "
                            "expert."
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

    generated_text = (
        response
        .choices[0]
        .message.content
    )

    # split generated docs
    readme = (
        generated_text
        .split(
            "===ARCHITECTURE==="
        )[0]
        .replace(
            "===README===",
            ""
        )
    )

    architecture = (
        generated_text
        .split(
            "===ARCHITECTURE==="
        )[1]
        .split(
            "===ONBOARDING==="
        )[0]
    )

    onboarding = (
        generated_text
        .split(
            "===ONBOARDING==="
        )[1]
    )

    # save markdown files
    save_document(
        "README.md",
        readme
    )

    save_document(
        "architecture.md",
        architecture
    )

    save_document(
        "onboarding.md",
        onboarding
    )

    return {
        "success": True,
        "message":
            "Documentation generated"
    }