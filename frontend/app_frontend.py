import os
import json
import requests
import streamlit as st

def app_info():
    st.title("App info")
    st.markdown("_Task - Water Potability prediction_")

    st.header("Brief description of the project")
    st.write(
        "The application is a simple frontend for the water potability prediction."
    )
    st.write(
        "This application sends data to the FastAPI backend and retrieves the prediction."
    )
    st.write(
        "This project showcases the use of multi app deployment scenario."
    )
    return

def get_prediction(dict_feats):
    # get the BACKEND_HOSTNAME from the env variable
    backend_hostname = os.getenv("BACKEND_HOSTNAME", "localhost:5000")

    # the endpoint of the post request
    url = f"http://{backend_hostname}/predict"

    headers = {"Content-type": "application/json"}
    # additional headers to indicate the content type of the post request

    result = requests.post(url, data=json.dumps(dict_feats), headers=headers)
    return result

def water_potability_frontend():
    st.title("Enter the following features required for water potability prediction")

    st.header("Features")
    st.write("Use blank or do not enter anything, for empty value for a feature")
    nan = float("nan")
    ph = st.number_input("ph", value=nan)
    Hardness = st.number_input("Hardness", value=nan)
    Solids = st.number_input("Solids", value=nan)
    Chloramines = st.number_input("Chloramines", value=nan)
    Sulfate = st.number_input("Sulfate", value=nan)
    Conductivity = st.number_input("Conductivity", value=nan)
    Organic_carbon = st.number_input("Organic_carbon", value=nan)
    Trihalomethanes = st.number_input("Trihalomethanes", value=nan)
    Turbidity = st.number_input("Turbidity", value=nan)

    dict_feats = {
        "ph" : ph,
        "Hardness" : Hardness,
        "Solids" : Solids,
        "Chloramines" : Chloramines,
        "Sulfate" : Sulfate,
        "Conductivity" : Conductivity,
        "Organic_carbon" : Organic_carbon,
        "Trihalomethanes" : Trihalomethanes,
        "Turbidity" : Turbidity,
    }

    st.write(dict_feats)

    get_pred_btn = st.button("Get prediction")
    if get_pred_btn:
        prediction = get_prediction(dict_feats)
        st.header("Water potability prediction")
        st.write(f"{json.loads(prediction.text)} \n")

    return

app_modes = {
    "App Info": app_info,
    "Water Potability Frontend App": water_potability_frontend,
}


def start_app():
    selected_mode = st.sidebar.selectbox("Select mode", list(app_modes.keys()))
    app_modes[selected_mode]()
    return


def main():
    start_app()
    return

if __name__ == "__main__":
    main()
