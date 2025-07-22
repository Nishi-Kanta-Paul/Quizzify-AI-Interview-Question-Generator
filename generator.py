from ollama_interface import query_ollama
from utils import load_prompt_template

def generate_questions(job_role, num_questions=5, mode="Beginner"):
    prompt_template = load_prompt_template("prompts/base_prompt.txt")
    full_prompt = prompt_template.replace("<job role>", job_role)\
                                 .replace("<num>", str(num_questions))\
                                 .replace("<Beginner/Advanced>", mode)
    return query_ollama(full_prompt)
