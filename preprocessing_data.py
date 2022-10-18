import pandas as pd

from fetching_data import gdp_df


# line11>> convert "1951-52" to 1951
# line12>> then convert 1951 to proper datetime format 1951-01-01 (yyyy-mm-dd)
# line15>> set Financial_year as index

def preprocessing(df):
    df['Financial_year'] = df['Financial_year'].apply(lambda x: str(x).split('-')[0])
    df['Financial_year'] = pd.to_datetime(df['Financial_year'])
    df['GDP_in_rs_cr'] = df['GDP_in_rs_cr'].astype('float64')
    df = df.drop(columns=['GDP_growth_rate_yoy'])
    df = df.set_index('Financial_year')

    return df


preprocessed_gdp_df = preprocessing(gdp_df)
# print(preprocessed_gdp_df)
