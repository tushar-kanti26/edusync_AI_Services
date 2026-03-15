from langchain_community.chat_message_histories import RedisChatMessageHistory
import os
import redis

REDIS_URL = os.getenv("REDIS_URL")

def get_session_history(session_id: str):
    return RedisChatMessageHistory(
        session_id=session_id,
        url=REDIS_URL
    )
