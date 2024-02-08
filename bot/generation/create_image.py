import os

from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API"))


def generate(prompt: str):
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        n=1,
        size='1024x1024',
    )

    return response.data[0].url
