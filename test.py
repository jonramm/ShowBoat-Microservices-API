from email import header
import requests
import json

# sample = {"name": "Kendrick Lamar", "type": "popular"}
# res = requests.post("https://youtube-scraper-microservice.herokuapp.com/videos", json=sample)
# print(res.json())

reports = [
    {"sim_number": "1",
    "num_trials": "10000",
    "user_cards": [12, 52],
    "opponent_cards": [[38, 52], [52, 52], [11, 0]],
   "community_cards": [25, 52, 52, 52, 52], 
   "win_pct": "70.5",
   "loss_pct": "25.5",
   "tie_pct": "4.0"},

    {"sim_number": "2",
    "user_cards": [51, 52],
    "opponent_cards": [[38, 52], [11, 0]],
   "community_cards": [25, 52, 52, 52, 52], 
   "num_trials": "10000",
   "win_pct": "70.5",
   "loss_pct": "25.5",
   "tie_pct": "4.0"}
]

headers={"Content-Type": "application/json"}
# res = requests.post("https://showboat-rest-api.herokuapp.com/report-generator", json=reports, headers=headers)
res = requests.post("http://127.0.0.1:5000/report-generator", json=reports, headers=headers)
print(res.text)

# url = "https://showboat-rest-api.herokuapp.com/image-transform"

# payload={'url': 'https://www.ediblemontereybay.com/wp-content/uploads/2020/09/new-mexican-breakfast-burrito.jpg',
# 'height': '500',
# 'width': '400'}

# response = requests.post(url, data=payload)

# print(response)

# res = requests.get("https://mstagg.pythonanywhere.com/2022-06-22/")
# print(res)