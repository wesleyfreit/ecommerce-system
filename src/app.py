from flask import Flask
from db.migrations import db
from config.constants import *

app = Flask(__name__)
app.config.from_object('config.constants')

db.init_app(app)

@app.route('/')
def index():
  return 'Hello World!'

if __name__ == '__main__':
  app.run(debug=True)

