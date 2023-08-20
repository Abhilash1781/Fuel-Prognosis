import numpy as np
import pickle as pk
import streamlit as st
import base64



# Load the trained model and scaled data
loaded_model = pk.load(open("XGBOOST.sav","rb"))
scaled_data = pk.load(open("scale.sav","rb"))



@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Set background image using HTML style
image_url = "https://github.com/Abhilash1781/Fuel-Prognosis/blob/main/Images/Deployment.png?raw=true"
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("{image_url}");
background-size: 100%;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# Function to convert input values
def input_converter(inp):
    vcl = ['Two-seater', 'Minicompact', 'Compact', 'Subcompact', 'Mid-size', 'Full-size', 'SUV: Small', 'SUV: Standard', 'Minivan', 'Station wagon: Small', 'Station wagon: Mid-size', 'Pickup truck: Small', 'Special purpose vehicle', 'Pickup truck: Standard']
    trans = ['AV','AM','M','AS','A']
    fuel = ["D", "E", "X", "Z"]
    lst = []
    for i in range(6):
        if (type(inp[i]) == str):
            if (inp[i] in vcl):
                lst.append(vcl.index(inp[i]))
            elif (inp[i] in trans):
                lst.append(trans.index(inp[i]))
            elif (inp[i] in fuel):
                if (fuel.index(inp[i]) == 0):
                    lst.extend([1, 0, 0, 0])
                    break
                elif (fuel.index(inp[i]) == 1):
                    lst.extend([0, 1, 0, 0])
                    break
                elif (fuel.index(inp[i]) == 2):
                    lst.extend([0, 0, 1, 0])
                    break
                elif (fuel.index(inp[i]) == 3):
                    lst.extend([0, 0, 0, 1])
        else:
            lst.append(inp[i])

    arr = np.asarray(lst)
    arr = arr.reshape(1, -1)
    arr = scaled_data.transform(arr)
    prediction = loaded_model.predict(arr)

    return (f"The Fuel Consumption (L/100km) is {prediction[0]:.2f}")


# Streamlit main function
def main():
    st.markdown("<h1 style='text-align: center; color: white;'>Fuel Consumption Prediction</h1>", unsafe_allow_html=True)           
    result = 0
    label_font_size = "28px"

    # List of vehicle classes, transmission types, and fuel types
    vehicle = ['Two-seater','Minicompact','Compact','Subcompact','Mid-size','Full-size','SUV: Small','SUV: Standard','Minivan','Station wagon: Small','Station wagon: Mid-size','Pickup truck: Small','Special purpose vehicle','Pickup truck: Standard']
    transmission = ['A','AM','AS','AV','M']
    fuel = ["D", "E", "X", "Z"]
    
    
    def insert_line_breaks(num_breaks=1):
      for _ in range(num_breaks):
        st.markdown("<br>", unsafe_allow_html=True)


    Vehicle_class_label = f"<h2 style='font-size: {label_font_size};'>Enter Vehicle class</h2>"
    st.markdown(Vehicle_class_label, unsafe_allow_html=True)
    Vehicle_class = st.selectbox("", options=vehicle)

    insert_line_breaks(num_breaks=3)

    Engine_size_label = f"<h3 style='font-size: {label_font_size};'>Select Engine Size (Enter value in this range [1-7])</h3>"
    st.markdown(Engine_size_label, unsafe_allow_html=True)
    Engine_size = st.selectbox("", options=[1, 2, 3, 4, 5, 6, 7])

    insert_line_breaks(num_breaks=3)

    Cylinders_label = f"<h3 style='font-size: {label_font_size};'>Enter number of Cylinders (Enter value in this range [1-16])</h3>"
    st.markdown(Cylinders_label, unsafe_allow_html=True)
    Cylinders = st.number_input("", min_value=1, max_value=16)

    insert_line_breaks(num_breaks=3)
    

    Transmission_label = f"<h3 style='font-size: {label_font_size};'>Select the Transmission</h3>"
    st.markdown(Transmission_label, unsafe_allow_html=True)
    Transmission_class = st.selectbox("", transmission)

    insert_line_breaks(num_breaks=3)

    Co2_Rating_label = f"<h3 style='font-size: {label_font_size};'>Enter CO2 Rating (Enter value in this range [1-10])</h3>"
    st.markdown(Co2_Rating_label, unsafe_allow_html=True)
    Co2_Rating = st.number_input("", min_value=1, max_value=10)

    insert_line_breaks(num_breaks=3)

    Fuel_type_label = f"<h3 style='font-size: {label_font_size};'>Select the Fuel type</h3>"
    st.markdown(Fuel_type_label, unsafe_allow_html=True)
    Fuel_type = st.selectbox("", fuel)


    if st.button("Predict"):
        result = input_converter([Vehicle_class,Engine_size,Cylinders,Transmission_class,Co2_Rating,Fuel_type])
        markdown_text = f"<h2 style='color:white;'><b>{result}</b></h2>"
        st.markdown(markdown_text, unsafe_allow_html=True)



if __name__ == "__main__":
    main()
