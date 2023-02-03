from twilio.rest import Client

account_sid = 'ACd88de1ba0e1a037bec429744c7f14dd3'
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG5c0d1d7a7653ea3ea06aff72cc9c6012',
    body='I cannot believe this works',
    to='+447586025686'
)

print(message.sid)