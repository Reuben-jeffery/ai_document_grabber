from flask import Flask, request, jsonify
import os
from ai_document_grabber.downloader import download_ai_document

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"message": "API is running successfully!"}), 200

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    file_url = data.get('url')
    filename = data.get('filename')

    if not file_url or not filename:
        return jsonify({"error": "URL and filename are required"}), 400

    try:
        download_ai_document(file_url, filename)
        return jsonify({"message": f"Downloaded file to {filename} successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

