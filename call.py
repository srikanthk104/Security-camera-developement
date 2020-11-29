from twilio.rest import Client

def call(number):
    account_sid = 'AC1597866df904b82962c9cb82ca75ddb8'
    auth_token = 'ba9bcb425d14e6392b467df5f00b648d'
    client = Client(account_sid, auth_token)
    call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=number,
                        from_='+12055461437')
    print(call.sid)

