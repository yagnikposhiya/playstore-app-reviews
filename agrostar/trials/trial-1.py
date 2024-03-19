"""
Author: Yagnik Poshiya
GitHub: @yagnikposhiya
"""

# import google_play_scrapper python3 module
import pandas as pd
import google_play_scraper
from google_play_scraper import Sort, reviews

# extract result and continuation token
result, continuation_token = reviews(
    'com.ulink.agrostar',
    lang='en',
    country='us',
    sort=Sort.NEWEST,
    count=500
)

# extract results
result, _ = reviews(
    'com.ulink.agrostar',
    continuation_token=continuation_token
)

print(result) # print results
# print('\nType of result variable: ',type(result)) # print type result
# print(result[0]) # print first element of result
# print('\nType first element of result variable: ',type(result[0])) # print type of first element of result

dataframe = pd.DataFrame(result)
# csv_file_path = '/home/yagnikposhiya/WorkStation/Lab/Playstore-App-Reviews/trial-1.csv'
excel_file_path = '/home/yagnikposhiya/WorkStation/Lab/Playstore-App-Reviews/AS001042013.xlsx' # agrostar ID: AS001042013
# dataframe.to_csv(csv_file_path, index=False)
dataframe.to_excel(excel_file_path, index=False)
print('Dataframe save to CSV successfully')
print('\nTotal number of reviews: {a}'.format(a=len(result)))