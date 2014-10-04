# ----- Flask Hello World  -----#

#import the Flask class from the flask module
from flask import Flask

#create the applicaiton object
app = Flask(__name__)

#use decorators to link the funciton to a url
@app.route("/")
@app.route("/hello")

#define the view using a funciton, which returns a string
def hell_world():
	return "Hello, World"

#start the development server using the run() method
if __name__ == "__main__":
	app.run()

