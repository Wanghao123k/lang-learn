from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 单条文本向量化
query_vector = embeddings.embed_query("hello world")
print(f"向量维度: {len(query_vector)}")
print(f"前5个值: {query_vector[:5]}")

# 批量文本向量化
doc_vectors = embeddings.embed_documents(["hello world", "I love programming"])
print(f"文档数量: {len(doc_vectors)}")
