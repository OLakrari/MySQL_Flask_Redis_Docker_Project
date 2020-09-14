from backend.classes import Citizen
from flask import render_template, request, jsonify
from backend import backend, db, fbcrypt, redis
import hashlib, base64, json, time


#curl --header "Content-Type: application/json" --request POST --data '{"citizen_name" : "Oumayma Lakrari" , "citizen_code" : "XCXF59213" , "citizen_CIN" : "Ouff Im tired" , "citizen_id" : 9}' http://127.0.0.1:5000/SubmitCitizenInfo
@backend.route('/SubmitCitizenInfo', methods=['POST'])
def submit_citizen_informations():
	start_time = time.clock()
	values = request.get_json()
	print(values, type(values))
	citizen_name = values["citizen_name"]
	citizen_code = values["citizen_code"]
	citizen_CIN = values["citizen_CIN"]
	citizen_id = values["citizen_id"]
	print('Pinging redis ... ', redis.ping())

	try :
		db.create_all()
		print('Starting db ...')
		y = redis.get(citizen_id)
		a = str(citizen_code) + str(citizen_CIN) + "__id" + str(citizen_id)
		b = a*9
		c = base64.b64encode(hashlib.sha256(b.encode('UTF-8')).digest())
		hashed_code = fbcrypt.generate_password_hash(c).decode("utf-8")
			
		if (y is None or len(y)<=1) :
			print('data not in the cache ...')
			x = Citizen.query.filter_by(citizenname = citizen_name).all()
			print('cheking data in db ..', x)
			if not x :
				print('Adding citizen to database ... ')
				citizen = Citizen(ID=citizen_id, citizenname = citizen_name, citizencin = citizen_CIN, citizenpass=hashed_code)
				print(citizen)
				db.session.add(citizen)
				db.session.commit()
				print('Setting citizen in cache ...')
				citizen_object = {
					'citizenname' : citizen_name,
					'citizenpass' : hashed_code,
					'citizencin' : citizen_CIN,
				}
				redis.set(citizen_id, json.dumps(citizen_object))
				print(time.clock() - start_time )
				return render_template('error.html', Current_error = Citizen.query.filter_by(ID = citizen_id).first())
			else :
				c = Citizen.query.filter_by(citizenpass = hashed_code).first()
				print('fetching data from database ...')
				citizen_object = {
					'citizenname' : citizen_name,
					'citizenpass' : hashed_code,
					'citizencin' : citizen_CIN,
				}
				redis.set(c.ID , json.dumps(citizen_object))
				print(time.clock() - start_time )
				return render_template('error.html', Current_error = Citizen.query.filter_by(ID = citizen_id).first())
		print('Returning data from the cache ... ')
		print(time.clock() - start_time )
		return render_template('error.html', Current_error = str(json.loads(redis.get(citizen_id))))
			
	except Exception as e:
		return {'Error ': 'Message : {}'.format(e)}	

#curl --request GET http://127.0.0.1:5000/cleanthemess
@backend.route('/cleanthemess')	
def cleanthemess():
	db.drop_all()
	for key in redis.keys():
		redis.delete(key)
	return render_template('error.html', Current_error= '__All_deleted___')

