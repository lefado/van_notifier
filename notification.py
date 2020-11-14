from twilio.rest import Client

from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_number='whatsapp:+34617794350'



class Twilio:
    def __init__(self):
        # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
        self.client = Client(account_sid, auth_token)
    def send(self, messages):
        bodies = [f'{m["header"]}: {m["price"]}\n{m["content"]}\n{m["link"]}'for m in messages]
        return [self.client.messages.create(body=b, from_=from_whatsapp_number, to=to_whatsapp_number) for b in bodies]