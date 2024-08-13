import requests as rq

response = rq.post(
    url: 'http://127.0.0.1:5000/user',
    json={
        'title': 'title_1',
        'description': 'description_1',
        'owner': 'owner_1'
    },
)

print(response.status_code)
print(response.text)