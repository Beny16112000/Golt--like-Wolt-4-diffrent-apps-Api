import requests
import json


# Send request to restaurant


class ApiClass:
    
    def __init__(self, restaurant, id, token):
        self.restaurant = restaurant
        self.id = id
        self.token = token

    def restaurantOrder(self):
        headers = {'Content-type': 'application/json'}
        headers['X-CSRFToken'] = self.token
        url = f'http://127.0.0.1:8000/restaurant/{self.restaurant}'
        data = {
            'id': self.id
        }
        response = requests.post(url, data=json.dumps(data),
                                            headers=headers)
        return response.status_code


