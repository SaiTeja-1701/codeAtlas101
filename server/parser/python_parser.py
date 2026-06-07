import ast
import os


def parse_python_repository(repo_path):
    """
    Parse every Python file inside repository.

    Parameters:
    ----------
    repo_path : str
        Path to cloned repository

    Returns:
    -------
    list
        List containing parsed metadata
        for every Python file.
    """

    # stores parsed output
    parsed_files = []

    # recursively walk through folders
    # Example:
    #
    # repo/
    # ├── app/
    # │   ├── main.py
    # │   └── auth.py
    #
    # os.walk goes through everything
    #
    for root, _, files in os.walk(repo_path):

        for file in files:

            # only parse python files
            if file.endswith(".py"):

                # create full path
                file_path = os.path.join(
                    root,
                    file
                )

                print(
                    f"Parsing: {file_path}"
                )

                # parse single file
                parsed_result = (
                    parse_python_file(
                        file_path=file_path,
                        repo_path=repo_path
                    )
                )

                parsed_files.append(
                    parsed_result
                )

    return parsed_files


def parse_python_file(
    file_path,
    repo_path
):
    """
    Parse ONE python file using AST.

    Extract:
    ----------
    - functions
    - classes
    - imports
    - API routes

    Example output:
    ----------------
    {
        "file": "app/auth.py",
        "functions": ["login"],
        "classes": ["AuthService"],
        "imports": ["jwt"],
        "routes": [
            {
                "method": "POST",
                "path": "/login"
            }
        ]
    }
    """

    try:
        # read file contents
        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            code = file.read()

        # convert source code
        # into AST tree
        #
        # Instead of text:
        #
        # def login():
        #
        # Python converts to:
        #
        # FunctionDef node
        #
        tree = ast.parse(code)

        # store extracted info
        functions = []
        classes = []
        imports = []
        routes = []

        # walk through every AST node
        #
        # This lets us inspect:
        #
        # FunctionDef
        # ClassDef
        # Import
        # decorators
        #
        for node in ast.walk(tree):

            # --------------------------------
            # Detect functions
            # --------------------------------
            #
            # Example:
            #
            # def login():
            #
            if isinstance(
                node,
                ast.FunctionDef
            ):

                functions.append(
                    node.name
                )

            # --------------------------------
            # Detect classes
            # --------------------------------
            #
            # Example:
            #
            # class AuthService:
            #
            elif isinstance(
                node,
                ast.ClassDef
            ):

                classes.append(
                    node.name
                )

            # --------------------------------
            # Detect imports
            # --------------------------------
            #
            # Example:
            #
            # import jwt
            #
            elif isinstance(
                node,
                ast.Import
            ):

                for alias in node.names:

                    imports.append(
                        alias.name
                    )

            # --------------------------------
            # Detect imports
            #
            # Example:
            #
            # from db import session
            #
            elif isinstance(
                node,
                ast.ImportFrom
            ):

                if node.module:

                    imports.append(
                        node.module
                    )

            # --------------------------------
            # Detect decorators
            #
            # Example:
            #
            # @app.post("/login")
            #
            # Used in:
            # FastAPI
            # Flask
            #
            if hasattr(
                node,
                "decorator_list"
            ):

                for decorator in (
                    node.decorator_list
                ):

                    route = extract_route(
                        decorator
                    )

                    if route:

                        routes.append(
                            route
                        )

        # convert file path
        # into relative path
        #
        # Example:
        #
        # full:
        # temp_repos/fastapi/app/main.py
        #
        # relative:
        # app/main.py
        #
        relative_path = (
            os.path.relpath(
                file_path,
                repo_path
            )
        )

        # structured response
        return {
            "file":
                relative_path,

            "functions":
                functions,

            "classes":
                classes,

            "imports":
                imports,

            "routes":
                routes
        }

    except Exception as error:

        print(
            f"Failed parsing: {file_path}"
        )

        return {
            "file": file_path,
            "error": str(error)
        }


def extract_route(decorator):
    """
    Extract FastAPI / Flask route.

    Example:
    ----------
    @app.post("/login")

    Output:
    ----------
    {
        "method": "POST",
        "path": "/login"
    }
    """

    try:

        # decorator must be a function call
        #
        # Example:
        #
        # app.post("/login")
        #
        if (
            isinstance(
                decorator,
                ast.Call
            )
            and hasattr(
                decorator.func,
                "attr"
            )
        ):

            # route method
            #
            # post / get / delete
            #
            route_method = (
                decorator.func.attr
            )

            supported_routes = [
                "get",
                "post",
                "put",
                "delete",
                "patch",
                "route"
            ]

            # only support API routes
            if (
                route_method
                in supported_routes
            ):

                # first argument
                #
                # "/login"
                #
                if decorator.args:

                    route_path = (
                        decorator.args[0]
                        .value
                    )

                    return {
                        "method":
                            route_method.upper(),

                        "path":
                            route_path
                    }

    except Exception:
        pass

    return None