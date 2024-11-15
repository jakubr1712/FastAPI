import re
from typing import List, Literal

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    from_: Literal["user", "bot"]
    message: str


class ChatMessage(BaseModel):
    history: List[Message]
    new_message: str


class ChatResponse(BaseModel):
    updated_history: List[Message]


def replace_duplicated_words(message: str) -> str:
    words = re.findall(r'\b\w+\b|[^\w\s]', message)
    seen_words = set()
    result = []

    for word in words:
        normalized_word = re.sub(r'[^\w]', '', word).lower()
        if normalized_word in seen_words and normalized_word != '':
            result.append("fake")
        else:
            result.append(word)
            if normalized_word:
                seen_words.add(normalized_word)

    final_result = ""
    for i, word in enumerate(result):
        if i > 0 and re.match(r'\w', word):
            final_result += " "
        final_result += word

    return final_result


@app.post("/api/chat", response_model=ChatResponse, status_code=status.HTTP_201_CREATED)
async def chat_endpoint(chat_message: ChatMessage):
    bot_response = replace_duplicated_words(chat_message.new_message)

    user_message = Message(from_="user", message=chat_message.new_message)
    bot_message = Message(from_="bot", message=bot_response)

    updated_history = chat_message.history + [user_message, bot_message]

    return ChatResponse(updated_history=updated_history)
