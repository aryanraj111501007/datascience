import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
 
class TwitterClient(object):
   
    def __init__(self):
        
       
        consumer_key = 'qDbAduteimrMT6gt2F4FezbQZ'
        consumer_secret = 'mLTc90qg3uAEgxdXXnTrcjHsM5P2RfE4NezFpmlA7LlHW5qX31'
        access_token = '910051464449376256-ksRK7dSyegQBkJDMEuGCKLTIBSyi72R'
        access_token_secret = '5cEtr9hUp5Q9zOoz5IowYIjt3CySYa9uxbmMnvFlVrthF'
 
        
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
       
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())
                                   
                                    
                          
 
    def get_tweet_sentiment(self, tweet):
       
       
        analysis = TextBlob(self.clean_tweet(tweet))
      
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
 
    def get_tweets(self, query, count = 10):
        
       
        tweets = []
 
        try:
           
            fetched_tweets = self.api.search(q = query, count = count)
            
 
            
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}
 
                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
 
               
                if tweet.retweet_count > 0:
                    
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            
            return tweets
 
        except tweepy.TweepError as e:
            
            print("Error : " + str(e))
 
def main():
   
    api = TwitterClient()
   
    movie=input("give name of movie\n")
    tweets = api.get_tweets(query = movie, count = 200)
    #print(len(tweets))
 
   
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    
    #print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    
    #print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    
   
       
    temp=(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets))
    print("succes chance is" +str(temp/2+(100*len(ptweets)/len(tweets))))
   
    
 

main()
