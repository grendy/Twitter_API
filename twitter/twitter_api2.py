from twython import Twython # pip install twython
import time # standard lib
import settings
import MySQLdb
from kafka import KafkaProducer, KafkaConsumer
import json
import datetime

#''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = settings.consumer_key2
CONSUMER_SECRET = settings.consumer_secret2
ACCESS_KEY = settings.access_token2
ACCESS_SECRET = settings.access_secret2


twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
conn = MySQLdb.connect(
            host=settings.host,
            port=settings.port,
            user=settings.user,
            passwd=settings.passwd,
            db=settings.db)
cur = conn.cursor()
cou = conn.cursor()
screen_id = '2'
sql = "select screen_name from twitter_user where api!='done' and id ='{}'".format(screen_id)
cur.execute(sql)
results = cur.fetchall()
cout = "select count(*)from twitter_user where api !='done' and id ='{}'".format(screen_id)
cou.execute(cout)
b = cou.fetchall()
terus = str(b).replace(",", "").replace("'", "").replace("(", "").replace(")", "").replace("[", "").replace(
    "]", "").replace("L", "")
terus = int(terus)
print "=================+++++++=================="
print terus

global account
try:
    for ulang in range(0,terus):
        try:
            a = results[ulang]
            account = str(a).replace(",", "").replace("'", "").replace("(", "").replace(")", "")
            #=================================================================================
            # account = 'jahabarsadiq'
            #=================================================================================
            print "=================+++++++=================="
            print account
            print "=================+++++++=================="
            sql = "select api from twitter_user where screen_name='{}'".format(account)
            cur.execute(sql)
            parameter = cur.fetchall()
            parameter = str(parameter).replace(",", "").replace("'", "").replace("(", "").replace(")", "").replace("[","").replace("]", "").replace("L", "")
            if parameter != 'update':
                hitung = 15
            else:
                hitung = 10
            user_timeline = twitter.get_user_timeline(screen_name=account,count=1)
            for tweet in user_timeline:
                lis = [tweet['id']]
                print lis
            # lis = [467020906049835008,] ## this is the latest starting tweet id  #467020906049835008
            for i in range(0, 1): ## iterate through all tweets
            ## tweet extract method with the last list item as the max_id
                user_timeline = twitter.get_user_timeline(screen_name=account,count=hitung, include_retweets=True, max_id=lis[-1])
                time.sleep(1) ## 5 minute rest between api calls
                for tweet in user_timeline:
                    json_tweet = json.dumps(tweet)
                    now = datetime.datetime.now()
                    date_now = now.strftime("%A")
                    hour_now = now.strftime("%H")
                    year_now = now.strftime("%Y")
                    get_date = json.loads(json_tweet)
                    #================================================
                    tanggal = get_date['created_at']
                    tanggal = tanggal.split(' ')[0]
                    jam = get_date['created_at']
                    print jam
                    jam = jam.split(' ')[3]
                    jam = jam.split(':')[0]
                    year = get_date['created_at']
                    year = year.split(' ')[5].encode('utf-8')
                    if tanggal in date_now:
                        print "====================================================="
                        print "TWITTER_API"
                        print "====================================================="
                        banding = int(hour_now) - int(jam)
                        print banding
                        if banding < 10 and year == year_now:
                            print "======================================================"
                            print "TWITTER COY"
                            print "======================================================"
                            for kafka in range(0, 20):
                                try:
                                    producer = KafkaProducer(bootstrap_servers=settings.broker)
                                    producer.send(settings.kafka_topic, json_tweet)
                                    print "======================================="
                                    print json_tweet
                                    print "SELESAI KIRIM"
                                    break
                                except:
                                    pass
                        else:break
                    else:break
                    if banding > 10 and year != year_now:
                        break
                    # print tweet ## print the tweet
                    lis.append(tweet['id']) ## append tweet id's
            api = "update"
            sql = "UPDATE twitter_user SET api = '{}' WHERE screen_name = '{}'".format(api, account)
            cur.execute(sql)
            conn.commit()
        except:
            pass
except:pass
conn.close()

