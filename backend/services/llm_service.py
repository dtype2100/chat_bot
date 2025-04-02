# from llama_cpp import Llama

# # 모델 경로 설정 (GGUF 파일)
# MODEL_PATH = "./models/phi-2.Q4_K_M.gguf"


# from llama_cpp import Llama

# llm = Llama.from_pretrained(
# 	repo_id="TheBloke/phi-2-GGUF",
# 	filename="phi-2.Q2_K.gguf",
# )

from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="TheBloke/Llama-2-7B-GGUF",
	filename="llama-2-7b.Q2_K.gguf",
)


# output = llm(
# 	"Once upon a time,",
# 	max_tokens=512,
# 	echo=True,
# )

# llama-cpp-python 초기화
# llm = Llama(
#     model_path=MODEL_PATH,
#     n_ctx=2048,
#     n_threads=8,  # 시스템에 맞게 조정
#     verbose=False
# )

def run_llama_inference(prompt: str) -> str:
    """LLM에게 프롬프트를 주고 응답을 받는 함수"""
    response = llm(prompt, max_tokens=200)
    return response["choices"][0]["text"].strip()
