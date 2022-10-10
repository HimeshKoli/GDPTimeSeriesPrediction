# GDPTimeSeriesPrediction

## Basics of Time-Series Analysis:
In this project according to the data we gathered, the requirement for analysis was satisfied by ARIMA model which we 
got from "statsmodels" package.

ARIMA consists of 3 parts:

AR (Auto Regressive) - AR equation goes as follows
```
yt = c + ϕ(1)y(t − 1) + ϕ(2)y(t − 2) + ⋯ + ϕ(p)y(t − p) + εt
```
AR basically calculates previous lags.
So here t-1, t-2, etc. are lags, so how many lags we have to consider for AR that can be found by using 
PartialAutoCorrelation_Plot.

I (Integration) which is also known as differencing, is used to make data stationary, like when nature is increasing or 
decreasing trend, it is non-stationary, so differencing eliminates that trend and makes it stationary, although it depends 
on how many times it needs to be differentiated, max-2, basically we take 'I' at a point where data becomes stationary 
and to get AR and MA values we put differenced dataframe in acf and pacf plots.

MA (Moving Averages) - MA uses past errors to make future predictions, so how many errors we have to consider for MA that 
can be found by using AutoCorrelation_Plot.

## Workflow of our analysis:

1) First we fetch data using api key provided from government site and made a dataframe.
2) Then did preprocessing over our dataframe till we get our target feature which is ```GDP_in_rs_cr``` and index as 
```Financial_year``` as needed.
3) Using Augmented-Dickey Fuller test checked if our data is stationary or not.
4) If its not-stationary then we make it stationary by differencing it.
5) Compute AR and MA values using 'I',acf, pacf plots.
6) After that we test our model and get RMSE score, if gap between target feature's mean and RMSE is huge then model is 
good enough.
7) Now we fit ARIMA on whole dataset and start forecasting for future predictions.

## Software and tools requirement for end to end implementation:

1) [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)
2) [Heroku](https://www.heroku.com/)
3) [Docker](https://www.docker.com/)
4) [GitHub](https://github.com/)
5) [Git-CLI](https://git-scm.com/downloads)

## References:

1) [Government site to fetch data - data.gov.in](https://data.gov.in/)
2) [Time Series Bible - Forecasting: Principles and Practice](https://otexts.com/fpp2/)
