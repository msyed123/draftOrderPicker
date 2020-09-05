import os
import random

from flask import Flask, render_template

app = Flask(__name__)
names = ["Dave", "Ethan", "Evan", "Juan", "Kyle", "Malcolm", "Mamoon", 
        "Matt", "Moses", "Sam"]
picks = {}

def picker():
    def spin():
        nums = [x for x in range(1, 11, 1)]
    
    
        for i in range(0,len(nums)):
            pick = random.choice(nums)
            picks[names[i]] = pick
            nums.remove(pick)
            
    spin()
    while picks["Malcolm"] > 3:
        spin()
        
    return picks

@app.route('/')
def doIt():
    return render_template('button.html')


@app.route('/draft')
def runIt():
    picks = picker()
    sortedPicks = sorted(picks.items(), key=lambda x: x[1])
    return render_template('list.html', picks=sortedPicks)
    
app.run(host='localhost', port='8080')
