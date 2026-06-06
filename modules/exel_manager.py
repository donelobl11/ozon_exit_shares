import pandas as pd
import logging
from pathlib import Path
from typing import Dict, List

class ExelManager:
    ACCESS_PATH: str = 'user_data/api_keys.xlsx'
    ACCESS_REQUIRED_COLUMNS = ['Name', 'Client-Id', 'Api-Key']

    def __init__(self) -> None:
        """Инициализирует менеджер работы с эксель файлами."""
        self._validate_paths()

    def _validate_paths(self) -> None:
        """Проверяет существование необходимых директорий."""
        Path('user_data').mkdir(parents=True, exist_ok=True)

    def load_api_keys(self) -> List[Dict[str, str]]:
        """Загружает API ключи из Excel файла.
        
        Returns:
            List[Dict[str, str]]: Список словарей с ключами клиентов
            
        Raises:
            FileNotFoundError: Если файл не существует
            ValueError: Если отсутствуют обязательные колонки
        """
        try:
            df = pd.read_excel(self.ACCESS_PATH)
            
            missing_cols = [col for col in self.ACCESS_REQUIRED_COLUMNS if col not in df.columns]
            if missing_cols:
                raise ValueError(f"Отсутствуют обязательные колонки: {missing_cols}")
            
            access_list = df[self.ACCESS_REQUIRED_COLUMNS].astype(str).to_dict('records')
            
            print(f"Успешно загружено {len(access_list)} API ключей")
            return access_list
            
        except FileNotFoundError:
            print(f"Файл {self.ACCESS_PATH} не найден")
            raise
        except Exception as e:
            print(f"Ошибка при загрузке API ключей: {str(e)}")
            raise




