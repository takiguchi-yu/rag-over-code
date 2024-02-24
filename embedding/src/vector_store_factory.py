from interfaces import IVectorStore
from vector_stores import ChromaVectorStore, FaissVectorStore


class VectorStoreFactory:
    _stores = {
        "chroma": ChromaVectorStore,
        "faiss": FaissVectorStore,
    }

    @staticmethod
    def get_vector_store(store_type: str) -> IVectorStore:
        """指定されたベクトルストアのインスタンスを返却します。

        :param store_type: "chroma" or "faiss"
        """
        if store_type not in VectorStoreFactory._stores:
            raise ValueError(f"Vector store '{store_type}' is not supported.")
        return VectorStoreFactory._stores[store_type]()
