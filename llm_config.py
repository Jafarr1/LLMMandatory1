from crewai import LLM

# Reasoning / architecture endpoint
architect_llm = LLM(
    model="ollama/llama3.2",
    base_url="http://127.0.0.1:11434"
)

# Coding endpoint
coder_llm = LLM(
    model="ollama/qwen2.5-coder:3b",
    base_url="http://127.0.0.1:11435"
)