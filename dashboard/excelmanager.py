
def get_cell_range(start_col, start_row, end_col, end_row):
    import xlrd
    from core.settings import SPREADSHEET_MAIN

    workbook = xlrd.open_workbook(SPREADSHEET_MAIN)
    sheet = workbook.sheet_by_index(0)
    return [sheet.row_slice(row, start_colx=start_col, end_colx=end_col+1) for row in xrange(start_row, end_row+1)]
