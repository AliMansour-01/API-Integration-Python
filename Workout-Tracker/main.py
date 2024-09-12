import requests
from datetime import datetime

GENDER = "Male"
Weight_KG = "7"
HEIGHT_CM = "188"
AGE = "21"

APP_ID = "--" #Enter your APP_ID
API_key = "--" #Enter your API key

exersice_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "--" #your sheety endpoint
exercise_text = input("Enter exercise that you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_key
}

endpoint_config = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": Weight_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exersice_endpoint, json=endpoint_config, headers=headers)
result = response.json()


today = datetime.now().strftime('%m/%d/%Y')
current_time = datetime.now().strftime('%X')

for exercise in result["exercises"]:
    excel_inputs = {
        "workout": {
            "date": today,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=excel_inputs)

    print(sheet_response.text)



