from mongo import MongoManager

doc={
	"nome":"Ruben2",
	"email":"r@gmail.com"
}

print "insert item 1"
mng= MongoManager()
IDResult=mng.add("tests",doc)
print IDResult
print doc
del doc["_id"]
print "insert item 2"
IDResult=mng.add("tests",doc)
print IDResult
print "find item 2"

filterDoc ={"_id":IDResult}
resultDoc=mng.get("tests",filterDoc)
print resultDoc
print "find all items"
resultDoc= mng.get("tests")
print resultDoc