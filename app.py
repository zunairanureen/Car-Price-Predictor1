from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the dataset
car = pd.read_csv("C:\\Users\\Ihtsham Mehmood\\Documents\\Downloads\\car price predictor\\Cleaned Car.csv")

# Load the model (ensure you have the model pickle file)
with open('C:\\Users\\Ihtsham Mehmood\\Documents\\Downloads\\car price predictor\\LinearRegressionmodel.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    # Prepare data for the dropdowns
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = sorted(car['fuel_type'].unique())
    
    # Render the main page
    return render_template('index.html', companies=companies, car_models=car_models, year=year, fuel_type=fuel_type)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form inputs
    company = request.form['company']
    model_name = request.form['car_model']
    year = int(request.form['year'])
    fuel_type = request.form['fuel_type']
    kms_driven = int(request.form['kms_driven'])  # Get kms_driven from the form

    # Prepare the input data for prediction
    input_data = pd.DataFrame({
        'company': [company],
        'name': [model_name],
        'year': [year],
        'fuel_type': [fuel_type],
        'kms_driven': [kms_driven]  # Include kms_driven in the input
    })

    # Predict the price using the model
    prediction = model.predict(input_data)
    
    # Return the result
    return render_template('index.html', 
                           companies=sorted(car['company'].unique()), 
                           car_models=sorted(car['name'].unique()), 
                           year=sorted(car['year'].unique(), reverse=True), 
                           fuel_type=sorted(car['fuel_type'].unique()), 
                           predicted_price=f'Predicted Price: ${prediction[0]:,.2f}')


if __name__ == "__main__":
    app.run(debug=True)
