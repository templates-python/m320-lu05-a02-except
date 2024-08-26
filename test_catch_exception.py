from namelist import NameList


def test_found():
    names = NameList()
    value = names.take_name(3)
    assert value == 'Frida'

def test_except():
    names = NameList()
    value = names.take_name(7)
    assert value == 'foobar'