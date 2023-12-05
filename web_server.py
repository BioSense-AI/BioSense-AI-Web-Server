import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from random import randint
import json
from read_adc import get_ecg_adc
from serve_dump import get_point, get_points
host_name = '0.0.0.0'  # Broadcasting Address
# host_name = ''  # can also use empty string to broadcast
host_port = 8000
integral = 0

def setupGPIO():
    pass
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)
    # GPIO.setup(18, GPIO.OUT)
    # GPIO.setup(19, GPIO.IN)

spO2 = 97
bpm = 105
state = 'Normal'
stress= 'High'

def getState():
    global state
    return state

def getStress():
    Numbers = [95,99,102,104,92]
    random_number = randint(0,4)
    if Numbers[random_number] > 100:
        return 'Very High'
    else:
        return 'High'
    
def getSPO2():
    Numbers = [97,98,99,100,95]
    random_number = randint(0,4)
    return str(Numbers[random_number])
# def getSPO2():
#     global spO2
#     spO2 += 1
#     return str(spO2)

def getTemp():
    Numbers = [97, 99, 102, 104, 92]
    random_number = randint(0, 4)
    if Numbers[random_number] > 100:
        return 'High'
    else:
        return 'Very High'
def getBPM():
    Numbers = [95,99,102,104,92]
    random_number = randint(0,4)
    return str(Numbers[random_number])

def get_data():
    # Replace this with your actual ECG data from the ADC
    # You might need to convert it to a JSON format
    ecg_data = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    return json.dumps({'ecg_data': ecg_data})

class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
                
        if self.path == '/state_page':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            state_value = getState()
            self.wfile.write(state_value.encode("utf-8"))
        elif self.path == '/stress_page':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            stress_value = getStress()
            self.wfile.write(stress_value.encode("utf-8"))
        elif self.path == '/spo2':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            spo2_value = getSPO2()
            self.wfile.write(spo2_value.encode("utf-8"))

        elif self.path == '/temp':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            temp_value = getTemp()
            self.wfile.write(temp_value.encode("utf-8"))

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # data_point = get_ecg_adc()
            data_point = get_point()
            # self.wfile.write(str(data_point).encode("utf-8"))
            self.wfile.write(str(data_point).encode("utf-8"))
        else:
            html = open('./index.html').read()
            self.do_HEAD()
            self.wfile.write(html.encode("utf-8"))

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        post_data = post_data.split("=")[1]

        setupGPIO()

        if post_data == 'On':
            print("Pi_LED will on")
            # GPIO.output(18, GPIO.HIGH)
        else:
            print("Pi_LED will off")
            # GPIO.output(18, GPIO.LOW)

        print("LED is {}".format(post_data))
        self._redirect('/')

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("biosense server starting - %s:%s" % (host_name, host_port))
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()