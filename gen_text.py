import os
from dotenv import load_dotenv
from groq import Groq

# loading variables from .env file
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
system_prompt = open("system_prompt.txt", "r").read()


def gen_text(arguments):
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
        model="llama3-8b-8192",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )
    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    prompt = """{
    "topic": "Can you fart underwater?",
    "additional-info": "You can up to 10 meters underwater. Consider the pressure underwater.",
    "mood": "funny",
    }"""

    print(gen_text(prompt))
