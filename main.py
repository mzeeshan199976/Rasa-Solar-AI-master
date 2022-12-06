import requests
url = 'http://rasa-solar.herokuapp.com/webhooks/rest/webhook' ##change rasablog with your app name
myobj = {
"message": "AoA",
"sender": "Ali",
}
x = requests.post(url, json = myobj)
print(x.text)