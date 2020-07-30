from flask import Flask, request, jsonify
import os
import pandas as pd
import numpy as np
import pickle


app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

pickle_in_car = open('used_car_model.pkl', 'rb')
rf = pickle.load(pickle_in_car)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/predict-car', methods=['POST'])
def predict_used_car():

    car = request.get_json(silent=True)
    brand = car['brand']
    model = car['model']
    transmission = car['transmission']
    seats = car['seats']
    age = car['age']
    location = car['location']
    kilometers = car['kilometers']
    power = car['power']
    engine = car['engine']
    model = 'Model_'+model
    brand = 'Brand_'+brand
    transmission = 'Transmission_'+transmission
    location = 'Location_'+location
    inp = {'Kilometers_Driven': 0,
           'Engine': 0,
           'Power': 0,
           'Seats': 0,
           'Age': 0,
           'Location_Ahmedabad': 0,
           'Location_Bangalore': 0,
           'Location_Chennai': 0,
           'Location_Coimbatore': 0,
           'Location_Delhi': 0,
           'Location_Hyderabad': 0,
           'Location_Jaipur': 0,
           'Location_Kochi': 1,
           'Location_Kolkata': 0,
           'Location_Mumbai': 0,
           'Location_Pune': 0,
           'Fuel_Type_CNG': 0,
           'Fuel_Type_Diesel': 0,
           'Fuel_Type_LPG': 0,
           'Fuel_Type_Petrol': 0,
           'Owner_Type_First': 0,
           'Owner_Type_Second': 0,
           'Owner_Type_Third': 0,
           'Brand_Ambassador': 0,
           'Brand_Audi': 0,
           'Brand_BMW': 0,
           'Brand_Bentley': 0,
           'Brand_Chevrolet': 0,
           'Brand_Datsun': 0,
           'Brand_Fiat': 0,
           'Brand_Force': 0,
           'Brand_Ford': 0,
           'Brand_Honda': 0,
           'Brand_Hyundai': 0,
           'Brand_Isuzu': 0,
           'Brand_Jaguar': 0,
           'Brand_Jeep': 0,
           'Brand_Lamborghini': 0,
           'Brand_Land-Rover': 0,
           'Brand_Mahindra': 0,
           'Brand_Maruti': 1,
           'Brand_Mercedes-Benz': 0,
           'Brand_Mini': 0,
           'Brand_Mitsubishi': 0,
           'Brand_Nissan': 0,
           'Brand_Porsche': 0,
           'Brand_Renault': 0,
           'Brand_Skoda': 0,
           'Brand_Smart': 0,
           'Brand_Tata': 0,
           'Brand_Toyota': 0,
           'Brand_Volkswagen': 0,
           'Brand_Volvo': 0,
           'Model_1-Series': 0,
           'Model_1000': 0,
           'Model_3-Series': 0,
           'Model_5-Series': 0,
           'Model_6-Series': 0,
           'Model_7-Series': 0,
           'Model_800': 0,
           'Model_A-Class': 0,
           'Model_A-Star': 0,
           'Model_A3': 0,
           'Model_A4': 0,
           'Model_A6': 0,
           'Model_A7': 0,
           'Model_A8': 0,
           'Model_Accent': 0,
           'Model_Accord': 0,
           'Model_Alto': 0,
           'Model_Amaze': 0,
           'Model_Ameo': 0,
           'Model_Aspire': 0,
           'Model_Aveo': 0,
           'Model_Avventura': 0,
           'Model_B-Class': 0,
           'Model_BR-V': 0,
           'Model_Baleno': 0,
           'Model_Beat': 0,
           'Model_Beetle': 0,
           'Model_Bolero': 0,
           'Model_Bolt': 0,
           'Model_Boxster': 0,
           'Model_Brio': 0,
           'Model_C-Class': 0,
           'Model_CLA': 0,
           'Model_CLS-Class': 0,
           'Model_CR-V': 0,
           'Model_Camry': 0,
           'Model_Captiva': 0,
           'Model_Captur': 0,
           'Model_Cayenne': 0,
           'Model_Cayman': 0,
           'Model_Cedia': 0,
           'Model_Celerio': 0,
           'Model_Ciaz': 0,
           'Model_City': 0,
           'Model_Civic': 0,
           'Model_Classic': 0,
           'Model_Clubman': 0,
           'Model_Compass': 0,
           'Model_Continental': 0,
           'Model_Cooper': 0,
           'Model_Corolla': 0,
           'Model_Countryman': 0,
           'Model_Creta': 0,
           'Model_CrossPolo': 0,
           'Model_Cruze': 0,
           'Model_D-MAX': 0,
           'Model_Discovery': 0,
           'Model_Duster': 0,
           'Model_Dzire': 0,
           'Model_E-Class': 0,
           'Model_EON': 0,
           'Model_EcoSport': 0,
           'Model_Ecosport': 0,
           'Model_Eeco': 0,
           'Model_Elantra': 0,
           'Model_Elite-i20': 0,
           'Model_Endeavour': 0,
           'Model_Enjoy': 0,
           'Model_Ertiga': 0,
           'Model_Esteem': 0,
           'Model_Estilo': 0,
           'Model_Etios': 0,
           'Model_Evalia': 0,
           'Model_F-Type': 0,
           'Model_Fabia': 0,
           'Model_Fiesta': 0,
           'Model_Figo': 0,
           'Model_Fluence': 0,
           'Model_Fortuner': 0,
           'Model_Fortwo': 0,
           'Model_Freelander': 0,
           'Model_Freestyle': 0,
           'Model_Fusion': 0,
           'Model_GL-Class': 0,
           'Model_GLA-Class': 0,
           'Model_GLC': 0,
           'Model_GLE': 0,
           'Model_GLS': 0,
           'Model_GO': 0,
           'Model_Gallardo': 0,
           'Model_Getz': 0,
           'Model_Grand-Vitara': 0,
           'Model_Grand-i10': 0,
           'Model_Grande': 0,
           'Model_Hexa': 0,
           'Model_Ignis': 0,
           'Model_Ikon': 0,
           'Model_Indica': 0,
           'Model_Indica-Vista': 0,
           'Model_Indigo': 0,
           'Model_Innova': 0,
           'Model_Innova-Crysta': 0,
           'Model_Jazz': 0,
           'Model_Jeep': 0,
           'Model_Jetta': 0,
           'Model_KUV': 0,
           'Model_KWID': 0,
           'Model_Koleos': 0,
           'Model_Lancer': 0,
           'Model_Laura': 0,
           'Model_Linea': 0,
           'Model_Lodgy': 0,
           'Model_Logan': 0,
           'Model_M-Class': 0,
           'Model_MUX': 0,
           'Model_Manza': 0,
           'Model_Micra': 0,
           'Model_Mobilio': 0,
           'Model_Montero': 0,
           'Model_Mustang': 0,
           'Model_Nano': 0,
           'Model_Nexon': 0,
           'Model_NuvoSport': 0,
           'Model_Octavia': 0,
           'Model_Omni': 0,
           'Model_One': 0,
           'Model_Optra': 0,
           'Model_Outlander': 0,
           'Model_Pajero': 0,
           'Model_Panamera': 0,
           'Model_Passat': 0,
           'Model_Petra': 0,
           'Model_Platinum': 0,
           'Model_Polo': 0,
           'Model_Pulse': 0,
           'Model_Punto': 0,
           'Model_Q3': 0,
           'Model_Q5': 0,
           'Model_Q7': 0,
           'Model_Qualis': 0,
           'Model_Quanto': 0,
           'Model_R-Class': 0,
           'Model_RS5': 0,
           'Model_Range-Rover': 0,
           'Model_Rapid': 0,
           'Model_Renault': 0,
           'Model_Ritz': 0,
           'Model_S-Class': 0,
           'Model_S-Cross': 0,
           'Model_S60': 0,
           'Model_S80': 0,
           'Model_SL-Class': 0,
           'Model_SLC': 0,
           'Model_SLK-Class': 0,
           'Model_SX4': 0,
           'Model_Safari': 0,
           'Model_Sail': 0,
           'Model_Santa': 0,
           'Model_Santro': 0,
           'Model_Scala': 0,
           'Model_Scorpio': 0,
           'Model_Siena': 0,
           'Model_Sonata': 0,
           'Model_Spark': 0,
           'Model_Ssangyong': 0,
           'Model_Sumo': 0,
           'Model_Sunny': 0,
           'Model_Superb': 0,
           'Model_Swift': 0,
           'Model_TT': 0,
           'Model_TUV': 0,
           'Model_Tavera': 0,
           'Model_Teana': 0,
           'Model_Terrano': 0,
           'Model_Thar': 0,
           'Model_Tiago': 0,
           'Model_Tigor': 0,
           'Model_Tiguan': 0,
           'Model_Tucson': 0,
           'Model_V40': 0,
           'Model_Vento': 0,
           'Model_Venture': 0,
           'Model_Verito': 0,
           'Model_Verna': 0,
           'Model_Versa': 0,
           'Model_Vitara': 0,
           'Model_WR-V': 0,
           'Model_Wagon-R': 0,
           'Model_X-Trail': 0,
           'Model_X1': 0,
           'Model_X3': 0,
           'Model_X5': 0,
           'Model_X6': 0,
           'Model_XC60': 0,
           'Model_XC90': 0,
           'Model_XE': 0,
           'Model_XF': 0,
           'Model_XJ': 0,
           'Model_XUV300': 0,
           'Model_XUV500': 0,
           'Model_Xcent': 0,
           'Model_Xenon': 0,
           'Model_Xylo': 0,
           'Model_Yeti': 0,
           'Model_Z4': 0,
           'Model_Zen': 0,
           'Model_Zest': 0,
           'Model_i10': 0,
           'Model_i20': 0,
           'Model_redi-GO': 0,
           'Transmission_Automatic': 0,
           'Transmission_Manual': 0}

    inp['Engine'] = engine
    inp['Power'] = power
    inp['Age'] = age
    inp['Seats'] = seats
    inp['Kilometers_Driven'] = kilometers
    inp[transmission] = 1
    inp[brand] = 1
    inp[model] = 1
    inp[location] = 1
    inp_ser = pd.Series(inp)
    prediction = rf.predict([inp_ser])
    return {
        "prediction": prediction[0]
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
