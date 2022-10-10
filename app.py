import pickle

from flask import Flask, render_template, request

app = Flask(__name__)
arima_model = pickle.load(open('arima_model.pkl', 'rb'))


@app.get('/')
def home():
    return render_template('base.html')


# line23>> first we made a mistake of "not passing user input in a variable" i.e: here 'year' in variable 'data', and this
# year is reflected in html page name="year" so we can store this user input in data
# line24>> then we corrected this storing mistake and actually form.get was better suited due to nature of our form in
# html page to get data, and then we didn't need to give datetime format
# line26&27>> our output type is series, but we need list, so we converted that into list
# line28>> so in this list there is our prediction as well as datatype and some as64 word i.e: 7.425678e+06, dtype:series, AS-64
# so from this we need only value, so we give [0] and in float format that to limit to 2 decimal so that code

@app.post('/predict')
def predict():
    # data = [datetime.datetime(x) for x in request.get_data()]
    data = request.form.get('year')
    output = arima_model.predict(data)
    # print(type(output))
    result = output.tolist()
    return render_template('base.html', predicted_gdp='The predicted forecast for your year is {}'.format(
        "{:.2f}".format(float(result[0]))))


# this will initiate our code, below block

if __name__ == "__main__":
    app.run(debug=True)
