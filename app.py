#9.4.3
#Create a New Python File and Import the Flask Dependency
from flask import Flask

#Create a New Flask App Instance
app = Flask(__name__)

#This __name__ variable denotes the name of the current function
# Use the __name__ variable to determine if your code is being run from the command line or if it has been imported into another piece of code
# #Variables with underscores before and after them are called magic methods in Python

#Create Flask Routes
#Define the starting point
@app.route('/')
def hello_world():
    return 'Hello world'
