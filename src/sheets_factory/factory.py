"""This is the main software file."""

import string
from os.path import abspath, basename, dirname, join

import pandas as pd
from pyexcelerate import Workbook


class SheetsFactory:
    def __init__(self, sheet_name: str, sheet_header: list, sheet_rows: list[list], diretory, file_name=None):
        self.work_sheet_name: str = sheet_name
        self.diretory: str = diretory
        self.file_name: str = file_name
        self.sheet_data: list = [sheet_header]
        self.sheet_data += sheet_rows

    def build_file_path_name(self, index=None):
        file_path = join(self.diretory, f"{self.file_name}_{index}" if index is not None else f"{self.file_name}")
        if ".xlsx" not in file_path:
            file_path = f"{file_path}.xlsx"
        return file_path

    def pandas(self, file_name=None, rows_data=None):
        """Generate a .xlsx with pandas."""
        print("Running pandas solution.")
        if file_name:
            self.file_name = file_name
        file_name = self.build_file_path_name()
        if not rows_data:
            rows_data = self.sheet_data

        pd.DataFrame(rows_data).to_excel(
            file_name,
            index=False,
            header=False
        )

    def pyexcelerate(self, file_name=None, rows_data=None):
        """Generate a .xlsx with pyexcelerate."""
        print("Running pyexcelerate solution.")
        if file_name:
            file_name = self.build_file_path_name()
        if not rows_data:
            rows_data = self.sheet_data

        wb = Workbook()
        wb.new_sheet(self.work_sheet_name, data=rows_data)
        wb.save(file_name)

    def chunked(self, size_of_chunk=200000, pandas=False):
        for index, chunk in enumerate(
                [self.sheet_data[x:x + size_of_chunk] for x in range(0, len(self.sheet_data), size_of_chunk)]):
            file_path = self.build_file_path_name(index=index)
            print(f"Criando: {file_path}")

            if pandas:
                self.pandas(file_name=file_path, rows_data=chunk)
            else:
                self.pyexcelerate(file_name=file_path, rows_data=chunk)


if __name__ == "__main__":
    mock_sheet_name = "Sheet_name_test"
    work_dir = dirname(dirname(abspath(".")))
    print(work_dir)
    abc_sheet_header = [x for x in string.ascii_lowercase]
    int_sheet_rows = [list(range(len(abc_sheet_header)))] * 1048574
    # int_sheet_rows = [list(range(len(abc_sheet_header)))] * 5

    wsf = SheetsFactory(
        sheet_name=mock_sheet_name,
        sheet_header=abc_sheet_header,
        sheet_rows=int_sheet_rows,
        diretory=work_dir,
        file_name=mock_sheet_name
    )
    # wsf.pandas()
    # wsf.pyexcelerate()
    wsf.chunked()
