# Code by Ben Pretzer
# This is a script to create a master dataset of all the hashtags

import glob
import os
import pandas as pd


os.chdir('./aggregated_scrapes_byhashtag/second half/')
filenames = [i for i in glob.glob("*.csv")]
hashtag = filenames[0].split('_')[0]
combined = pd.concat([pd.read_csv(f) for f in filenames])
combined.to_csv("master_second_half_of_month.csv", index = False)
