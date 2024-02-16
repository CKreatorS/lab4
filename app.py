from flask import Flask, render_template
from route import bp

# function defines an app within flask
def create_app():
    app = Flask(__name__)

# registers app 
    app.register_blueprint(bp)
    return app

app = Flask(__name__)

IMG_DIR = './static'

@app.route('/image')
def serve_image():
    "a simple HTTP image"
    return render_template('image.html')

if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=8081)