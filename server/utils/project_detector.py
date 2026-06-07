import os

# folders that usually matter in software architecture
IMPORTANT_DIRS = {
    "controllers",
    "services",
    "models",
    "routes",
    "routers",
    "middleware",
    "db",
    "database",
    "api",
    "utils",
    "components",
    "pages",
}


def detect_project(repo_path):
    """
    Main function.

    Takes a repository path and tries to understand:
    - project type
    - framework
    - architecture
    - important directories
    """

    files = []
    folders = []

    # recursively walk through repository
    for root, dirs, filenames in os.walk(repo_path):

        # collect all file names
        for file in filenames:
            files.append(file)

        # collect all folder names
        for directory in dirs:
            folders.append(directory)

    # detect language/project type
    project_type = detect_language(files)

    # detect framework
    framework = detect_framework(files)

    # infer architecture style
    architecture = detect_architecture(folders)

    # keep only folders we care about
    important_dirs = [
        folder
        for folder in folders
        if folder.lower() in IMPORTANT_DIRS
    ]

    return {
        "project_type": project_type,
        "framework": framework,
        "architecture": architecture,
        "important_dirs": important_dirs
    }


def detect_language(files):
    """
    Detect project language using file extensions.

    Example:
    .py -> Python
    .jsx/.js -> MERN
    .tsx -> React TypeScript
    """

    if any(file.endswith(".py") for file in files):
        return "python"

    if any(file.endswith(".jsx") for file in files):
        return "mern"

    if any(file.endswith(".tsx") for file in files):
        return "react-typescript"

    return "unknown"


def detect_framework(files):
    """
    Detect framework using common files.

    Example:
    requirements.txt -> Python backend
    package.json -> Node/React
    manage.py -> Django
    """

    file_set = set(files)

    # Django
    if "manage.py" in file_set:
        return "django"

    # Python project
    if "requirements.txt" in file_set:
        return "python"

    # Node project
    if "package.json" in file_set:
        return "node"

    return "unknown"


def detect_architecture(folders):
    """
    Infer architecture style using folder names.

    Example:
    controllers + models + views
    -> MVC

    services + repositories
    -> service-oriented
    """

    folder_set = set(
        folder.lower()
        for folder in folders
    )

    mvc_dirs = {
        "controllers",
        "models",
        "views"
    }

    service_dirs = {
        "services",
        "repositories",
        "controllers"
    }

    # MVC detection
    if mvc_dirs.intersection(folder_set):
        return "mvc"

    # service-oriented detection
    if service_dirs.intersection(folder_set):
        return "service-oriented"

    # default
    return "layered"