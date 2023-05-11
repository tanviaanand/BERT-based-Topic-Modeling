# Code by Ben Pretzer
# This is the main modeling script, I have the running of the model itself commented out but in those 
# comments (line 46) is where you would change number of topics, use different models, etc
# Also contains a class to run the coherence tests on different amount of BERTopic topic #'s



from bertopic import BERTopic
import pandas as pd
from matplotlib import pyplot as plt
from flair.embeddings import TransformerDocumentEmbeddings
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

'''
topic_model = BERTopic(verbose=True, calculate_probabilities=True)
topics, probabilities = topic_model.fit_transform(docs)
info = topic_model.get_topic_info()

info.to_csv("all-topics.csv", index=False)

head = topic_model.get_topic_freq().head(8)

for i in range(20):
    topic = topic_model.get_topic(i)
    df = pd.DataFrame(topic)
    df.to_csv('./BERTopic_topics_removedSW/Topic_' + str(i+1) + '.csv', index=False, header = ['word', 'c-TF-IDF score'])


all_topics = topic_model.visualize_topics()
all_topics.show()

bar = topic_model.visualize_barchart()
bar.show()

heatmap = topic_model.visualize_heatmap()
heatmap.show()

'''

'''
bert_base = TransformerDocumentEmbeddings('bert-base-uncased')
'''

'''
topic_model = BERTopic(language = 'english', nr_topics = 25)
topics, probabilities = topic_model.fit_transform(docs)
params = topic_model.get_params()
topic_model.save('./bert-base-25')
'''

class BT:
    def runBert(self):
        desc = pd.read_csv('./BERTdesc_cleaned.csv', usecols=['description'])
        docs = desc['description'].tolist()
        topic_model = BERTopic.load('./bert-base-25')
        topics = topic_model.fit_transform(docs)
        vectorizer = topic_model.vectorizer_model
        tokenizer = vectorizer.build_tokenizer()
        # Extract features for Topic Coherence evaluation
        words = vectorizer.get_feature_names()
        tokens = [tokenizer(doc) for doc in docs]
        dictionary = corpora.Dictionary(tokens)
        corpus = [dictionary.doc2bow(token) for token in tokens]
        topic_words = [[words for words, _ in topic_model.get_topic(topic)] for topic in range(len(set(topics))-1)]
        # Evaluate
        coherence_model = CoherenceModel(topics=topic_words,
                                         texts=tokens,
                                         corpus=corpus,
                                         dictionary=dictionary,
                                         coherence='c_v')
        coherence = coherence_model.get_coherence()
        return coherence


'''
# For loop for getting coherence score and plotting out coherence values in increments of 5

'''
'''
info = topic_model.get_topic_info()

info.to_csv('25 topics (bert-base).csv', index = False)

bar2 = topic_model.visualize_barchart()
bar2.show()


hye = topic_model.visualize_hierarchy()
hye.show()


probs = topic_model.visualize_distribution(probabilities[0])
probs.show()
'''


