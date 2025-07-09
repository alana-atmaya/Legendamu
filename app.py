from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Selamat datang di LegendaMu</h1><p>Website ini sedang dalam tahap pengembangan untuk mengubah gambar menjadi video cinematic.</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
