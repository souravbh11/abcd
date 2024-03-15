from Flask import Flask
import config
from Project.utils import MedicalInsurance
import numpy as np

app= Flask(__name__) #creating a object of flask#
 @app.route("/")
def get_home():
    return "hello hii"

if __name__== "__main__":
   app.run()
