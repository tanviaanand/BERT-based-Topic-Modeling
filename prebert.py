# Code by Ben Pretzer
# This script goes through the TikTok descriptions and removes keywords based on whether or not they are present
# in the list in the script. 

import pandas as pd
import wordninja
import enchant
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

master = pd.read_csv('./bertopic/BERTdesc.csv')
eng_d = enchant.Dict('en_US')
column_names = ['description', 'old description']
new_DF = pd.DataFrame(columns=column_names)

remove_keywords = ['#', '@', '!', 'nicotinepouch', 'vape', 'vapecommunity', 'vapefam', 'vapelife', 'vapelyfe', 'vapenation', 
'vapeon', 'vapeporn', 'vaper', 'vapestagram', 'vapetricks', 'vaping', 'fyp', '?', '.', 'I', "'", 'foryourpage',
'foryou', 'Reply', 'Vapor', 'foryoupage', 'fy', ',', 'xyzbca', ':', 'Marinar', 'ViataDeNavigato', 'perte',
'parati', 'tiktok', 'Răspunde', 'рек', 'schweinfurt', 'хочуврек', 'рекомендации', 
'4u', 'foru', 'fürdich', 'вейп', 'growupwithme', 'trucos', 'What', 'featureme', '&', '(', ')', '|', 'pourtoi', 'viatadenavigator',
'😂', '’', 'X', '1', 'lang', '👌🏼', 'TheOriginal', 'A', '😅', '😍', '-', '//', 'zxycba', 'guys', 'lol', 'The', '3', '2', 'follow',
'spam', 'This', 'My', '❤️', 'see', '😎', 'New', 'You', '🤣', 'tik_tok', 'followme', '“', 'x', 'O', 'Just', 'FYP', 'How', 'good', 'let',
'”', '🤔', 'Do', 'uae', 'f', '*', 'nike', '￼', 'keşfet', 'lentejas', 'WereAllMad', 'onevibeph', 'Follow', '<', '+', 'cool', 'THE', 'when', 
'4', 'antworten', '``', 'No', 'și', 'Répondre', '🥰', '😁', 'things', 'When', 'BadBitch', 'whole', 'transitions', 'chill', 'Love', 'NavigatorRoman',
'vibe', 'FeatureMe', 'nus', 'jus', 'FY', 'ape', 'on', 'de', 'at', 'sorry', 'over', 'topic', 'could', 'is', 'this', 'ask', 'he', 'his', 'for', 'page', 'as',
'is', 'on', 'tacos', 'per', 'through', 'my', 'corvette', 'over', 'you', 'de', 'ha?', 'your', 'with', 'love', 'to?', 'yours', 
'in', 'de', 'it', 'ti', 'ha', 'ti?', 'huh', 'huh?', 'such', 'them', 'Them', 'nu', 'ta', 'para']

for video in range(len(master)):
    sentence = master.loc[video, 'text']
    new_desc = ''
    text_tokens = word_tokenize(sentence)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    for token in tokens_without_sw:
        if eng_d.check(token) == False:
            splitword = wordninja.split(token)
            for word in splitword:
                num_letters = len(word)
                if (eng_d.check(word) == True) and (num_letters > 1) and not str(word).isdigit():
                    if word not in remove_keywords:
                        new_desc = new_desc + word + ' '
        elif token not in remove_keywords and not str(token).isdigit():
            if not token.replace('.', '').replace('-', '').isdigit():
                new_desc = new_desc + token + ' '
    new_DF.loc[len(new_DF.index)] = [new_desc, sentence]



'''
desc = master.loc[:,'text']

newDesc = desc.to_csv('BERTdesc.csv', index=False)
'''

newDesc = new_DF.to_csv('BERTdesc_cleaned.csv', index=False)
