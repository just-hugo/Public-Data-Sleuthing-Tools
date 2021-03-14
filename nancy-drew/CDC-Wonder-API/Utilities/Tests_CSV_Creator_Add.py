import unittest
from csv_utilities import make, add, read, find

read= read()
make = make()
add = add()
find = find()

# TODO: refactor tests to remove dependencies on other functions. Ex do not use find.cell() inside of a test that is not written for find.cell() (do not call find.cell() in a test where you're adding a cell to a row).


class AddCellToRow(unittest.TestCase):

    def test_1_happy_path_string(self):
        """
        add.cell_to_row() takes a string (cell) and adds it to a list (row).
        """

        # Test data
        cell = "test_string"
        row = []

        # Test steps
        add.cell_to_row(cell, row)
        self.assertTrue(row)

    def test_2_happy_path_list(self):
        """
        add.cell_to_row() can take a list as the first argument to populate multiple cells across a row.

        This functionality is similar to copy-and-pasting a whole row in a spreadsheet.
        """

        # Test data
        cell_list = ["string_1", "string_2"]
        row = []

        # Test steps
        add.cell_to_row(cell_list, row)
        self.assertTrue(row)

    def test_3_negative_dict_as_argument(self):
        """
        add.cell_to_row() cannot take a dictionary as the first argument.
        """

        # Test data
        cell = {"gender": "blah"}
        row = []

        # Test steps
        try:
            add.cell_to_row(cell, row)

        except Exception as e:

            self.assertIn("Cell argument cannot be a dictionary. Valid cell types are: string and list.", str(e))

    def test_4_missing_argument(self):
        """
        add.cell_to_row() requires 2 arguments: a cell (string or list) and a row (list).

        Missing arguments will generate a TypeError.
        """

        # Test data
        cell = "string_1"

        # Test steps
        try:
            add.cell_to_row("string")

        except Exception as e:
            self.assertIsInstance(e, TypeError)

        try:
            add.cell_to_row([])

        except Exception as e:
            self.assertIsInstance(e, TypeError)


class AddCellsToRowBySelector(unittest.TestCase):

    def test_1_happy_path(self):
        """
        add.cells_to_row_by_selector() takes a dictionary argument and returns a list of all the dictionary values.
        """

        # Test data
        cells = {'cell_1': 'some.selector'}

        # Test steps
        row = add.cells_to_row_by_selector(cells)
        self.assertIsInstance(row, list)

    def test_2_negative_string_as_argument(self):
        """
        add.cells_to_row_by_selector() cannot accept strings as arguments.
        """

        # Test data
        row = []

        # Test steps
        try:
            add.cells_to_row_by_selector('string_1', row)

        except Exception as e:

            self.assertIn("Argument must be a dictionary. The convention is 'cell name': 'cell selector'.", str(e))

    def test_3_negative_list_as_argument(self):
        """
        add.cells_to_row_by_selector() cannot accept lists as arguments.
        """

        # Test data
        cell = ["string_1", "string_2"]
        row = []

        # Test steps
        try:
            add.cells_to_row_by_selector(cell, row)

        except Exception as e:
            self.assertIn("Argument must be a dictionary. The convention is 'cell name': 'cell selector'.", str(e))


class AddRowToTable (unittest.TestCase):

    def test_1_happy_path(self):
        """
        add.row_to_table() takes two arguments: a list (row) and a list of lists (table).
        It returns the row appended to the table.
        """

        # Test data
        row = ["cell_1", "cell_2", "cell_3"]
        table = []

        # Test steps
        add.row_to_table(row, table)
        self.assertIn(row, table)


class FindCell (unittest.TestCase):

    def test_1_happy_path_required_arguments(self):
        """
        find.cell(object, x) returns <class 'bs4.element.ResultSet'>
        """

        # Test data
        test_xml_file = read.file('../API-Responses/D140_All_Homicides_By_Year.xml')

        # Test steps
        tree = make.xml_tree(test_xml_file)
        test = find.cell(tree, 'r')
        self.assertIsInstance(test, list, 'bs4.element.ResultSet')

    def test_2_happy_path_optional_arguments(self):
        """
        find.cell(object, x, y, z) returns the expected string.
        """

        # Test data
        test_xml_file = read.file('../API-Responses/D140_All_Homicides_By_Year.xml')
        test_xml_file.data = 3

        # Test steps
        tree = make.xml_tree(test_xml_file)
        test = find.cell(tree, 'c[v]', 2, 'v')
        self.assertIn(test, '367.1')

    def test_3_negative_invalid_object(self):
        """
        when object is dict:
        AttributeError: 'dict' object has no attribute 'select'
        when object is string:
        AttributeError: 'str' object has no attribute 'select'
        when object is list:
        AttributeError: 'list' object has no attribute 'select'
        when object is int:
        AttributeError: 'int' object has no attribute 'select'
        """
        # Test data
        print('placeholder')

        # Test steps

    def test_4_negative_invalid_x(self):

        # Test data
        print('placeholder')

        # Test steps

    def test_4_negative_invalid_y(self):

        # Test data
        print('placeholder')

        # Test steps

    def test_5_negative_invalid_z(self):

        # Test data
        print('placeholder')

        # Test steps

    def test_6_negative_x_y(self):

        # Test data
        print('placeholder')

        # Test steps
