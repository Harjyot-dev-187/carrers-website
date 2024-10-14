from flask import Flask, render_template  # importing Flask class from flask module
app = Flask(__name__) # app object of class Flask, __name__ when printed goes to main - used to invoke main of program

# any website can be accesed through only url, where url changes when we navigate through website

@app.route("/") # this will route to  the website domain name after that is only slash means it is home page
def hello_world():
    # return "Hello jovian" # it means whenever url / is accesed than show helloworld
    return render_template('home.html')  # render template is used to run our templte

# Now use pen and paper and think what you want to show on page
# make a few pages go duty and first make skeleton than you improve it
# use unsplash.com to get good images
# Any image present in static.Any thing here can be shared by flask externally 
# added html and css and now use bootstrap tp use predesigned style, search for bootstrap css.
# to add bootstrap see docs - on left side of bootstrap site you see various utility classes. use those styles classes
# can use various bootstrap classes to make front end better

# show dynamic data in web page
# flask way to insert dynami data see jobs example in free code camp lecture- {{jobs}} 

# instead of returing html we can also return json


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)