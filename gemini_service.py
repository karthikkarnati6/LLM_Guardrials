from urllib import response
from google import genai
from google.genai import types
from config import(
    GEMINI_API_KEY,
    GEMINI_MODEL
)




client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(prompt: str) -> str:
    
    
    """
    Generate a response from the Gemini API using the provided prompt and model.

    Args:
        prompt (str): The input prompt to send to the Gemini API.
        model (str): The model to use for generating the response. Defaults to GEMINI_MODEL.

    Returns:
        str: The generated response from the Gemini API.
    """
    #response = client.models.generate_content(
       # model=GEMINI_MODEL,
        #contents=prompt,)
    #return response.text or ""
    
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                )
            ]
        )
    )

    return response.text or ""
#print(generate_response("what is LLM Guardrails in 2 lines"))