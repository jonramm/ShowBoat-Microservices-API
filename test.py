from email import header
import requests
import json

# sample = {"name": "Santana"}
# res = requests.post("https://youtube-scraper-microservice.herokuapp.com/videos", json=sample)
# print(res.json())

reports = [
    {"sim_number": "1",
   "num_trials": "10000",
   "num_opponents": "2",
   "user_cards": "1",
   "opponent_cards": "1",
   "community_cards": "1", 
   "win_pct": "70.5",
   "loss_pct": "25.5",
   "tie_pct": "4.0"},

   {"sim_number": "2",
   "num_trials": "10000",
   "num_opponents": "2",
   "user_cards": "1",
   "opponent_cards": "1",
   "community_cards": "1", 
   "win_pct": "70.5",
   "loss_pct": "25.5",
   "tie_pct": "4.0"}
]

headers={"Content-Type": "application/json"}
res = requests.post("http://127.0.0.1:5000/report-generator", json=reports, headers=headers)
print(res)

# url = "https://showboat-rest-api.herokuapp.com/image-transform"

# payload={'url': 'https://www.ediblemontereybay.com/wp-content/uploads/2020/09/new-mexican-breakfast-burrito.jpg',
# 'height': '500',
# 'width': '400'}

# response = requests.post(url, data=payload)

# print(response)