def create_chunks(
    parsed_files,
    project_type
):
    """
    Convert parsed repository data
    into intelligent chunks.

    Why?
    ----------
    We do NOT want to embed
    entire files.

    Instead:

    function -> chunk
    route -> chunk
    component -> chunk

    This improves retrieval quality.
    """

    chunks = []

    # -------------------------
    # Python repositories
    # -------------------------
    if project_type == "python":

        for file_data in parsed_files:

            file_path = file_data.get(
                "file",
                "unknown"
            )

            # ---------------------
            # Functions
            # ---------------------
            for function in (
                file_data.get(
                    "functions",
                    []
                )
            ):

                chunk = {
                    "content":
                        f"Python function {function}",

                    "file":
                        file_path,

                    "type":
                        "function",

                    "language":
                        "python"
                }

                chunks.append(
                    chunk
                )

            # ---------------------
            # Classes
            # ---------------------
            for class_name in (
                file_data.get(
                    "classes",
                    []
                )
            ):

                chunk = {
                    "content":
                        f"Python class {class_name}",

                    "file":
                        file_path,

                    "type":
                        "class",

                    "language":
                        "python"
                }

                chunks.append(
                    chunk
                )

            # ---------------------
            # Routes
            # ---------------------
            for route in (
                file_data.get(
                    "routes",
                    []
                )
            ):

                chunk = {
                    "content":
                        (
                            f"API route "
                            f"{route['method']} "
                            f"{route['path']}"
                        ),

                    "file":
                        file_path,

                    "type":
                        "route",

                    "language":
                        "python"
                }

                chunks.append(
                    chunk
                )

    # -------------------------
    # MERN repositories
    # -------------------------
    elif project_type == "mern":

        for file_data in parsed_files:

            file_path = file_data.get(
                "file",
                "unknown"
            )

            # ---------------------
            # React components
            # ---------------------
            for component in (
                file_data.get(
                    "components",
                    []
                )
            ):

                chunk = {
                    "content":
                        (
                            f"React component "
                            f"{component}"
                        ),

                    "file":
                        file_path,

                    "type":
                        "component",

                    "language":
                        "javascript"
                }

                chunks.append(
                    chunk
                )

            # ---------------------
            # API Routes
            # ---------------------
            for route in (
                file_data.get(
                    "routes",
                    []
                )
            ):

                chunk = {
                    "content":
                        (
                            f"Express route "
                            f"{route['method']} "
                            f"{route['path']}"
                        ),

                    "file":
                        file_path,

                    "type":
                        "route",

                    "language":
                        "javascript"
                }

                chunks.append(
                    chunk
                )

            # ---------------------
            # Mongo models
            # ---------------------
            for model in (
                file_data.get(
                    "mongo_models",
                    []
                )
            ):

                chunk = {
                    "content":
                        (
                            f"Mongo model "
                            f"{model}"
                        ),

                    "file":
                        file_path,

                    "type":
                        "database_model",

                    "language":
                        "javascript"
                }

                chunks.append(
                    chunk
                )

            # ---------------------
            # API Calls
            # ---------------------
            for api in (
                file_data.get(
                    "api_calls",
                    []
                )
            ):

                chunk = {
                    "content":
                        (
                            f"API call "
                            f"{api}"
                        ),

                    "file":
                        file_path,

                    "type":
                        "api_call",

                    "language":
                        "javascript"
                }

                chunks.append(
                    chunk
                )

    return chunks