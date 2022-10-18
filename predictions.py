import datetime
import pickle
from datetime import date

from statsmodels.tsa.arima.model import ARIMA

from preprocessing_data import preprocessed_gdp_df


# line17>> passed argument in date format because index is financial_year which is in date format
# line20>> start and end takes range so starting from len(preprocessed_gdp_df) i.e: 62 which coordinates to that year
# in Financial_year, and it takes that value from index till end=year which will be given at the end of choice
# line23&24>> create new .pkl file and load data in that file
# line26>> at the end, will get range between start and end, but need only last value in that series range, so
# slicing it to [-1] to get end value

def predictions(year: date):
    model = ARIMA(preprocessed_gdp_df['GDP_in_rs_cr'], order=(1, 2, 1))
    result = model.fit()
    result.predict(start=len(preprocessed_gdp_df), end=year, typ='levels').rename('ARIMA predictions')
    # return float("{:.2f}".format(pred[-1]))

    pickle.dump(result, open('arima_model.pkl', 'wb'))
    pickled_model = pickle.load(open('arima_model.pkl', 'rb'))

    return pickled_model.predict(start=len(preprocessed_gdp_df), end=year, typ='levels').apply(lambda x: round(x, 2))[-1]


# This below function bracket is designed to work to get a range on user input, so since I have already implemented one
# type where user gets prediction for a desire year instead whole range over years I will do this implementation in some time

# def predictions_step(step):
#     model = ARIMA(preprocessed_gdp_df['GDP_in_rs_cr'], order=(1, 2, 1))
#     result = model.fit()
#     result.predict(start=len(preprocessed_gdp_df), end=len(preprocessed_gdp_df) + (step - 1), typ='levels')
#
#     pickle.dump(result, open('arima_model_step.pkl', 'wb'))
#     pickled_model = pickle.load(open('arima_model_step.pkl', 'rb'))
#
#     return pickled_model.predict(start=len(preprocessed_gdp_df), end=len(preprocessed_gdp_df)+(step-1), typ='levels')

# the reason it is passed like this is that the argument taken is in datetime format
x = datetime.datetime(2020, 1, 1)
print(predictions(x))

# print(predictions_step(15))
