

import requests

class ApiManager:
    LIST_ACTIONS_URL = 'https://api-seller.ozon.ru/v1/actions'
    LIST_PRODUCTS_IN_ACTIONS_URL = 'https://api-seller.ozon.ru/v1/actions/products'
    LIST_CANDIDATES_URL = 'https://api-seller.ozon.ru/v1/actions/candidates'
    DELETE_PRODUCTS_FROM_ACTION_URL = 'https://api-seller.ozon.ru/v1/actions/products/deactivate'

    def __init__(self, access):
        self.headers = {
            'Api-Key': access['Api-Key'],
            'Client-Id': access['Client-Id']
        }

    def get_list_actions(self):
        return requests.get(url=self.LIST_ACTIONS_URL, headers=self.headers).json()
    
    def get_list_products_in_actions(self, action_id):
        post_dict = {
            'action_id': action_id,
            'limit': 100,
        }
        return requests.post(url=self.LIST_PRODUCTS_IN_ACTIONS_URL, headers=self.headers, json=post_dict).json()

    def get_candidates_in_actions(self, action_id):
        post_dict = {
            'action_id': action_id,
            'limit': 100,
        }
        return requests.post(url=self.LIST_CANDIDATES_URL, headers=self.headers, json=post_dict).json()
    
    def delete_products_from_action(self, action_id, products_ids):
        post_dict = {
            'action_id': action_id,
            'product_ids': products_ids
        }
        return requests.post(url=self.DELETE_PRODUCTS_FROM_ACTION_URL, headers=self.headers, json=post_dict).json()