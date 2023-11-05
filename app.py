from flask import Flask
from sqlalchemy import create_engine
from models.models import *

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+mysqlconnector://root:course123@localhost/STI data'
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URL'], echo=True)

Base.metadata.create_all(engine)

@app.route('/')
def index():
    return 'Hello World'

if__name__=='__main__'
    app.run(debug= True)