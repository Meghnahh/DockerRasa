import requests
url = "https://akshay2.herokuapp.com/webhooks/rest/webhook"
myobj = {
"message":"hi",
"sender":1,
}
x = requests.post(url, json = myobj)
print(x.text)
