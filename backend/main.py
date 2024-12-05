import re
from typing import List, Literal

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    final_result = ""

    for i, word in enumerate(words):
        normalized_word = re.sub(r'[^\w]', '', word).lower()
        if normalized_word in seen_words and normalized_word != '':
            word = "fake"
        else:
            if normalized_word:
                seen_words.add(normalized_word)

        if i > 0 and re.match(r'\w', word):
            final_result += " "
        final_result += word

    return final_result


@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(chat_message: ChatMessage):
    bot_response = replace_duplicated_words(chat_message.new_message)

    user_message = Message(from_="user", message=chat_message.new_message)
    bot_message = Message(from_="bot", message=bot_response)

    updated_history = chat_message.history + [user_message, bot_message]

    return ChatResponse(updated_history=updated_history)


class SortRequest(BaseModel):
    array: List[int]


class SortResponse(BaseModel):
    sorted_array: List[int]


def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


@app.post("/api/sort", response_model=SortResponse)
async def sort_endpoint(sort_request: SortRequest):
    sorted_array = quicksort(sort_request.array)
    return SortResponse(sorted_array=sorted_array)
