import requests
import json


# Send request to partner


class Api:

    def __init__(self, id, token):
        self.id = id
        self.token = token

    def partnerOrder(self):
        headers = {'Content-type': 'application/json'}
        headers['X-CSRFToken'] = self.token
        url = f'http://127.0.0.1:8000/partner/get-api'
        data = {
            'id': self.id
        }
        response = requests.post(url, data=json.dumps(data),
                                            headers=headers)
        return response.status_code