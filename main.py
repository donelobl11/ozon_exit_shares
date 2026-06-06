from modules.api_manager import ApiManager
from modules.exel_manager import ExelManager
from modules.main_stream import main_stream

import time


DELAY_MINUTS = 60


if __name__ == "__main__":
    while True:
        start_time = time.strftime('%X')
        print('Начало прогона' +': ' + start_time)
        exel_manager = ExelManager()
        accesses = exel_manager.load_api_keys()
        for access in accesses:
            print(f'\033[94m{access['Name']} started\033[0m')
            main_stream(access=access)
            print(f'\033[92m{access['Name']} finished\033[0m')
        
        print('Конец прогона: ' + 'начало - ' + start_time + ' | конец - ' + time.strftime('%X'))

        time.sleep(DELAY_MINUTS*60)