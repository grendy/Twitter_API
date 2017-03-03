# Twitter_API
Twitter_API using Twython
#Requirement
Python2.7 must be installed on the device
```bash
pip install twython 
pip install kafka 
```
##Get access to twitter
Go to https://apps.twitter.com/ to register your app to get your api keys
```bash
CONSUMER_KEY = settings.consumer_key
CONSUMER_SECRET = settings.consumer_secret
ACCESS_KEY = settings.access_token
ACCESS_SECRET = settings.access_secret
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
```
##Connect to mysql
Connect to mysql using MySQLdb library
```bash
conn = MySQLdb.connect(
            host=settings.host,
            port=settings.port,
            user=settings.user,
            passwd=settings.passwd,
            db=settings.db)
```
##Get tweet
Get all tweet from user timeline
```bash
user_timeline = twitter.get_user_timeline(screen_name=account,count=1)
```
Get all mention tweet and retweet
```bash
search_tweeet = twitter.search(q=account, result_type='recent',count=hitung, retweeted = True)
```
#Send data
Send data to kafka 
```bash
producer = KafkaProducer(bootstrap_servers=settings.broker)
producer.send(settings.kafka_topic, json_tweet)
```                                    
##Running engine
To running engine use crontab for automatic scheduling
```bash
python2.7 twitter_api.py
```
