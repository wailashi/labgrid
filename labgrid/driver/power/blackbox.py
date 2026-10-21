import re
import requests

from ..exception import ExecutionError

PORT = 80

def power_set(host, port, index, value):
    index = int(index)
    state = "ON" if value else "OFF"
    assert 1 <= index <= 4

    response = requests.get(
            f"http://{host}:{port}/hidden.html?M0:O{index}={state}",
            )
    response.raise_for_status()


def power_get(host, port, index):
    index = int(index)
    assert 1 <= index <= 4

    response = requests.get(
            f"http://{host}:{port}/hidden.html",
            )
    response.raise_for_status()


    pattern = rf'M0:O{index}=(On|Off)'
    match = re.search(pattern, r.text)

    if not match:
        raise ExecutionError(f"Blackbox: Output index {index} not found in response"})

    state = match.groups(1)
    retrun state == 'On'

