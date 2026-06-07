# repo cloning
from utils.repo_loader import (
    clone_repository
)

# project detection
from utils.project_detector import (
    detect_project
)

# parsers
from parser.python_parser import (
    parse_python_repository
)

from parser.mern_parser import (
    parse_mern_repository
)

# chunking
from rag.chunker import (
    create_chunks
)

#vector_mem
from utils.vector_memory import (
    vector_store
)

def parse_repository(
    repo_path,
    project_type
):
    """
    Parse repository
    depending on stack.

    Python repo
    -> python parser

    MERN repo
    -> mern parser
    """

    if project_type == "python":

        print(
            "\nParsing Python repository..."
        )

        return (
            parse_python_repository(
                repo_path
            )
        )

    elif project_type == "mern":

        print(
            "\nParsing MERN repository..."
        )

        return (
            parse_mern_repository(
                repo_path
            )
        )

    return []


def analyze_repository(
    repo_url
):
    """
    Full repository analysis pipeline.

    Flow:
    ----------
    clone repo
        ↓
    detect project
        ↓
    parse code
        ↓
    create chunks
        ↓
    return structured data
    """

    # --------------------
    # Clone repository
    # --------------------
    clone_result = (
        clone_repository(
            repo_url
        )
    )

    repo_path = (
        clone_result[
            "repo_path"
        ]
    )

    # --------------------
    # Detect project
    # --------------------
    project_info = (
        detect_project(
            repo_path
        )
    )

    print(
        "\n========== PROJECT DETECTED =========="
    )

    print(project_info)

    print(
        "======================================"
    )

    # --------------------
    # Parse repository
    # --------------------
    parsed_files = (
        parse_repository(
            repo_path=repo_path,
            project_type=project_info[
                "project_type"
            ]
        )
    )

    print(
        "\n========== PARSING DONE =========="
    )

    print(
        f"Parsed files: {len(parsed_files)}"
    )

    print(
        "=================================="
    )

    # --------------------
    # Create chunks
    # --------------------
    chunks = (
        create_chunks(
            parsed_files=
                parsed_files,

            project_type=
                project_info[
                    "project_type"
                ]
        )
    )

    print(
        f"\nChunks created: {len(chunks)}"
    )

    vector_store.build_index(
        chunks
    )

    print(
        f"\nVector memory created"
    )

    return {
        "repo_name":
            clone_result[
                "repo_name"
            ],

        "repo_path":
            repo_path,

        "analysis":
            project_info,

        "parsed_files":
            parsed_files,

        "chunks":
            chunks
    }
