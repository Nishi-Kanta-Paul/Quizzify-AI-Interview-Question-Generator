from flask import Flask, render_template, request, send_file
from generator import generate_questions
from utils import export_to_file
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    if request.method == 'POST':
        job_role = request.form.get('job_role', 'Software Engineer')
        num_questions = int(request.form.get('num_questions', 5))
        mode = request.form.get('mode', 'Beginner')
        save = request.form.get('save', None)
        
        output = generate_questions(job_role, num_questions, mode)

        if save:
            filename = f"{job_role.replace(' ', '_').lower()}_interview_questions.md"
            export_to_file(output, filename)
            return send_file(filename, as_attachment=True)

    return render_template("index.html", output=output)

if __name__ == '__main__':
    app.run(debug=True)
