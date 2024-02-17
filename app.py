from flask import Flask, render_template
from route import bp

# function defines an app within flask
def create_app():
    app = Flask(__name__)

# registers app 
    app.register_blueprint(bp)
    return app

# defines flask in app variable
app = Flask(__name__)

IMG_DIR = './static'

# renders an image into local host
@app.route('/image')
def serve_image():
    "a simple HTTP image"
    return render_template('image.html')

# creates web browser 
if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=8081)