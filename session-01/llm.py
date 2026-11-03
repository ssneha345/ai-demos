from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user",
            "content":"hello, who was the prime minister of india in 2000?"
        }
    ]
)

print(response.choices[0].message.content)
print(len(response.choices) )


