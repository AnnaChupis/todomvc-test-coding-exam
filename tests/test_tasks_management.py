from todomvc_tests.model import todomvc


def test_crud():
    todomvc.open()

    todomvc.add('a','b','c')
    todomvc.should_have('a','b','c')

    todomvc.edit('b','b edited')

    todomvc.toggle('b edited')
    todomvc.clear_completed()
    todomvc.should_have('a', 'c')

    todomvc.cancel_edit('c','c edited')

    todomvc.delete('c')
    todomvc.should_have('a')
