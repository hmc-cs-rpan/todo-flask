from flask import Flask, request
from models import Schema
from service import ItemService

app = Flask(__name__)             

@app.route("/")                   
def hello():                      
    return "Hello World!"  

@app.route("/item", methods=["POST"])
def create_item():
    return ItemService().create_item(request.get_json())

if __name__ == "__main__":  
	Schema()
	app.run() 
