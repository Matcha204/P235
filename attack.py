import requests
for i in range(1,5000):
    URL = f'https://networking-ecommerce-new.onrender.com/profile?id={i}'
    r = requests.get(URL)
    if r.status_code == 200:
        print(URL)