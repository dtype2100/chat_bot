from fastapi import APIRouter
from models.request_model import QueryRequest
from services.llm_service import run_llama_inference

router = APIRouter()

@router.post("/generate")# generate
def generate_text(request: QueryRequest):
    """프롬프트 받아서 응답 생성"""
    output = run_llama_inference(request.prompt)
    return {"response": output}
