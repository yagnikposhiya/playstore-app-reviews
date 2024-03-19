"""
Author: Yagnik Poshiya
GitHub: @yagnikposhiya
"""

# import required python modules
import pandas as pd # for generate dataframe from the scrapped list
import google_play_scraper
from google_play_scraper import reviews_all, Sort # for scrapping user review list

application_id = 'com.BigHaat' # set application ID
language = 'en' # set language
country = 'us' # set country
milliseconds = 5000 # set milliseconds

dataframe = pd.DataFrame() # create global dataframe
loop_continuation = True # set loop continuation
count = 0 # set count variable for while loop iterations

while(loop_continuation):
    result = reviews_all(
    application_id,
    sleep_milliseconds=milliseconds,
    lang=language,
    country=country,
    sort=Sort.MOST_RELEVANT
    ) # scrap reviews from the google play

    dataframe_local = pd.DataFrame(result) # create local dataframe

    if dataframe_local.empty:
        print('Local dataframe is empty')
    else:
        dataframe = dataframe.append(dataframe_local,ignore_index=True) # append local dataframe to global dataframe
        dataframe = dataframe.drop_duplicates(subset=['reviewId','userName'])
        count = count + 1
        print('Iteration: {}'.format(count))

    if count >= 20:
        print('Exiting loop.')
        break

# set excel file path
excel_file_path = '/home/yagnikposhiya/WorkStation/Lab/playstore-app-reviews/bighaat/reviews/bighaat_reviews_1.xlsx'
dataframe.to_excel(excel_file_path,index=False)
print('Dataframe is saved successfully!')
print('\nTotal number of reviews: {a}'.format(a=dataframe.shape[0]))


    



