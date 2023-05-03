# create.py

import json
import os
from pathlib import Path

import openai

PROMPT = "anime style girl who holds C programming book"
DATA_DIR = Path.cwd() / "responses"

DATA_DIR.mkdir(exist_ok=True)

openai.api_key = json.load(open(".openai_api_key.json"))["key"]

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json",
)

file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"

with open(file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)