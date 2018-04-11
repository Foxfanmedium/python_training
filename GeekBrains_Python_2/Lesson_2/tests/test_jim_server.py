import pytest
import network.jim.server
import sys
import socket
import Lesson_2.network.jim.server.py


@pytest.fixture
def action():
    return 'sendto'


@pytest.fixture
def headers():
    return 'headers'


@pytest.fixture
def body():
    return 'body'


@pytest.fixture
def code():
    return 'code'




















