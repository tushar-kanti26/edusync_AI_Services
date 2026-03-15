from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI

from app.routes.chatbot import router as chatbot_router
from app.routes.inforgraphs import router as infograph_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="EduSync AI API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.api_route("/", methods=["GET", "HEAD"])
def hello():
    return {"message": "Welcome to Edusync AI service!"}

app.include_router(chatbot_router, prefix="/chatbot", tags=["Chatbot"])
app.include_router(infograph_router, prefix="/infograph", tags=["Infograph"])