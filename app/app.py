import openai
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import config

from pydantic import BaseModel

app = FastAPI()

origins = [
    config.CLIENT_ORIGIN
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = config.OPENAI_API_SECRET_KEY


class Message(BaseModel):
    content: str


@app.post("/chats/{chat_id}/message")
def post_message(chat_id: int, message: Message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.content}
        ]
    )

    return {"response": completion['choices'][0]['message']['content']}
