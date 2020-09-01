import os
from twilio.rest import Client

account_sid = 'ACd69fda12e83f4317fe54b9b2ab0f0739'
auth_token = 'ca53a04e9126a54ef7aa8c4367837dc5'
client = Client(account_sid, auth_token)

from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_number='whatsapp:+917275456455'

msg=client.messages.create(body="c",
	media_url="https://firebasestorage.googleapis.com/v0/b/emsfirebaseproject-4a5cf.appspot.com/o/Try.jpeg?alt=media&token=33d7b48d-83cc-4f5d-9787-aaa45a5c0747",
	from_=from_whatsapp_number,
	to=to_whatsapp_number)

print("Successs")