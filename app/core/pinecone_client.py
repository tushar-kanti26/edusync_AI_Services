from pinecone import Pinecone
import os

api_key = os.environ.get("PINECONE_API_KEY")

pc = Pinecone(api_key=api_key)

INDEX_NAME = "edusync"
index = pc.Index(INDEX_NAME)
