import json
import openai

open_ai_api_key = json.load(open(".open_ai_api.json"))["key"]
print(open_ai_api_key)
openai.api_key = open_ai_api_key

response = openai.Completion.create(
    engine="davinci",
    prompt="This is a test",
    temperature=0.3,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
)

print(response)
print(response.choices[0].text)