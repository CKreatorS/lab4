from flask import Flask
import random 

app = Flask(__name__)

def dice_roll()->str:
    numbers = random.randint(1, 20)
    
    if numbers == 1:
        return 'critical miss!'
    if numbers == 20:
        return 'critical hit!'
    else:
        return 'you roll for ' + numbers + ' damage!'