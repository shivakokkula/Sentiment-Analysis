import tweepy
from pygooglenews import GoogleNews
import pandas as pd

def get_tweets():
    bearer_token='AAAAAAAAAAAAAAAAAAAAAOycZgEAAAAA46lWMN9lTrOR6V5cgqCc51pMdoE%3D7qQOWJfk4t43oWTvqCMmndpkE2LDAcmbbLyCAiK4lqK2UpUJTI'
    consumer_key= 'kfEpRZylqrx6sCOfyQ1qJl4r4'
    consumer_secret= 'ORnhGiYiyiRPi7f3VkQ1qV6H9TJcneV6EblSmG6QrvNKZvilN0'
    access_token= '1497433308992794625-AmAxwuCNA4TPMdDukeV50sISaREMPi'
    access_token_secret= 'xHFK6yazYvTkQ8LUL9F8IHJDosxhxsbexfEg4pZKUJvXX'
    client = tweepy.Client(bearer_token=bearer_token,consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_token_secret)
    query = 'green hydrogen'
    tweets = client.search_recent_tweets(query=query,max_results=10,tweet_fields=['created_at','text','entities'])
    tweetlist=[]
    for tweet in tweets.data:
        if 'entities' in tweet:
            if 'mentions' in tweet.entities.keys():
                tweetlist.append([tweet.entities['mentions'][0]['username'],tweet.created_at,tweet.text])
    return tweetlist

def get_google_news():
    gn=GoogleNews()
    search=gn.search('green hydrogen')
    newslist=[]
    for item in search['entries']:
        newslist.append([item['source']['title'],item['published'],item['title'].split(' - ')[0]])
    return newslist
tweetlist=get_tweets()
newslist=get_google_news()
articles=tweetlist+newslist
df=pd.DataFrame(articles,columns=['Date','Content','Source'])
print(df)
df.to_csv("data.csv")
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
df['sentiment']=sentiment_pipeline(df['Content'])
df.to_csv("sentinet.csv")