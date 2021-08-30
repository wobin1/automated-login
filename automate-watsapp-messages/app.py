from twilio.rest import Client 
 
account_sid = 'ACb3964e7314c7af4d9f5c44d978bb3bb5' 
auth_token = '0b8626c67d7cd5db9197bc849645f930' 
client = Client(account_sid, auth_token) 

def sendMessage() :
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your test is working',      
                              to='whatsapp:+2348144169123' 
                          ) 
 
    print(message.sid)
