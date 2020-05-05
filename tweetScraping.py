import GetOldTweets3 as gt
import numpy as np
import datetime
import pandas as pd

### NOTE I WOULD NOT RUN THIS,

### I had to let this run overnight for this to completely run, and it crashed my vm
### In hindsight I would
maxTweets = 1000

search = 'coronavirus'

untilDate = datetime.date.today() + datetime.timedelta(1)
untilDate = untilDate.strftime("%Y-%m-%d")

tweetTextList = []
tweetDateList = []

numDays = 80

i = 1
untilDate = datetime.date.today() + datetime.timedelta(i)
while i <= numDays:
    untilDate = untilDate.strftime("%Y-%m-%d")

    tweetCriteria = gt.manager.TweetCriteria().setTopTweets(True) \
        .setQuerySearch(search).setMaxTweets(maxTweets) \
        .setSince("2020-02-01").setUntil(untilDate)
    tweets = gt.manager.TweetManager.getTweets(tweetCriteria);

    untilDate = datetime.date.today() - datetime.timedelta(i)
    i += 1
    for tweet in tweets:
        tweetTextList.append(tweet.text)
        tweetDateList.append(tweet.date)

dfTweets = pd.DataFrame(list(zip(tweetDateList, tweetTextList)))



dfTweets.to_csv('finalTweets.csv', sep=',', encoding='utf-8')
