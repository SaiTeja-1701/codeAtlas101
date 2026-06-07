import os
import re


def parse_mern_repository(repo_path):
    """
    Parse MERN repository.

    Extract:
    ----------
    - Express routes
    - React components
    - API calls
    - Mongo models

    Returns:
    ----------
    Parsed metadata for files
    """

    parsed_files = []

    # walk through repo
    for root, _, files in os.walk(repo_path):

        for file in files:

            # only JS ecosystem files
            if file.endswith(
                (
                    ".js",
                    ".jsx",
                    ".ts",
                    ".tsx"
                )
            ):

                file_path = (
                    os.path.join(
                        root,
                        file
                    )
                )

                print(
                    f"Parsing MERN file: {file_path}"
                )

                parsed = (
                    parse_mern_file(
                        file_path,
                        repo_path
                    )
                )

                parsed_files.append(
                    parsed
                )

    return parsed_files


def parse_mern_file(
    file_path,
    repo_path
):
    """
    Parse single MERN file
    using regex heuristics.

    We avoid AST for MVP
    because speed > perfection.
    """

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            code = file.read()

        # -------------------
        # Detect React Components
        # -------------------
        #
        # function Dashboard()
        #
        components = re.findall(
            r"function\s+([A-Z]\w+)",
            code
        )

        # -------------------
        # Detect Express Routes
        # -------------------
        #
        # router.post("/login")
        #
        routes = re.findall(
            r'router\.(get|post|put|delete|patch)\(["\'](.*?)["\']',
            code
        )

        route_data = [
            {
                "method":
                    method.upper(),

                "path":
                    path
            }
            for method, path
            in routes
        ]

        # -------------------
        # Detect API calls
        # -------------------
        #
        # axios.get("/api")
        # fetch("/api")
        #
        api_calls = re.findall(
            r'(?:axios|fetch).*?["\'](.*?)["\']',
            code
        )

        # -------------------
        # Detect Mongo Models
        # -------------------
        #
        # mongoose.model("User")
        #
        mongo_models = re.findall(
            r'mongoose\.model\(["\'](.*?)["\']',
            code
        )

        # relative path
        relative_path = (
            os.path.relpath(
                file_path,
                repo_path
            )
        )

        return {
            "file":
                relative_path,

            "components":
                components,

            "routes":
                route_data,

            "api_calls":
                api_calls,

            "mongo_models":
                mongo_models
        }

    except Exception as error:

        return {
            "file":
                file_path,

            "error":
                str(error)
        }