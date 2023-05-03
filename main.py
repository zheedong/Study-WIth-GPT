import json
import openai
import fitz
from time import time

openai.api_key = json.load(open(".openai_api_key.json"))["key"]

PDF_FILE_PATH = "./data/sample4.pdf"
doc = fitz.open(PDF_FILE_PATH)
for page in doc:
    text = page.get_text()
    print(text)

f = open(f"summary/test_{time()}.md", "w")

for page in doc:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Summarise following text in markdown format:\n" + page.get_text(), # TODO : max tokens?
        temperature=0.3,
        max_tokens=2049,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    f.write(response.choices[0].text)

f.close()