from flask import Flask, render_template, request, jsonify, send_file
from qr_generator import AIQRCodeGenerator
import os
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/generated'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.json
    text = data.get('text', '')
    style = data.get('style', 'circles')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Generate unique filename
    filename = f"qr_{uuid.uuid4().hex[:8]}_{style}.png"
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Generate QR code
    generator = AIQRCodeGenerator()
    try:
        generator.generate_qr(
            text=text,
            output_path=output_path,
            style=style
        )
        
        # Return the path to the generated image
        return jsonify({
            'success': True,
            'image_url': f"/static/generated/{filename}",
            'download_name': filename
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Clean up old files periodically (keep only last 100 files)
def cleanup_old_files():
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        files = [os.path.join(app.config['UPLOAD_FOLDER'], f) for f in files if f.endswith('.png')]
        files.sort(key=lambda x: os.path.getctime(x), reverse=True)
        
        # Keep only the most recent 100 files
        for old_file in files[100:]:
            try:
                os.remove(old_file)
            except:
                pass
    except:
        pass

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Clean up old files on startup
    cleanup_old_files()
    
    # Get port from environment variable for Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)