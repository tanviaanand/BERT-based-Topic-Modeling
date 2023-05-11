# Code by Ben Pretzer
# This was a de-duplication script for videos that showed up multiple times on BERTopic TikTok data collection.

import pandas as pd
import datetime

data = pd.read_csv("./aggregated_scrapes_byhashtag/second half/master_second_half_of_month.csv")
path = "./aggregated_scrapes_byhashtag/second half"
# data.columns = ['id','secretID','text','createTime','authorMeta.id','authorMeta.secUid','authorMeta.name','authorMeta.nickName','authorMeta.verified','authorMeta.signature','authorMeta.avatar','authorMeta.following','authorMeta.fans','authorMeta.heart','authorMeta.video','authorMeta.digg','musicMeta.musicId','musicMeta.musicName','musicMeta.musicAuthor','musicMeta.musicOriginal','musicMeta.musicAlbum','musicMeta.playUrl','musicMeta.coverThumb','musicMeta.coverMedium','musicMeta.coverLarge','musicMeta.duration','covers.default','covers.origin','covers.dynamic','webVideoUrl','videoUrl','videoUrlNoWaterMark','videoApiUrlNoWaterMark','videoMeta.height','videoMeta.width','videoMeta.duration','diggCount','shareCount','playCount','commentCount','downloaded','mentions','hashtags','effectStickers','Hashtag video present under']
# newdata = data.to_csv('./aggregated_scrapes_byhashtag/MASTER METADATA BY HASHTAG/master.csv', index = False)

'''
data2 = pd.read_csv("./aggregated_scrapes_byhashtag/vapestagram/vapestagram_2-28.csv")
'''

list_vids = []
videoURL = []
numVids = 0
numDupes = 0
for video in range(len(data)):
    row = {}
    start = 0
    numVids += 1
    if data.loc[video, "webVideoUrl"] not in videoURL:
        videoURL.append(data.loc[video,"webVideoUrl"])
        for cell in range(len(data.columns)):
            row.update({start: data.iloc[video][start]})
            # if cell == 3:
                # row.update({start: datetime.datetime.fromtimestamp(data.iloc[video][start])})
            start += 1
        list_vids.append(row)
    else:
        URL = data.loc[video, "webVideoUrl"]
        origIndex = videoURL.index(URL)
        # list_vids[origIndex][44] = list_vids[origIndex][44] + ', ' + data.loc[video, 'Hashtag video present under']
        numDupes += 1
        continue

# Variability checker below, from one file to another
'''
numVidsSame = 0
for secVid in range(len(data2)):
    sameVid = data.loc[data["webVideoUrl"].str.contains(data2.loc[secVid, "webVideoUrl"], case=False)]
    if len(sameVid) > 0:
        numVidsSame += 1
    
    if any(data2.loc[secVid, "webVideoUrl"] in sublist for sublist in data):
        numVidsSame += 1

    for secVidIter in range(len(data)):
        if elemToFind in data.iloc[secVidIter][29]:
            numVidsSame += 1
            break


print("Number of videos that are the same: " + str(numVidsSame))

'''

newData = pd.DataFrame(list_vids)


# TODO
newData.to_csv(path + 'master_second_half_of_month.csv', index = False)
print("Number of videos in master dataset for master: " + str(len(list_vids)))


print('Number of dupes: ' + str(numDupes))
