from litellm import completion
from pydantic import BaseModel


class Identifier(BaseModel):
  is_news: bool
  is_weather: bool

question = input("enter the question: ")

response = completion(
    model="ollama/llama3.2:1b",
    messages=[
        {"role": "system", "content": (
            "You are an expert classifier. Given a user's question, respond ONLY with a JSON object in this format:\n"
            "{\n"
            '  "is_news": true/false,\n'
            '  "is_weather": true/false\n'
            "}\n"
            "Guidelines:\n"
            "- Set is_news to true if the question is about current events, news, or recent happenings (for example: 'what happen to nvidia yesterday').\n"
            "- Set is_weather to true if the question is about weather, temperature, climate, or weather conditions.\n"
            "- Do not include any explanation, commentary, or extra text. Only output the JSON object."
        )},
        {"role": "user", "content": question}
    ],
    api_base="http://localhost:11434",
    temperature=0.1,
    max_tokens=100
)
print(response.choices[0].message.content)
