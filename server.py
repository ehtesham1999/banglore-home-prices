from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    locations = util.get_location_names()
    return render_template('index.html',locationss=locations)


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    if request.method == 'POST':
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        output =  util.get_estimated_price(location,total_sqft,bhk,bath)

        return render_template('index.html', prediction_text="You Can Sell The House at {} Lakhs".format(output))
    else:
        return render_template('index.html', prediction_text="You Can Sell The House")

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
