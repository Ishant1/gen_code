from Rag.Dataset.load_dataset import get_git_code, load_github_data_from_local, split_documents
from Rag.Database.chroma import get_database


data_path = get_git_code("https://github.com/langchain-ai/langchain", "langchain")
documents = load_github_data_from_local(f"{data_path}/libs/langchain/langchain")
splits = split_documents(documents)

chroma = get_database("")

