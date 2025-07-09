from flask import Flask, request, send_file
from moviepy.editor import *
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return 'Legendamu Flask Backend Aktif'

@app.route('/generate', methods=['POST'])
def generate():
    file = request.files.get('image')
    if not file:
        return 'No file uploaded', 400

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    input_path = os.path.join(UPLOAD_FOLDER, f"input_{timestamp}.png")
    output_path = os.path.join(RESULT_FOLDER, f"video_{timestamp}.mp4")
    file.save(input_path)

    try:
        duration = 5
        clip = ImageClip(input_path).set_duration(duration)
        zoomed = clip.fx(vfx.resize, 1.1).fadein(1).fadeout(1)

        w, h = zoomed.size
        target_h = int(w / 2.35)
        bar = (h - target_h) // 2
        cinematic = zoomed.crop(y1=bar, y2=h - bar)

        cinematic.write_videofile(output_path, fps=24, codec='libx264', audio=False)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return f'Error: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)
