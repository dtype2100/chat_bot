from fastapi import APIRouter
from models.request_model import QueryRequest
from services.llm_service import run_llama_inference
from services.chatbot_service import ChatbotService
import os 

router = APIRouter()
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
model_path = os.path.join(ROOT_DIR, 'ai_models', 'llama-3.2-Korean-Bllossom-3B-gguf-Q4_K_M', 'llama-3.2-Korean-Bllossom-3B-gguf-Q4_K_M.gguf')


@router.post("/generate")# generate
def generate_text(request: QueryRequest):
    """프롬프트 받아서 응답 생성"""
    output = run_llama_inference(request.prompt)
    return {"response": output}


@router.post("/chat")# generate
async def generate_text(request: QueryRequest):
    """프롬프트 받아서 응답 생성"""
    chatbot = ChatbotService(model_path)
    output = chatbot.chat(request.prompt)

    return {"response": output}
