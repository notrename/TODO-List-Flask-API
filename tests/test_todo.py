import allure
import pytest
from datetime import datetime
import requests


@allure.feature('Тестирование ToDo API')
@pytest.mark.api
@pytest.mark.positive
class TestTODO:

    def test_post_query(self):
        with allure.step('Подготовка тестовых данных'):
            data = {
                'name': 'autotest task',
                'description': 'test description for autotest task',
                'priority': 'low',
                'deadline': datetime.now().strftime('%Y-%m-%d %H:%M'),
            }
        with allure.step('Отправка POST запроса'):
            result = requests.post('127.0.0.1:5000', json=data)
        assert result.status_code == 201

    def test_get_query(self): ...
