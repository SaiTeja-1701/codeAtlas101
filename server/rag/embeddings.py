from sentence_transformers import (
    SentenceTransformer
)

# lightweight model
#
# fast
# good enough for MVP
#
MODEL_NAME = (
    "all-MiniLM-L6-v2"
)

# load once globally
embedding_model = (
    SentenceTransformer(
        MODEL_NAME
    )
)


def generate_embeddings(
    texts
):
    """
    Convert text into vectors.

    Example:
    ----------
    "login function"

    becomes:

    [0.12, 0.44, ...]
    """

    embeddings = (
        embedding_model.encode(
            texts,
            convert_to_numpy=True
        )
    )

    return embeddings