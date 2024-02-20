from flask import Blueprint, render_template
import random


bp = Blueprint('test_combat', __name__)

@bp.route('/combat', methods = ['GET'])
def dice_roll() -> str:
    """ A function that rolls a 20 sided dice and outputs the value """
    numbers = random.randint(1, 20)

    if numbers == 1:
        return 'critical miss!'
    if numbers == 20:
        return 'critical hit!'
    else:
        return 'you roll for ' + str(numbers) + ' damage!'
    
@bp.route('/advantage', methods = ['GET'])
def adv_endpoint() -> str:
    """ A function that rolls two 20 sided dice and returns the greater value """
    dice_one = random.randint(1, 20)
    dice_two = random.randint(1, 20)
    
    if dice_one > dice_two:
        if dice_one == 1:
            return 'critical miss!'
        if dice_one == 20:
            return 'critical hit!'
        else:
            return 'you roll for ' + str(dice_one) + ' damage!'
        
    if dice_two > dice_one:
        if dice_two == 1:
            return 'critical miss!'
        if dice_two == 20:
            return 'critical hit!'
        else:
            return 'you roll for ' + str(dice_two) + ' damage!'

    else:
        if dice_one == 1:
            return 'critical miss!'
        if dice_one == 20:
            return 'critical hit!'
        else:
            return 'you roll for ' + str(dice_one) + ' damage!'

@bp.route('/disadvantage', methods = ['GET'])
def dis_endpoint() -> str:
    """ A function rolling two 20 sided dice and returning the lesser value """
    dice_one = random.randint(1, 20)
    dice_two = random.randint(1, 20)
    
    if dice_one < dice_two:
        if dice_one == 1:
            return 'critical miss!'
        if dice_one == 20:
            return 'critical hit!'
        else:
            return 'you roll for ' + str(dice_one) + ' damage!'
        
    if dice_two < dice_one:
        if dice_two == 1:
            return 'critical miss!'
        if dice_two == 20:
            return 'critical hit!'
        else:
            return 'you roll for ' + str(dice_two) + ' damage!'

    else:
        if dice_one == 1:
            return 'critical miss!'
        if dice_one == 20:
            return 'critical hit!'
        else:
            return 'you roll for ' + str(dice_one) + ' damage!'
        
@bp.route('/image', methods = ['GET'])
def serve_image():
    "a function generating an image "
    return render_template('image.html')