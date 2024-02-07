from flask import Flask
import random 

app = Flask(__name__)

@app.route('/combat')
def dice_roll() -> str:
    numbers = random.randint(1, 20)

    if numbers == 1:
        return 'critical miss!'
    if numbers == 20:
        return 'critical hit!'
    else:
        return 'you roll for ' + str(numbers) + ' damage!'
    
@app.route('/advantage')
def adv_endpoint() -> str:
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

@app.route('/disadvantage')
def dis_endpoint() -> str:
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

if __name__ == '__main__':
    app.run(host='localhost', port=8081)