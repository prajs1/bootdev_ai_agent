import os
import sys

from dotenv import load_dotenv
from google import genai

if len(sys.argv) > 1:
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    prompt = sys.argv[1]

    client = genai.Client(api_key=api_key)

    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    print(response.text)
    if "--verbose" in sys.argv:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    print("ERROR: No prompt provided!!")
    sys.exit(1)
