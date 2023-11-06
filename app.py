from flask import Flask
from sqlalchemy import create_engine
from models.models import *

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Berklin21@localhost/sti data'
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

Base.metadata.create_all(engine)


# ClientProfile.__table__.create(engine, checkfirst=True)
# ClientScreening.__table__.create(engine, checkfirst=True)
# ClientTreatment.__table__.create(engine, checkfirst=True)
# PartnerManagement.__table__.create(engine, checklist=True)

@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
