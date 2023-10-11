from twilio.rest import Client

TWILIO_SID = "ACb185128cc7af934b601dd3f73c4fcabd"
TWILIO_AUTH_TOKEN = "093c03abe5b401ab074fc2a248aae6f4"
TWILIO_VIRTUAL_NUMBER = "+16033191069"
TWILIO_VERIFIED_NUMBER = "+91 7680023449"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        return message.sid