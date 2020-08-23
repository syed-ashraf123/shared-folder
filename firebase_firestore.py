import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred=credentials.Certificate("emsfirebaseproject-4a5cf-firebase-adminsdk-kbdxt-5f8dac7ee4.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
doc=db.collection('employee').get()
for i in doc:
    print(i.to_dict())
doc=db.collection('employee').document('emp2@gmail.com')
db.collection('employee').document('emp3@gmail.com').get().to_dict()