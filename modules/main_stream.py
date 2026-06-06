from modules.api_manager import ApiManager



def main_stream(access):
    api_manager = ApiManager(access)
    list_actions = api_manager.get_list_actions()
    list_actions_filtered = []
    for action in list_actions['result']:
        list_actions_filtered.append({
            'id': action['id'],
            'title': action['title'],
            'date_start': action['date_start'],
            'date_end': action['date_end'],
            'potential_products_count': action['potential_products_count']
        })
    list_products_in_actions = []
    for action in list_actions_filtered:
        products = api_manager.get_list_products_in_actions(action['id'])
        list_products_in_actions.append({
            'action_id': action['id'],
            'products': products['result']['products'],
            'products_ids': [item['id'] for item in products['result']['products']]
        })
    for item in list_products_in_actions:
        if item['products'] == []:
            continue
        deleter_response = api_manager.delete_products_from_action(item['action_id'], item['products_ids'])
        print(deleter_response)