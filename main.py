import json
import openai
import fitz
from time import time

openai.api_key = json.load(open(".openai_api_key.json"))["key"]

PDF_FILE_PATH = "./data/sample1.pdf"
doc = fitz.open(PDF_FILE_PATH)
for page in doc:
    text = page.get_text()
    print(text)

f = open(f"summary/test_{time()}.md", "w")

for page in doc:
    response = openai.Completion.create(
        engine="davinci",
        prompt="Summarise following text and give some additional examples and translate it into Korean in markdown format:\n" + page.get_text(),
        temperature=0.3,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    f.write(response.choices[0].text)

f.close()