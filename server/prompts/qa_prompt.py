def build_qa_prompt(
    question,
    retrieved_chunks
):
    """
    Build prompt for
    repository Q&A.

    We force model
    to stay grounded
    in retrieved code.

    This reduces hallucinations.
    """

    context = ""

    # build context block
    for chunk in retrieved_chunks:

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
You are a senior software architect.

You are analyzing a repository.

ONLY use the provided repository context.

If uncertain, say uncertain.

Question:
{question}

Repository Context:
{context}

Provide answer in this format:

## Summary

## Key Files

## Flow

## Dependencies

## Risks
"""

    return prompt