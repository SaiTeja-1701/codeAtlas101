import os
import shutil
from pathlib import Path
from git import Repo


TEMP_REPO_DIR = "temp_repos"


def extract_repo_name(repo_url: str):
    """
    Example:
    https://github.com/fastapi/fastapi
    -> fastapi
    """
    return repo_url.rstrip("/").split("/")[-1]


def clone_repository(repo_url: str):
    repo_name = extract_repo_name(repo_url)

    repo_path = os.path.join(
        TEMP_REPO_DIR,
        repo_name
    )

    # remove old repo if exists
    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    print("\nCloning repository...")
    print(repo_url)

    Repo.clone_from(
        repo_url,
        repo_path
    )

    print("Repository cloned.")
    print(f"Saved to: {repo_path}")

    return {
        "repo_name": repo_name,
        "repo_path": repo_path
    }