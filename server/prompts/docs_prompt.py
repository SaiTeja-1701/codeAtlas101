def build_docs_prompt(
    repo_analysis,
    retrieved_chunks
):
    """
    Build documentation prompt.

    Goal:
    ----------
    Generate professional
    markdown docs
    grounded in repository
    context.
    """

    context = ""

    # build repo context
    for chunk in (
        retrieved_chunks
    ):

        context += (
            f"\nFile: "
            f"{chunk['file']}\n"
        )

        context += (
            f"Type: "
            f"{chunk['type']}\n"
        )

        context += (
            f"Content: "
            f"{chunk['content']}\n"
        )

    prompt = f"""
You are a senior technical documentation engineer.

Generate professional repository documentation.

Repository Analysis:
{repo_analysis}

Repository Context:
{context}

Generate:

1. README.md
2. architecture.md
3. onboarding.md

Use markdown.

Include:

- project overview
- architecture
- important modules
- execution flow
- setup instructions
- risks

Also include Mermaid diagrams.

Be concise but useful.

Return in this format:

===README===
markdown here

===ARCHITECTURE===
markdown here

===ONBOARDING===
markdown here
"""

    return prompt