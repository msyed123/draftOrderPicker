# -*- coding: utf-8 -*-

'''Entry point to all things to avoid circular imports.'''
import os
import random

from flask import Flask, render_template

sortedPicks = []
unsortedPicks = []
calculated = False
counter = 0
finished = True

names = ["Dave", "Ethan", "Evan", "Juan", "Kyle", "Malcolm", "Mamoon", 
        "Matt", "Moses", "Sam"]
picks = {}
app = Flask(__name__)

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


def runIt():
    global sortedPicks, unsortedPicks, counter, finished
    unsortedPicks = picker()
    sortedPicks = sorted(picks.items(), key=lambda x: x[1])
    counter = 0
    finished = True

@app.route('/draft')
def addOne():
    global sortedPicks, counter, calculated, finished
    if calculated is False:
        runIt()
        calculated = True
    counter += 1
    if counter is len(names):
        finished = False
    return render_template('list.html', picks=sortedPicks[-counter:], showButton=finished)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)