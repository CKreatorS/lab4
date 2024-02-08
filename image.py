from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/imag')
def serve_image():
    "a simple HTTP image"
    return render_template()

if __name__ == '__main__':
    app.run(host='localhost', port=8081)