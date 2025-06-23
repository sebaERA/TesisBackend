import os
import requests
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
SURVEY_CODE = os.getenv("SURVEY_CODE")
BASE_URL = "https://rest.eus.canaryspeech.com"
SUBJECT_ID = os.getenv("SUBJECT_ID", "+tes")

def get_access_token():
    url = f"{BASE_URL}/v3/auth/tokens/get"
    headers = {"Csc-Api-Key": API_KEY, "Content-Type": "application/json"}
    response = requests.post(url, headers=headers)
    response.raise_for_status()
    return response.json()["accessToken"]

def begin_assessment(token):
    url = f"{BASE_URL}/v3/api/assessment/begin"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"subjectId": SUBJECT_ID, "surveyCode": SURVEY_CODE, "generateUploadUrls": True}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data["id"], data["uploadUrls"]["free_speech"]

def upload_audio(upload_url, audio_path):
    with open(audio_path, "rb") as audio_file:
        response = requests.put(upload_url, headers={"Content-Type": "audio/wav"}, data=audio_file.read())
        response.raise_for_status()

def end_assessment(token, assessment_id):
    url = f"{BASE_URL}/v3/api/assessment/end"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {
        "assessmentId": assessment_id,
        "responseData": [{
            "code": "free_speech",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "type": "recordedResponse",
            "data": {"duration": 60}
        }]
    }
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

def get_scores(token, assessment_id):
    url = f"{BASE_URL}/v3/api/list-scores?assessmentId={assessment_id}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    for _ in range(10):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            scores = data.get("scores", [])
            if scores:
                return scores
            time.sleep(2)
    raise Exception("No se pudo obtener resultados del análisis")

def analizar_audio(audio_path: str):
    token = get_access_token()
    assessment_id, upload_url = begin_assessment(token)
    upload_audio(upload_url, audio_path)
    end_assessment(token, assessment_id)
    scores = get_scores(token, assessment_id)
    return scores
