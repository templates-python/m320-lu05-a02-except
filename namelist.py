"""
provides the class NameList
"""


class NameList:
    """
    Diese Klasse dient der Nutzung von try-except, um das "fangen" eines Fehlers zu implementieren.
    Es wird bewusst eine Liste implementiert, bei der falsche Indexe möglich sind, so dass ein
    IndexError erzeugt wird.
    """

    def __init__(self):
        """
        constructor without arguments: creates a list
        """
        self._name_list = ['Konrad', 'Greta', 'Mike', 'Frida', 'Ephron']

    def take_name(self, index):
        """
        returns the name at the specified index
        :param: the index of the requested name
        :return: the name at the index
        """
        return self._name_list[index]
