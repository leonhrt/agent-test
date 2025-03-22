from fastapi import APIRouter, Form
from llama_index.llms.gemini import Gemini

from core.config import settings

router = APIRouter()

@router.post("/ask")
async def endpoint(text: str = Form(...)):
    llm = Gemini(
        model="models/" + settings.LLM_MODEL,
        api_key=settings.GEMINI_API_KEY
    )

    return llm.complete(text)


