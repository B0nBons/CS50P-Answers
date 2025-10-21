import requests

def get_excuse():
    e = requests.get('https://excuser-three.vercel.app/v1/excuse/developers/')
    e = e.json()
    return e

def find_excuse(x):
    ex = (x[0]["excuse"])
    return ex

try:
    print(find_excuse(get_excuse()))

except requests.exceptions.Timeout:
    print("Timed out.")
