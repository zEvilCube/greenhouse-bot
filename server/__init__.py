import json
from typing import Tuple, Any

import requests

from config import config
from templates import *

BASE_URL = config.server_url.get_secret_value()


def verify_auth(api_key: str) -> bool:
    response = requests.get(f"{BASE_URL}/auth?api_key={api_key}")
    return response.status_code == 200


def get_readings(api_key: str) -> tuple[int, int, int] | tuple[None, None, None]:
    response = requests.get(f"{BASE_URL}/readings?api_key={api_key}")
    if response.status_code != 200:
        return None, None, None

    values = json.loads(response.text)
    return (
        values.get("light") or MISSING_VALUE,
        values.get("temperature") or MISSING_VALUE,
        values.get("humidity") or MISSING_VALUE
    )


def get_references(api_key: str) -> tuple[int, int, int] | tuple[None, None, None]:
    response = requests.get(f"{BASE_URL}/references?api_key={api_key}")
    if response.status_code != 200:
        return None, None, None

    values = json.loads(response.text)
    return (
        values.get("light"),
        values.get("temperature"),
        values.get("humidity")
    )


def change_references(api_key: str, light: int = None, temp: int = None, humidity: int = None) -> None:
    requests.put(
        f"{BASE_URL}/references",
        json={"api_key": api_key, "light": light, "temperature": temp, "humidity": humidity}
    )
