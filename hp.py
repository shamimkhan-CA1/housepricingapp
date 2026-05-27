import streamlit as st
import pickle

## to load the model and label encoder
## we use run binary = rb with pickle

model = pickle.load(open("hp.pkl","rb"))

le = pickle.load(open("label_encoder.pkl","rb"))
le1 = pickle.load(open("label_encoder1.pkl","rb"))
le2 = pickle.load(open("label_encoder2.pkl","rb"))


st.title("House Price Prediction App")

## selection drop down, for Location ('Downtown', 'Rural', 'Suburban', 'Urban')
## selection drop down, for Condition ('Excellent', 'Fair', 'Good', 'Poor')
## selection drop down, for Garage ('No', 'Yes')

house_location = st.selectbox("select Location",le.classes_)
house_condition = st.selectbox("select Condition",le1.classes_)
house_with_garage = st.selectbox("Whether garage",le2.classes_)

# user inputs

area = st.number_input("Enter area (in sq. foots)", min_value=501, max_value=4999)
year_built = st.number_input("Enter year_built", min_value=1900, max_value=2023)
floors = st.slider("floors (numbers)",1,3)
Bedrooms = st.slider("Bedrooms (numbers)",1,5)
Bathrooms = st.slider("Bathrooms (numbers)",1,4)

encoded_model = le.transform([house_location])[0]
encoded_model1 = le1.transform([house_condition])[0]
encoded_model2 = le2.transform([house_with_garage])[0]

if st.button("Predict Price"):
    input_data = [[encoded_model,encoded_model1,encoded_model2,area,year_built,floors,Bedrooms,Bathrooms]]
    predicted_price = model.predict(input_data)
    st.success(f"Estimated Selling Price: {predicted_price[0]}")