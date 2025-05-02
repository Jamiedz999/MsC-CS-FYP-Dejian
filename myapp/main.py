from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt'}

article_content = None

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    global article_content
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                with open(filepath, 'r', encoding='utf-8') as f:
                    article_content = f.read()
    return render_template('index.html', content=article_content)

@app.route('/search', methods=['POST'])
def search():
    global article_content
    search_term = request.form.get('search_text')
    print(f"搜索词: {search_term}")
    print(article_content)
    if article_content and search_term:
        process = subprocess.Popen(['python', 'search_algo.py', search_term, article_content],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(timeout=5)
        highlighted_sentence = stdout.decode('utf-8').strip()
        print(f"高亮句子: {highlighted_sentence}")
        return jsonify({'highlighted_sentence': highlighted_sentence})

    return jsonify({'highlighted_sentence': None})

if __name__ == '__main__':
    app.run(debug=True)