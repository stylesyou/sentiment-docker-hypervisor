from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s



#consumer key, consumer secret, access token, access secret.
ckey="sUeFRv8pilAPHOj72ixZmwx2D"
csecret="3AG24gawDQko0hBvYibsqTOQ9Vosn4vUPrjr9M6gywnMIJ7lMc"
atoken="3810009132-IZU13pDx2BK6S3viphMqiWewLKcqDTu4CrxTxNY"
asecret="hbOOFKWcLQdjlu1i41NTLHf584P0aWATSVDPQkU8TQNCP"


class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]
            print(tweet)

            if confidence*100 >= 50:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()

            return True
        except:
            return True
        
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["President Trump"])


