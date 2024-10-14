from flask import Flask  # importing Flask class from flask module
app = Flask(__name__) # app object of class Flask, __name__ when printed goes to main - used to invoke main of program

# any website can be accesed through only url, where url changes when we navigate through website

@app.route("/") # this will route to  the website domain name after that is only slash means it is home page
def hello_world():
    return "Hello jovian" # it means whenever url / is accesed than show helloworld

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)