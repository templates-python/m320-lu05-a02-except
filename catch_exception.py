"""
A simple program to demonstrate except
"""
from namelist import NameList


def main():
    """ main function for running the code """
    name_list = NameList()
    for idx in range(6):
        print(name_list.take_name(idx))


if __name__ == '__main__':
    main()
