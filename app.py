import pickle

from flask import Flask, render_template, request

app = Flask(__name__)
port = 5000
arima_model = pickle.load(open('arima_model.pkl', 'rb'))


@app.get('/')
def home():
    return render_template('base.html')

# line24&25>> firstly made a mistake of "not passing user input in a variable" i.e: here 'year' in variable 'data', and this
# year is reflected in html page name="year" so to store this user input in data and also using request.get_data()which was not suited
# line25>> then corrected this storing mistake and actually form.get was better suited due to nature of the form in
# html page to get data, and then further didn't need to give datetime format
# line27&28>> output type is series, but needed list, so converted that into list
# line29>> in this list there is prediction as well as datatype and some as64 word i.e: 7.425678e+06, dtype:series, AS-64
# so from this need only prediction value, so gave [0] and to get value in float format limit to 2 decimal, so that code

@app.post('/predict')
def predict():
    # data = [datetime.datetime(x) for x in request.get_data()]
    data = request.form.get('year')
    output = arima_model.predict(data)
    # print(type(output))
    result = output.tolist()
    return render_template('base.html', predicted_gdp='The predicted GDP forecast for your choice of year is {} Rs'.format("{:.2f}".format(float(result[0]))))


# this below block of code will initiate the entire project

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
