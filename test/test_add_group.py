# -*- coding: utf-8 -*-
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


def delete_first_group(self):
    wd = self.app.wd
    self.open_group_page()
    wd.find_element_by_name("selected[]").click()
    wd.find_element_by_name("delete").click()
    self.return_to_groups_page()


def test_add_empty_group(application):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
