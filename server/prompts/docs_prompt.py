def build_document_prompt(
    doc_type,
    repo_analysis,
    retrieved_chunks,
    commits
):
    """
    Build document-specific prompt.
    """

    context = ""

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

    commit_context = ""

    for commit in commits[:10]:

        commit_context += (
            f"- "
            f"{commit['message']}\n"
        )

    prompts = {

        "readme": f"""
Generate a professional README.md.

Include:

# Project Overview
# Features
# Tech Stack
# Architecture
# Setup
# Usage
# Risks

Repository:
{repo_analysis}

Recent Development:
{commit_context}

Repository Context:
{context}
""",

        "architecture": f"""
Generate architecture.md.

IMPORTANT:

Mermaid diagrams MUST be
syntactically valid.

ONLY use:

graph TD

Example:

```mermaid
graph TD
Frontend[React Frontend]
--> Backend[Express API]

Backend
--> Database[(MongoDB)]

Repository:
{repo_analysis}

Repository Context:
{context}
""",

        "onboarding": f"""
Generate onboarding.md.

Explain:

- setup
- important files
- project flow
- recent development areas
- where to start

Recent Development:
{commit_context}

Repository Context:
{context}
""",

        "api_docs": f"""
Generate API_DOCUMENTATION.md.

Include:
- endpoint
- method
- purpose
- flow

Repository Context:
{context}
""",

        "risk_analysis": f"""
Generate RISK_ANALYSIS.md.

Analyze:

- architecture risks
- maintainability
- security concerns
- scaling limitations

Repository Context:
{context}
""",

        "srs": f"""
Generate a professional
Software Requirements
Specification.

Include:

1. Introduction
2. Purpose
3. Scope
4. System Overview
5. Functional Requirements
6. Non Functional Requirements
7. Architecture
8. Risks
9. Constraints
10. Future Scope

Recent Development:
{commit_context}

Repository Context:
{context}
"""
    }

    return prompts[
        doc_type
    ]