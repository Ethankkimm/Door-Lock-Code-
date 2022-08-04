from flask import Flask
app = Flask(__name__)

import easysensors 
from easygopigo3 import EasyGoPiGo3
import time

easyGPG = EasyGoPiGo3()

easyGPG.reset_all()
easyGPG.reset_encoders()

led = easyGPG.init_led()

print('GoPiGo Initialized')

#ssh = paramiko.SSHClient()
#ssh.connect('10.247.104.29', username=pi, password=robots1234)
#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(*python3 path/name_of_file)

@app.route('/')
def index():
    # set eye color and open eyes after
    easyGPG.set_eye_color((0, 255, 0)) # Set eyes to red (can be changed
    easyGPG.open_eyes() # Send the updated color
    return 'Hello, world'
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
    
@app.route('/red')
def red():
    # set eye color and open eyes after
    easyGPG.set_eye_color((255, 0, 0)) # Set eyes to red
    easyGPG.open_eyes() # Send the updated color
    return 'Hello, world 2.0'

@app.route('/open')
def open():
    #code to open the door
    led.light_off()
    return 'Welcome home'
    
@app.route('/lock')
def lock():
    # code to lock the door again
    led.light_max()
    return 'YOU SHALL NOT PASS'