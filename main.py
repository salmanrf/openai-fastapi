import openai
import os

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

print(os.environ["OPENAI_API_SECRET_KEY"])


class Message(BaseModel):
    content: str


@app.post("/chats/{chat_id}/message")
def post_message(chat_id: int, message: Message):
    return {"chat_id": chat_id, message: message}
