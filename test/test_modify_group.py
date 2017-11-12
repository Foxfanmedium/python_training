# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(application):
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(application):
    app.group.modify_modify_first_group(Group(header="New header"))
