from bottle import route, run, response
from mongo import MongoManager
import json

@route('/')
def root():
	return ""



# FUNCIONES RELATIVAS A USUARIO

@route('/users', method='GET')
def getListOfUsers():
	mng = MongoManager()
	dbResult=mng.get("tests") 
	response.set_header("Content-Type:","text/json")

	result =json.dumps(dbResult)
	return result

@route('/users', method='POST')
def getListOfUsersPOST():
	return "Not implemented"

@route('/users/<user>', method='GET')
def getUser(user):
	doc={"_id":user}
	mng = MongoManager()
	dbResult=mng.get("tests",doc) 
	response.set_header("Content-Type:","text/json")




if __name__ == '__main__':

	run(debug=True,reloader=True)
