# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinaliser(fixture.destroy)
    return fixture


def test_add_group(application):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="qwerty", header="qwerty", footer="Test"))
    app.session.logout()


def test_add_empty_group(application):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
