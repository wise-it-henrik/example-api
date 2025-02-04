from flask import Flask, request, jsonify
import os, json, random

app = Flask(__name__)
json_folder = 'json_files'

# Ensure the json_files folder exists
if not os.path.exists(json_folder):
    os.makedirs(json_folder)

# Generate three files with id 1-3 with sample text if the folder is empty
content = [
    "Lorem ipsum dolor",
    "Hello world!",
    "Roses are red, violets are blue"
]
if not os.listdir(json_folder):
    for i in range(1, 4):
        with open(os.path.join(json_folder, f'{i}.json'), 'w') as f:
            json.dump({"id": i, "content": f"{content[i - 1]}"}, f)

# Helper function to get the next available id
def get_next_id():
    files = os.listdir(json_folder)
    if not files:
        return 1
    ids = [int(f.split('.')[0]) for f in files]
    return max(ids) + 1

@app.route('/json-files', methods=['GET'])
def get_all_json_files():
    json_files = []
    for filename in os.listdir(json_folder):
        with open(os.path.join(json_folder, filename), 'r') as f:
            content = json.load(f)
            json_files.append(content)
    return jsonify(json_files)

@app.route('/json-files/<int:file_id>', methods=['GET'])
def get_json_file(file_id):
    filepath = os.path.join(json_folder, f'{file_id}.json')
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = json.load(f)
        return jsonify(content)
    else:
        return jsonify({"error": "File not found"}), 404

@app.route('/json-files', methods=['POST'])
def create_json_file():
    content = request.json.get('content')
    if not content:
        return jsonify({"error": "Content is required"}), 400
    
    file_id = get_next_id()
    filepath = os.path.join(json_folder, f'{file_id}.json')
    with open(filepath, 'w') as f:
        json.dump({"id": file_id, "content": content}, f)
    
    return jsonify({"id": file_id, "content": content}), 201

@app.route('/json-files/<int:file_id>', methods=['PUT'])
def update_json_file(file_id):
    content = request.json.get('content')
    mode = request.headers.get('mode')
    
    if not content:
        return jsonify({"error": "Content is required"}), 400
    
    if mode not in ['overwrite', 'append']:
        return jsonify({"error": "Invalid mode. Use 'overwrite' or 'append'"}), 400
    
    filepath = os.path.join(json_folder, f'{file_id}.json')
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            file_data = json.load(f)
        
        if mode == 'overwrite':
            file_data['content'] = content
        elif mode == 'append':
            file_data['content'] += content
        
        with open(filepath, 'w') as f:
            json.dump(file_data, f)
        
        return jsonify({"id": file_id, "content": file_data['content']})
    else:
        return jsonify({"error": "File not found"}), 404

@app.route('/json-files/<int:file_id>', methods=['DELETE'])
def delete_json_file(file_id):
    filepath = os.path.join(json_folder, f'{file_id}.json')
    if os.path.exists(filepath):
        os.remove(filepath)
        return jsonify({"message": "File deleted"})
    else:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)