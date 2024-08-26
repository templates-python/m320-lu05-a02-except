from catch_exception import main
from namelist import NameList


def test_found():
    names = NameList()
    value = names.take_name(3)
    assert value == 'Frida'


def test_except(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == 'Konrad\nGreta\nMike\nFrida\nEphron\nlist index out of range\n'
