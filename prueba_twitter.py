import twitter

api = twitter.Api(consumer_key='GEhDM21zab0umymr8XcMdPX8V',
  consumer_secret='5gF43JjkufNqi5HY9WFPzYdwegfbBuDNIuM8AJe9ZgheYn01CJ',
  access_token_key='1007907322902007808-Xeatas7xTUd4Q04amWoyGS1W8jJLqG',
  access_token_secret='UR8DZw7UG9inAgkEBU45R43ELZvTDXGrL4crRLN8AczXR')
#print(api.VerifyCredentials())
status = api.PostUpdate('Se activo la alarma')
print status.text
