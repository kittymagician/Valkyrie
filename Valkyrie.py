from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
account_sid = "twilio SID goes here" #Twilio SID 
auth_token  = "twilio auth token goes here" #Twilio Auth Token
client = Client(account_sid, auth_token)
responder_number = "Your Responder Number Goes here" # The number you want requests to forward to.
twilio_number = "Your Twilio Number Goes Here." # The Twilio number that serves the bot.
default_resp = "I have forwarded on your request to the community support team"
fallback_resp = "Welcome to the Emergency Response SMS bot. What do you need support with? Say Food Shopping for Food Shopping, Mediciation for Medication, emotional support call for emotional support phone call."
app = Flask(__name__)

@app.route("/sms", methods =['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body'].lower()
    print(message_body)
    resp = MessagingResponse()
    if message_body == 'hi':
      response_message = fallback_resp
    if 'food shopping' in message_body:
      response_message = 'Great! What food do you require? Say I need food followed by the items. For example \'I need 1 tinned beans\''
    elif 'i need' in message_body:
      helper_resp = message_body.replace('i need ', '')
      helper_message = 'a new food request has come in from the following number: ' + number + ' for the following items: ' + helper_resp
      message = client.messages.create(
          to=responder_number, 
          from_=twilio_number,
          body=helper_message)
      response_message = default_resp
    elif 'medication' in message_body:
      response_message = 'Great! Where do we need to pick your medications up from and is the perscription paid/free? Say for example \'pick up from spires pharmacy free prescription in the name of John Doe\''
    elif 'pick up' in message_body:
      helper_resp = message_body.replace('pick up from ', '')
      helper_message = 'a new medication request has come in from the following number: ' + number + ' for the following: ' + helper_resp
      message = client.messages.create(
          to=responder_number, 
          from_=twilio_number,
          body=helper_message)
      response_message = default_resp
    elif 'emotional support call' in message_body:
      helper_message = 'a new emotional support phone call request has come in from the following number: ' + number
      message = client.messages.create(
          to=responder_number, 
          from_=twilio_number,
          body=helper_message)
      response_message = default_resp
    else:
      response_message = fallback_resp

    resp.message(response_message)

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000')
