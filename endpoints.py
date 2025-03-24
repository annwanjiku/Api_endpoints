import requests

def get_landing_page():
    url = "http://127.0.0.1:5000"
    result = requests.get(url,headers={"content-type":"application/json"})
    return result.text

def get_names():
    url = ("http://127.0.0.1:5000/names")
    result = requests.get(url,headers={'content-type':'application/json'})

    if result.status_code == 200:
        return result.json()
    return {f"Error, request failed , status code {result.status_code}"}

def add_names():
    url = "http://127.0.0.1:5000/names/Amerlia"
    result = requests.post(url)
    return result.json()

def add_fruit():
    url = ("http://127.0.0.1:5000/fruits/ginger")
    result = requests.post(url)
    return result.json()

def update_school():
    url = ("http://127.0.0.1:5000/schools/HS/HighSchool")
    result = requests.put(url)
    return result.json()

def see_schools():
    url = "http://127.0.0.1:5000/schools"
    result = requests.get(url)
    return result.json()

if __name__ == "__main__":
    print(get_landing_page())
    # print(add_names())
    # print(update_school())
    # print(see_schools())
    # print(add_fruit())
    # print(get_names())
