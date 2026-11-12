import requests

# 1. تست ثبت نام (Register)
url_register = "http://127.0.0.1:5000/register"
data = {"username": "moein_test", "password": "1234"}
response = requests.post(url_register, json=data)

print("Status Code:", response.status_code)
print("Response:", response.text)