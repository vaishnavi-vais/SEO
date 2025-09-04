from flask import Flask, request, jsonify, render_template
from seo_generator import generate_seo_content
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate-seo', methods=['POST'])
def generate_seo():
    data = request.json
    keyword = data.get('keyword')
    
    if not keyword:
        return jsonify({'error': 'Keyword is required'}), 400
    
    try:
        seo_content = generate_seo_content(keyword)
        return jsonify(seo_content)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
