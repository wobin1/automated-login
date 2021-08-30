from twilio.rest import Client 
 
account_sid = 'ACb3964e7314c7af4d9f5c44d978bb3bb5' 
auth_token = '470504e0a3575b807ab1bbceb57028af' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='There was once a man',      
                              to='whatsapp:+2348144169123' 
                          ) 
 
print(message.sid)