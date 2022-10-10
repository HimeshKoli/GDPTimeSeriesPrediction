import pandas as pd
import requests

import warnings

warnings.filterwarnings('ignore')


# df_main = pd.DataFrame(columns=['Financial_year', 'GDP_in_rs_cr', 'GDP_growth_rate_yoy'])

# we first set up our api call to get data

def get_data():
    api_key = '579b464db66ec23bdd000001023b005613b940c9705454ff030f9881'
    url = 'https://api.data.gov.in/resource/07d49df4-233f-4898-92db-e6855d4dd94c?api-key=' + api_key + '&format=json&limit=70'

    response = requests.get(url).json()

    all_data = []

    for item in response['records']:
        data = {'Financial_year': item['financial_year'],
                'GDP_in_rs_cr': item['gross_domestic_product_in_rs_cr_at_2004_05_prices'],
                'GDP_growth_rate_yoy': item['gross_domestic_product___growth_rate_yoy_']
                }
        # print(Financial_year)
        # print(GDP_in_rs_cr)
        # print(GDP_growth_rate_yoy)

        all_data.append(data)
    # print(df.head().to_markdown())
    # quit()
    return pd.DataFrame(all_data)


gdp_df = get_data()
# print(gdp_df)
