<img src="https://github.com/kittymagician/Valkyrie/blob/master/img/cover.png" width="200" height="100">

# Valkyrie
Community COVID-19 Emergency SMS Bot built with Flask, Python and Twilio.

This SMS bot has been developed to support the local community in the volume of incoming requests.

Currently the bot accepts requests for food support, mediciation and emotional support however the bot can be easily modified for any topics needed. The bot provides wake words that specifically trigger requests. For example "I need" is a wake word for food. "pick up" is a wake word for medication etc. The information is the forwarded to the volenteer to respond back to. The message also includes the sender's number so that the volenteer can call the person back to confirm the request.

# Installation

You will need a VPS/server/ngrok and a Twilio account.


Sign up to [Twilio](https://www.twilio.com/try-twilio) and top up your account.

Purchase a telephone number from Twilio and specify the number's usecase (Bot).

Obtain your SID and API key and configure your number to point to the server your going to use as a webhook.

Modify the Valkyrie.py script with the number you wish to forward requests to and the number you have purchased.

pip3 install twilio, flask  
