"""
Author: Yagnik Poshiya
GitHub: @yagnikposhiya
"""

# import google_play_scrapper python3 module
import pandas as pd
import google_play_scraper
from google_play_scraper import Sort, reviews_all

result = reviews_all(
    'com.ulink.agrostar',
    sleep_milliseconds=1000, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
)

print(result)
dataframe = pd.DataFrame(result)
# csv_file_path = '/home/yagnikposhiya/WorkStation/Lab/Playstore-App-Reviews/trial-1.csv'
excel_file_path = '/home/yagnikposhiya/WorkStation/Lab/Playstore-App-Reviews/AS001042013-4.xlsx' # agrostar ID: AS001042013
# dataframe.to_csv(csv_file_path, index=False)
dataframe.to_excel(excel_file_path, index=False)
print('Dataframe save to CSV successfully')
print('\nTotal number of reviews: {a}'.format(a=len(result)))