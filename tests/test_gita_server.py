import pickle
import pytest
from gita_socket.client import GitaClient
from utils.packet import Packet


@pytest.fixture
def gita_client():
    return GitaClient()


def test_one(gita_client):
    try:
        p = Packet(1, 'None')
        res = gita_client.send_and_wait(p)
        c = pickle.loads(res)
    finally:
        gita_client.close_connection()
    assert (c.response == 'co')
