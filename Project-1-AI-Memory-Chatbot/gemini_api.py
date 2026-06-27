from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("API_KEY")
)


def get_response(message, history=None):
    """
    Send user message to Gemini and return response.
    """

    if history is None:
        history = []

    prompt = ""

    # Add previous conversation memory
    for chat in history:
        prompt += f"{chat['role']}: {chat['content']}\n"

    prompt += f"user: {message}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text