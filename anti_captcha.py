import requests
import json
import time
import base64

path = "your_image.jpeg"
with open(path, "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
picture = str(my_string)
picture = picture[1:]
print(picture)
while True:
    try:
        opa = {
            "clientKey": "", #your client key
            "task": {
                "type": "ImageToTextTask",
                "body": picture,
                "phrase": False,
                "case": False,
                "numeric": False,
                "math": 0,
                "minLength": 0,
                "maxLength": 0
            },
           "languagePool": "rn"
        }
        response = requests.get('https://api.anti-captcha.com/createTask ', json=opa)

        print(response.text)

        x = json.loads(response.text)
        y = x["taskId"]

        dude = {
            "clientKey": "", #your client key
            "taskId": y
        }
        while True:
            try:
                response1 = requests.get('https://api.anti-captcha.com/getTaskResult', json=dude)
                z = json.loads(response1.text)
                captcha = z["solution"]["text"]
                break
            except:
                time.sleep(1)
                #print("sleep")
                continue
        print(captcha)
        # введите каптчу
        break
    except:
        continue
