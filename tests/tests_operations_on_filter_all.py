from selenium.webdriver.common.keys import Keys

from todomvc_tests.model import todomvc


def test_activating():
    todomvc.given_opened_with('a', 'b', 'c',n=1)

    todomvc.toggle('b')

    todomvc.should_have_complete()
    todomvc.should_have_active('a','b','c')
    todomvc.should_have_items_left(3)


def test_clear_completing():
    todomvc.given_opened_with('a', 'b', 'c',n=2)


    todomvc.clear_completed()

    todomvc.should_have('a', 'b')
    todomvc.should_have_items_left(2)


def test_adding():
    todomvc.open()

    #When nothing add
    todomvc.add()

    todomvc.should_have_empty_todolist()

    #When
    todomvc.add('a')

    todomvc.should_have('a')
    todomvc.should_have_items_left(1)

    #When
    todomvc.add('b','c')

    todomvc.should_have('a', 'b', 'c')
    todomvc.should_have_items_left(3)


def test_editing():
    todomvc.given_opened_with('a', 'b', 'c')

    #When finish with enter
    todomvc.edit('b','b edited', Keys.ENTER)

    todomvc.should_have('a', 'b edited', 'c')
    todomvc.should_have_items_left(3)

    #When finish with tab
    todomvc.edit('c','c edited',Keys.TAB)

    todomvc.should_have('a','b edited','c edited')
    todomvc.should_have_items_left(3)


def test_cancel_editing():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.cancel_edit('c','c edited')

    todomvc.should_have('a','b','c')


def test_completing():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.toggle('a')

    todomvc.should_have_complete('a')
    todomvc.should_have_active('b','c')
    todomvc.should_have_items_left(2)


def test_completing_all():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.toggle_all()

    todomvc.should_have_complete('a','b','c')
    todomvc.should_have_active()
    todomvc.should_have_items_left(0)


def test_activating_all():
    todomvc.given_opened_with('a', 'b', 'c')
    todomvc.toggle_all()

    todomvc.toggle_all()

    todomvc.should_have_complete()
    todomvc.should_have_active('a','b','c')
    todomvc.should_have_items_left(3)


def test_deleting():
    todomvc.given_opened_with('a', 'b', 'c')

    todomvc.delete('b')

    todomvc.should_have('a','c')
    todomvc.should_have_items_left(2)   

