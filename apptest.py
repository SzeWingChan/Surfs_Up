#9.4.3
#Skill drill

#Create a New Python File and Import the Flask Dependency
from flask import Flask

#Create a New Flask App Instance
apptest = Flask(__name__)

#Create Flask Routes
#Define the starting point
@apptest.route('/')
def test():
    return 'test', 
