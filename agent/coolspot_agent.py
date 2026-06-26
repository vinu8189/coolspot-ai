import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=os.getenv("MODEL", "gemini-2.5-flash"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def run_agent(query: str):

    prompt = f"""
You are CoolSpot AI, a smart local assistant.

User request:
{query}

TASK:
- Identify the city (e.g., Amsterdam, Utrecht, Rotterdam)
- Understand if user has kids or heat concern
- Suggest 5 REAL indoor places in that city

RULES:
- Only suggest real well-known places
- Prefer: museums, libraries, malls, indoor attractions, cinemas
- Make it kid-friendly if mentioned
- Do NOT invent fake names
- Keep response short and useful

FORMAT:
- Place 1
- Place 2
- Place 3
- Place 4
- Place 5
"""

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Something went wrong: {str(e)}"