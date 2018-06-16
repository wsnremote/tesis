import twitter
import sys

api = twitter.Api(consumer_key='GEhDM21zab0umymr8XcMdPX8V',
  consumer_secret='5gF43JjkufNqi5HY9WFPzYdwegfbBuDNIuM8AJe9ZgheYn01CJ',
  access_token_key='1007907322902007808-Xeatas7xTUd4Q04amWoyGS1W8jJLqG',
  access_token_secret='UR8DZw7UG9inAgkEBU45R43ELZvTDXGrL4crRLN8AczXR')

#print(sys.argv)
try:
	status = api.PostUpdate(sys.argv[2]+' '+sys.argv[3]+' '+sys.argv[4]+' '+sys.argv[5]+' '+sys.argv[6]+' '+sys.argv[7]+' '+sys.argv[8]+' del usuario: '+sys.argv[1]+' '+sys.argv[9]+' '+sys.argv[10]+' '+sys.argv[11]+' '+sys.argv[12]+' '+sys.argv[13])
except:
	pass
