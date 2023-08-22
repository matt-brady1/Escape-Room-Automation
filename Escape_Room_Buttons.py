from flask import Flask, jsonify
from flask_cors import CORS
import RPi.GPIO as GPIO

#Prints button status to http://*IP ADDRESS*
#If button is pressed, print "Triggered" to IP address for Escape Room Master to read.
#author: Matt Brady email: mattpbrady7@gmail.com

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)#use BCM pin numbers for button inputs
GPIO.setwarnings(False)

#Button PINs for Room 1
clueButton1 = 16
startButton1 = 12
finishButton1 = 26
auxButton1 = 36

#Button PINs for Room 2
clueButton2 = 5
startButton2 = 6
finishButton2 = 13
auxButton2 = 38

#Button PINs for Room 3
clueButton3 = 23
startButton3 = 24
finishButton3 = 25
auxButton3 = 40

#Button PINs for Room 4
clueButton4 = 17
startButton4 = 27
finishButton4 = 22
auxButton4 = 37

#Setup Room 1 Buttons
GPIO.setup(clueButton1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(startButton1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(finishButton1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(auxButton1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Setup Room 2 Buttons
GPIO.setup(clueButton2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(startButton2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(finishButton2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(auxButton2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Setup Room 3 Buttons
GPIO.setup(clueButton3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(startButton3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(finishButton3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(auxButton3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Setup Room 4 Buttons
GPIO.setup(clueButton4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(startButton4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(finishButton4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(auxButton4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Set trigger value ERM looks for
triggerValue = "Triggered"

CORS(app, resources=r'/*') #set header allowing ERM access to button status

###ROOM 1###
@app.route('/Clue1')
def Clue1():
    buttonStatus = GPIO.input(clueButton1)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered"

    return jsonify(response)

@app.route('/Start1')
def Start1():
    buttonStatus = GPIO.input(startButton1)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

@app.route('/Finish1')
def Finish1():
    buttonStatus = GPIO.input(finishButton1)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

@app.route('/Aux1')
def Finish1():
    buttonStatus = GPIO.input(auxButton1)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

###ROOM 2###
@app.route('/Clue2')
def Clue2():
    buttonStatus = GPIO.input(clueButton2)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

@app.route('/Start2')
def Start2():
    buttonStatus = GPIO.input(startButton2)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

@app.route('/Finish2')
def Finish2():
    buttonStatus = GPIO.input(finishButton2)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

@app.route('/Aux2')
def Finish1():
    buttonStatus = GPIO.input(auxButton2)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)


###ROOM 3###
@app.route('/Clue3')
def Clue3():
    buttonStatus = GPIO.input(clueButton3)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

@app.route('/Start3')
def Start3():
    buttonStatus = GPIO.input(startButton3)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

@app.route('/Finish3')
def Finish3():
    buttonStatus = GPIO.input(finishButton3)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

@app.route('/Aux3')
def Finish1():
    buttonStatus = GPIO.input(auxButton3)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

###ROOM 4###
@app.route('/Clue4')
def Clue4():
    buttonStatus = GPIO.input(clueButton4)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

@app.route('/Start4')
def Start4():
    buttonStatus = GPIO.input(startButton4)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

@app.route('/Finish4')
def Finish4():
    buttonStatus = GPIO.input(finishButton4)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

@app.route('/Aux4')
def Finish1():
    buttonStatus = GPIO.input(auxButton4)
    if(buttonStatus == 0):
        response = triggerValue
    else:
        response = "Not Triggered" 

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090)
    


