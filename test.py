from email import header
import requests
import json

# sample = {"name": "Santana"}
# res = requests.post("https://youtube-scraper-microservice.herokuapp.com/videos", json=sample)
# print(res.json())

reports = [
    {"sim_number": "1",
    "user_cards": ["1", "2", "3"],
    "opponent_cards": [["1", "2"], ["3", "4"]],
   "community_cards": "1", 
   "num_trials": "10000",
   "num_opponents": "2",
   "win_pct": "70.5",
   "loss_pct": "25.5",
   "tie_pct": "4.0"},

    {"sim_number": "2",
    "user_cards": ["4", "5", "6"],
    "opponent_cards": [["1", "2"], ["3", "4"]],
   "community_cards": ["1", "2", "3"], 
   "num_trials": "10000",
   "num_opponents": "2",
   "win_pct": "70.5",
   "loss_pct": "25.5",
   "tie_pct": "4.0"}
]

headers={"Content-Type": "application/json"}
res = requests.post("https://showboat-rest-api.herokuapp.com/report-generator", json=reports, headers=headers)
print(res.text)

# url = "https://showboat-rest-api.herokuapp.com/image-transform"

# payload={'url': 'https://www.ediblemontereybay.com/wp-content/uploads/2020/09/new-mexican-breakfast-burrito.jpg',
# 'height': '500',
# 'width': '400'}

# response = requests.post(url, data=payload)

# print(response)