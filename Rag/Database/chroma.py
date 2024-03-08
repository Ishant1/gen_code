from langchain_community.vectorstores import Chroma


def get_database(embedding_model, persistent_dir, documents=None):
    db = Chroma(
        embedding_function=embedding_model,
        persist_directory=persistent_dir
    )

    if documents:
        db = db.from_documents(documents)

    return db


def get_db_as_retriever(db, search_type:str="mmr", **kwargs):
    search_kwargs = kwargs

    return db.as_retriever(
        search_type=search_type,
        search_kwargs=search_kwargs,
    )
