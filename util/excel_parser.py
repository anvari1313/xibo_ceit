import xlrd
from xlrd.sheet import ctype_text


class ExcelParser:
    def __init__(self, file_path):
        # Open the workbook
        self.__xl_workbook = xlrd.open_workbook(file_path)
        self.sheet_names = self.__xl_workbook.sheet_names()
        self.cols = []
        self.rows = []

    def parse(self):
        self.parse_sheet(self.sheet_names[0])
        # for sheet_name in self.sheet_names:
            # self.parse_sheet(sheet_name=sheet_name)

    def parse_sheet(self, sheet_name):

        xl_sheet = self.__xl_workbook.sheet_by_name(sheet_name)

        num_cols = xl_sheet.ncols  # Number of columns
        for col_idx in range(0, num_cols):  # Iterate through columns
            self.cols.append(xl_sheet.cell(0, col_idx).value) # Get cell object by row, col

        print(self.cols)

        num_cols = xl_sheet.ncols  # Number of columns
        for row_idx in range(1, xl_sheet.nrows):  # Iterate through rows
            current_row = []
            for col_idx in range(0, num_cols):  # Iterate through columns
                cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
                current_row.append(cell_obj.value)

            self.rows.append(current_row)

        print(self.rows)