import requests, os, json
from dotenv import load_dotenv

# Retrieve a list of IND network devices
def get_alarms():
    url = f"https://{os.environ['IND_HOST']}/api/v1/alarms"

    user = os.environ['IND_USER']
    password = os.environ['IND_PASS']

    headers = {
        "Accept" : "application/json"
    }

    resp = requests.get(url, headers=headers, auth=requests.auth.HTTPBasicAuth(user, password), verify=False)
    alarms = resp.json()['records']
    
    return alarms

if __name__ == "__main__":
    load_dotenv()
    print(json.dumps(get_alarms(), indent=2))