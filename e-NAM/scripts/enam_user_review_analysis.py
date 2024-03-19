"""
Author: Yagnik Poshiya
GitHub: @yagnikposhiya
"""

# import required python modules
import pandas as pd

user_review_data_file_path = '/home/yagnikposhiya/WorkStation/Lab/playstore-app-reviews/e-NAM/data/enm-reviews.xlsx' # set user review data file path
dataframe = pd.read_excel(user_review_data_file_path) # load user review data into pandas dataframe

print(dataframe.head(5)) # loaded data for verification
print('- Type of dataframe contains raw data: {}'.format(type(dataframe))) # type of dataframe

def clean_data(df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    '''
    This function is used to clean user review data
    1. Remove rows with missing values (NaN) in 'content' column

    Parameters:
    - df (pd.core.frame.DataFrame): User Review DataFrame

    Returns:
    - pd.core.frame.DatafFrame: clean dataframe
    '''

    print('- Length of dataframe before cleaning: {}'.format(len(df))) # length of df before cleaning
    column_name_content = 'content' # set column name

    if column_name_content in df:
        total_empty_cells = df[column_name_content].isna().sum()
        print('- Total number of reviews do not contain any content: {}'.format(total_empty_cells))

        if total_empty_cells: # if total number of empty cells are non-zero
            df = df[df[column_name_content].notna() & (df[column_name_content] != '')] # remove rows with empty values in the 'column_name' column
    else:
        print('- Dataframe does not contain {} column'.format(column_name_content))
    
    print('- Length of dataframe after cleaning: {}'.format(len(df))) # length of df after cleaning
    return df


def extract_rows_score_5(df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    '''
    This function is used to extract rows for which 'score' column values are higher than threshold values.
    And sort newly extracted dataframe based on 'thumbsUpCount' column.

    Parameters:
    - df (pd.core.frame.DataFrame): DataFrame does not contain NaN value in 'content' column
    '''

    high_score_threshold = 5 # set threshold for 'score' column
    column_name_score = 'score' # set column name
    column_name_thumbsUpCount = 'thumbsUpCount' # set column name
    
    if column_name_score in df:
        high_score_rows = df[df[column_name_score] >= high_score_threshold]
        filtered_df = pd.DataFrame(high_score_rows) # create new dataframe after filtering

        filtered_df_sorted = filtered_df.sort_values(by=column_name_thumbsUpCount,ascending=False) # sort dataframe based on thumbsUpCount values
    else:
        print('- Dataframe does not contain {} column'.format(column_name_score))

    return filtered_df_sorted


def extract_rows_score_1(df:pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    '''
    This function is used to extract rows for which 'score' column values are lower than threshold values.
    And sort newly extracted dataframe based on 'thumbsUpCount' column.

    Parameters:
    - df (pd.core.frame.DataFrame): DataFrame does not contain NaN value in 'content' column
    '''

    low_score_threshold = 1 # set threshold for 'score' column
    column_name_score = 'score' # set column name
    column_name_thumbsUpCount = 'thumbsUpCount' # set column name
    
    if column_name_score in df:
        low_score_rows = df[df[column_name_score] <= low_score_threshold]
        filtered_df = pd.DataFrame(low_score_rows) # create new dataframe after filtering

        filtered_df_sorted = filtered_df.sort_values(by=column_name_thumbsUpCount,ascending=False) # sort dataframe based on thumbsUpCount values
    else:
        print('- Dataframe does not contain {} column'.format(column_name_score))

    return filtered_df_sorted


def dataframe_to_excel_file(df:pd.core.frame.DataFrame, filename:str) -> None:
    '''
    This function is used to save dataframe into Excel file

    Parameters:
    - df (pd.core.frame.DataFrame): dataframe that needs to be saved into the Excel file
    - filename (str): filename with which file will be stored 
    '''

    root_path = '/home/yagnikposhiya/WorkStation/Lab/playstore-app-reviews/e-NAM/data/filtered-data'
    excel_file_path = root_path + '/' + filename
    df.to_excel(excel_file_path, index=False) # saved dataframe into Excel file

    print('Dataframe is saved successfully!')




dataframe = clean_data(dataframe) # call clean_data() function & get clean dataframe

# filter data based on 5 score rating
extracted_5_score_rows = extract_rows_score_5(dataframe) # call extract_rows_score_5() function & get rows only for 5 score ratings and sort dataframe based on thumbUpCount
dataframe_to_excel_file(extracted_5_score_rows,'5_score_Max_thumbsUpCount.xlsx')

# filter data based on 1 score rating
extracted_1_score_rows = extract_rows_score_1(dataframe) # call extract_rows_score_5() function & get rows only for 5 score ratings and sort dataframe based on thumbUpCount
dataframe_to_excel_file(extracted_1_score_rows,'1_score_Min_thumbsUpCount.xlsx')
