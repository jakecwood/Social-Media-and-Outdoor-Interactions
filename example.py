#This is the first part
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


#This is the second part. You must replace the text with your keys and secrets.
ckey = 'consumer_key'
csecret = 'consumer_secret'
atoken = 'access_token'
asecret = 'access_secret'

#This is the third part.
class listener (StreamListener):

    def on_data(self, data):

            print (data)

            saveFile = open('twitDB.json','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True

    def on_error(self, status):
        print (status)

#This is the fourth part. Don't forget to replace the keywords with the ones you want to use.
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["REPLACE"])
