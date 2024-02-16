from flask import Blueprint, render_template

bp = Blueprint('test_combat', __name__)

@bp.route('/image', methods = ['GET'])
def serve_image():
    "a simple HTTP image"
    return render_template('image.html')