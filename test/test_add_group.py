# -*- coding: utf-8 -*-
from model.group import Group
import allure


@allure.title("Тест: добавление группы в справочник групп")
def test_add_group(app, db, check_ui, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    with allure.step('Проверяем эквивалентность нового списка групп со старым с добавленной группой'):
        with allure.step('Получаем новый список групп'):
            new_groups = db.get_group_list()
        with allure.step('Добавляем новую групп к старому списку групп'):
            old_groups.append(group)
        with allure.step('Сравниваем отсортированные списки групп'):
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            with allure.step('Проверяем эквивалентность нового списка групп со списком получаемым через UI-интерфейс'):
                assert sorted(map(Group.clean, new_groups), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                                           key=Group.id_or_max)
