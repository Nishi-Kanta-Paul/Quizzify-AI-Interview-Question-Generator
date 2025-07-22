def load_prompt_template(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def export_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
