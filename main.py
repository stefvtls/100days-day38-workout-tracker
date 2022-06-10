from dotenv import load_dotenv
import os
import requests
import datetime as dt


load_dotenv()
today = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%H:%M:%S")
NUTRITION_API = os.getenv("NUTRITION_API")
NUTRITION_ID = os.getenv("NUTRITION_ID")
NUTRITION_KEY = os.getenv("NUTRITION_KEY")

exercises = input("what exercises did you do?")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
EXERCISE_HEADERS = {"x-app-id": NUTRITION_ID, "x-app-key": NUTRITION_KEY}
EXERCISE_JSON = {
 "query": exercises,
 "gender": "male",
 "weight_kg": 70.5,
 "height_cm": 170,
 "age": 28
}

response_nutrition = requests.post(url=EXERCISE_ENDPOINT, headers=EXERCISE_HEADERS, json=EXERCISE_JSON)
response_nutrition.raise_for_status()
results = response_nutrition.json()


SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/workoutPlan/records"
SHEETY_HEADERS = {"Content-Type": "application/json"}
AUTH_USERNAME = os.getenv("AUTH_USERNAME38")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD38")
BEARER_TOKEN = os.getenv("BEARER_TOKEN38")
for x in range(0, len(results['exercises'])):
    SHEETY_JSON = {
        "record": {
            "date": today,
            "time": time,
            "exercise": results['exercises'][x]['user_input'],
            "duration": results['exercises'][x]['duration_min'],
            "calories": results['exercises'][x]['nf_calories'],
        }
    }
    # BASIC AUTH
    # response_sheety = requests.post(url=SHEETY_ENDPOINT, json=SHEETY_JSON, headers=SHEETY_HEADERS, auth=(AUTH_USERNAME, AUTH_PASSWORD))
    # BEARER TOKEN
    response_sheety = requests.post(url=SHEETY_ENDPOINT, json=SHEETY_JSON, headers={"Authorization": f"Bearer {BEARER_TOKEN}"})
    response_sheety.raise_for_status()



