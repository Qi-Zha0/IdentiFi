import serial
import json
import firebase_admin
from cardGUI import guiDisplay
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('/home/qi/hackmit/readCard/identifi-e2b81-firebase-adminsdk-l3ob2-21032827c4.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

#logs the device number into devicelist.txt if not present
def logDevice(uid):
	with open("devicelist.txt", "a+") as file:
    		for line in file:
        		if uid in line:
           			break
    		else: # not found, we are at the eof
	        	file.write(uid) # append missing data
	        	file.write("\n")

	file.close()
	return

def displayInfo(UID):
	users_ref = db.collection(u'users')
	print("fetching profile..")
	docs = users_ref.where(u'rfid', u'==', unicode(UID)).get()
	for doc in docs: #each doc is a user's file
		dictInfo = doc.to_dict()
		fullInfo = u'{} => {}'.format(doc.id, dictInfo)
		guiDisplay(dictInfo)
		print fullInfo

	return

#############################################################3
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
UID = ''

while True:
    data = arduino.readline()
    if data:
        UID = data[:-2]
        logDevice(UID)
        displayInfo(UID)
        print(UID) #a string of uid

