from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from mapreduce import ParallelMapReduce
import os
import tempfile
import re

app = Flask(__name__, 
            static_folder='static',
            static_url_path='/static')

CORS(app)

# Ensure uploads directory exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def serve_frontend():
    return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/api/wordcount', methods=['POST'])
def word_count():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    n_workers = int(request.form.get('workers', 4))
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Save the uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    try:
        # Read the file
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = [line for line in f if line.strip()]
        
        # Create and execute MapReduce job
        mapreduce = ParallelMapReduce(n_workers=n_workers)
        result = mapreduce.execute(lines, word_count_map, word_count_reduce)
        
        # Clean up the uploaded file
        os.remove(filepath)
        
        # Convert result to list of dicts for JSON serialization
        word_counts = [{'word': word, 'count': count} 
                      for word, count in sorted(result.items())]
        
        return jsonify({
            'success': True,
            'results': word_counts,
            'total_words': len(word_counts)
        })
    
    except Exception as e:
        # Clean up the uploaded file in case of error
        if os.path.exists(filepath):
            os.remove(filepath)
        return jsonify({'error': str(e)}), 500

def word_count_map(document):
    words = re.findall(r'\w+', document.lower())
    return [(word, 1) for word in words]

def word_count_reduce(word, counts):
    return sum(counts)

if __name__ == '__main__':
    app.run(debug=True) 