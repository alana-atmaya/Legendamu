
from flask import Flask, request, redirect, url_for import os from werkzeug.utils import secure_filename

app = Flask(name) UPLOAD_FOLDER = 'static/uploads' app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/') def home(): return ''' <!DOCTYPE html> <html lang="id"> <head> <meta charset="UTF-8"> <title>LegendaMu - Gambar ke Video</title> </head> <body> <h1>LegendaMu</h1> <p>Unggah gambar Anda untuk melihat hasil video cinematic.</p> <form action="/upload" method="POST" enctype="multipart/form-data"> <input type="file" name="image" accept="image/*" required><br><br> <button type="submit">Ubah Jadi Video</button> </form> </body> </html> '''

@app.route('/upload', methods=['POST']) def upload_image(): if 'image' not in request.files: return "Gagal: Tidak ada file gambar." file = request.files['image'] if file.filename == '': return "Gagal: Tidak ada nama file." if file: filename = secure_filename(file.filename) os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True) file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) return redirect(url_for('show_video'))

@app.route('/video') def show_video(): return ''' <!DOCTYPE html> <html lang="id"> <head><meta charset="UTF-8"><title>Hasil Video</title></head> <body> <h2>Hasil Video Cinematic</h2> <video width="480" controls autoplay loop> <source src="/static/sample_video.mp4" type="video/mp4"> Browser Anda tidak mendukung tag video. </video> <br><br> <a href="/">⬅️ Kembali</a> </body> </html> '''

if name == 'main': app.run(debug=True, host='0.0.0.0', port=10000)

