import csv
from bs4 import BeautifulSoup

class add:

    def __init__(self):
        return

    # Argument must be string or list
    def cell_to_row(self, cell, row_name):

        if type(cell) is str:
            row_name.append(cell)
            return row_name

        elif type(cell) is list:
            row_name.append(cell)
            return row_name

        elif type(cell) is dict:
            raise TypeError("Cell argument cannot be a dictionary. Valid cell types are: string and list.")

        elif type(cell) is int:
            raise TypeError("Cell argument cannot be an integer. Valid cell types are: string and list.")

    # Argument must be a dictionary
    def cells_to_row_by_selector(self, *args):

        try:
            row_of_cells = []

            for cell_name in args:
                for selector in cell_name:
                    row_of_cells.append(cell_name[selector])
            return row_of_cells

        except TypeError:
            raise TypeError("Argument must be a dictionary. The convention is 'cell name': 'cell selector'.")


    def row_to_table(self, row_to_add, table_list):
        return table_list.append(row_to_add)


class find:

    def __init__(self):
        return

    def cell(self, soup_object, x=str, y=None, z=None):
        """
        Row must be a BeautifulSoup object.

        x is a string, y is a number, z is a string. These are positional coordinates for the Beautiful Soup syntax tree.

        Arguments must be submitted in one of the following combinations: (row, x) or (row, x, y, z).

        (row, x, y) and (row x, z) are not permitted.
        """

        if z:
            return soup_object.select(x)[y][z]
        elif z is None:
            if y is None:
                return soup_object.select(x)
            else:
                raise Exception()


class make:

    def __init__(self):
        return

    def csv_file(self, csv_file_name, csv_data):
        # csv_data should be a list of lists, where each list is a row and each item is a cell, ex [[Row, 1][Row, 2]]
        with open(csv_file_name, mode='w', newline='') as file:
            write = csv.writer(file)
            write.writerows(csv_data)
        return print(csv_file_name + ' has been made.')

    def new_table(self, *args):
        test = []
        for arg in args:
            test.append(arg)
        return [test]

    def xml_tree(self, response_file):
        return BeautifulSoup(response_file, "html.parser")


class read:

    def __init__(self):
        return

    def file(self, filename):
        with open(filename, 'r') as file:
            return file.read()

    def table_data(self, data_table):
        year_by_year_table = []
        for each_row in data_table:
            try:
                cells = {'gender': find.cell(self, each_row, 'c[l]', 0, 'l'),
                         'race': find.cell(self, each_row, 'c[l]', 1, 'l'),
                         'year': find.cell(self, each_row, 'c[l]', 2, 'l'),
                         'deaths': find.cell(self, each_row, 'c[v]', 0, 'v'),
                         'pop': find.cell(self, each_row, 'c[v]', 1, 'v'),
                         'crude_rate': find.cell(self, each_row, 'c[v]', 2, 'v')}

                year_by_year_row = add.cells_to_row_by_selector(self, cells)
                add.row_to_table(self, year_by_year_row, year_by_year_table)
                print(year_by_year_row)
            except:
                print('except')
        return




