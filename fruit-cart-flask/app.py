from flask import Flask, session, redirect, url_for, escape, request,render_template
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import json
app = Flask(__name__)
app.secret_key = "tashi"

engine = create_engine('sqlite:///fruits.sqlite', connect_args={'check_same_thread': False}) # allow us to interact with database
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    fruit = Column(String(15))
    price = Column(Integer)
    number = Column(Integer)
    total = Column(Integer)
     
Session = sessionmaker(bind=engine)
sess = Session()
Base.metadata.create_all(engine)

@app.route('/')
def load():
	return render_template('home.html')

@app.route('/<fid>/<name>/<price>')
def addCart(fid, name, price):
	session[fid]=[name,price]
	return render_template('home.html', session=session)

@app.route('/checkout/', methods=['POST'])
def checkOut():
	return render_template('checkout.html', result=session)

@app.route('/placeorder/', methods = ['POST'])
def placeorder():
	flist = ""
	plist = ""
	total_amount = request.form['total_amount']
	phone_number = request.form['number']
	for key,value in session.items():
		flist += value[0] + ", "
		plist += value[1] + ", "
	
	item = User(fruit = flist, number=phone_number,price=plist, total=total_amount)		
	sess.add(item)
	sess.commit()	
	[session.pop(key) for key in list(session.keys())]	
	return render_template('home.html')		
