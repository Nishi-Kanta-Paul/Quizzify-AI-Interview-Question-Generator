import subprocess

def query_ollama(prompt, model="phi", timeout=300):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout
        )
        return result.stdout.decode()
    except Exception as e:
        return f"⚠️ Error running Ollama: {e}"
