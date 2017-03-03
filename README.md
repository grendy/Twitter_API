# Twitter_API
Twitter_API using Twython
#Requirement
Python2.7 must be installed on the device
```bash
pip install twython 
pip install kafka 
```
#Send data to kafka
```bash
producer = KafkaProducer(bootstrap_servers=settings.broker)
producer.send(settings.kafka_topic, json_tweet)
```                                    
##Get Oath twitter
Go to https://apps.twitter.com/ to register your app to get your api keys

##Running engine
```bash
python2.7 twitter_api.py
```
