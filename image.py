from flask import Flask, render_template

app = Flask(__name__)

@app.route('/imag')
def serve_image():
    "a simple HTTP image"
    return render_template('blob:chrome-untrusted://media-app/fa742c2c-e46a-475a-868f-02ce1c5f7b00')

if __name__ == '__main__':
    app.run(host='localhost', port=8081)