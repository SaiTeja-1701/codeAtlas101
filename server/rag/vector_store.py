import faiss
import numpy as np

from rag.embeddings import (
    generate_embeddings
)


class VectorStore:
    """
    Store repository chunks
    in FAISS.

    Later:
    question
        ↓
    semantic search
        ↓
    retrieve best chunks
    """

    def __init__(self):

        # store chunk metadata
        self.chunks = []

        # FAISS index
        self.index = None

    def build_index(
        self,
        chunks
    ):
        """
        Build vector index
        from chunks.
        """

        self.chunks = chunks

        # extract text
        texts = [
            chunk["content"]
            for chunk in chunks
        ]

        print(
            "\nGenerating embeddings..."
        )

        embeddings = (
            generate_embeddings(
                texts
            )
        )

        # embedding size
        dimension = (
            embeddings.shape[1]
        )

        # create FAISS index
        self.index = (
            faiss.IndexFlatL2(
                dimension
            )
        )

        # add vectors
        self.index.add(
            np.array(
                embeddings,
                dtype=np.float32
            )
        )

        print(
            f"Indexed {len(chunks)} chunks."
        )

    def search(
        self,
        query,
        top_k=5
    ):
        """
        Semantic search.

        Example:
        ----------
        query:
        "authentication"

        returns:
        top relevant chunks
        """

        if self.index is None:

            raise Exception(
                "Vector store empty."
            )

        # embed query
        query_embedding = (
            generate_embeddings(
                [query]
            )
        )

        # search nearest chunks
        distances, indices = (
            self.index.search(
                np.array(
                    query_embedding,
                    dtype=np.float32
                ),
                top_k
            )
        )

        results = []

        for idx in indices[0]:

            if idx < len(
                self.chunks
            ):

                results.append(
                    self.chunks[idx]
                )

        return results