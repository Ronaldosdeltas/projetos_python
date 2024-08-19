from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
   return 'BEM VINDO AO SITE!'


app.run()