import os
from dotenv import load_dotenv
from groq import Groq

# loading variables from .env file
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
system_prompt = open("system_prompt.txt", "r").read()


def gen_text(arguments: str) -> str:
    # The arguments are provided in JSON form
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": arguments,
            }
        ],
        model="mixtral-8x7b-32768",
        temperature=1,
        max_tokens=8192,
        top_p=1,
        stop=None,
        stream=False,
        response_format={"type": "json_object"},
    )

    result = chat_completion.choices[0].message.content
    if result is None: return ""
    else: return result


if __name__ == "__main__":
    prompt = """{
    "topic": "Can you fart underwater?",
    "additional-info": "You can up to 10 meters underwater. Consider the pressure underwater.",
    "mood": "funny",
    }"""

    print(gen_text(prompt))
