from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('svc.sav')

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        CreditScore = int(request.form['CreditScore'])
        Geography = request.form['Geography']
        if Geography == 'France':
            Geography = 1
        elif Geography == 'Germany':
            Geography = 2
        elif Geography == 'Spain':
            Geography = 3
        Gender = request.form['Gender']
        if Gender == 'Male':
            Gender = 1
        elif Gender == 'Female':
            Gender = 2
        Age = int(request.form['Age'])
        Tenure = int(request.form['Tenure'])
        Balance = float(request.form['Balance'])
        NumOfProducts = int(request.form['NumOfProducts'])
        HasCrCard = int(request.form['HasCrCard'])
        IsActiveMember = int(request.form['IsActiveMember'])
        EstimatedSalary = float(request.form['EstimatedSalary'])
        prediction = model.predict([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,
                                     IsActiveMember,EstimatedSalary]])
        result = ""
        if prediction == 1:
            result = "The customer will leave the bank."
        else:
            result = "The customer will not leave the bank."

        return render_template('index.html', prediction_text=result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
