from git import Repo


def get_recent_commits(
    repo_path,
    limit=20
):
    """
    Fetch recent commits.

    Used for:
    ----------
    smarter documentation
    onboarding context
    engineering insights
    """

    try:

        repo = Repo(
            repo_path
        )

        commits = []

        for commit in repo.iter_commits(
            max_count=limit
        ):

            commits.append({
                "message":
                    commit.message.strip(),

                "author":
                    str(
                        commit.author
                    ),

                "date":
                    str(
                        commit.committed_datetime
                    )
            })

        return commits

    except Exception as error:

        print(
            "Commit parsing failed:",
            error
        )

        return []