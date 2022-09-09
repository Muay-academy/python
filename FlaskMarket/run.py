from market import app
from flask import Flask
import os
import socket

#Checks if the run.py file has executed directly and not imported
#Run this command to run the application in DEBUG mode
#docker build . -t flask_app_dev
#docker run -p 5000:5000 -e DEBUG=1 flask_app_dev
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('DEBUG') == '1')