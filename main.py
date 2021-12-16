'''
Oliver Erdmann
12/2/21
twilio messaging and calling
'''

from twilio.rest import Client
from tkinter import *
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

root = Tk()
root.title("text someone")
root.geometry("250x105")
root.configure(bg='white')

# creating the client var
# create a twilio account and put your own sid and auth token
account_sid = "your sid"
auth_token = "your auth token"
client = Client(account_sid, auth_token)

# send message
def text():
    message = client.messages.create(
        to="+1 receiving number",
        # must go to twilio - console - phone numbers - manage - verified caller IDs - add the phone number
        from_="+1 twilio number",
        body=user_text_input.get(),
    )

# text input label
text_input = Label(root, text='What would you like to say?', font=('calibre', 10, 'bold'))
text_input.pack(side=TOP, pady=3)

# user input for message
user_text_input = Entry(root, width=250, font=('calibre', 10, 'normal'))
user_text_input.pack(side=TOP, pady=9)

# buttons for text and call
text_button = Button(root, text='text', command=text)
text_button.pack(side=BOTTOM, pady=6)

app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    body = request.values.get('Body', None)
    resp = MessagingResponse()


root.mainloop()