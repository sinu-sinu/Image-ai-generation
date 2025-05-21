from .google_auth import get_gspread_client

def open_sheet(sheet_id, worksheet_name="Sheet1"):
    client = get_gspread_client()
    sheet = client.open_by_key(sheet_id)
    worksheet = sheet.worksheet(worksheet_name)
    return worksheet

def read_global_attributes(worksheet):
    style = worksheet.acell('A2').value
    background_color = worksheet.acell('B2').value
    theme = worksheet.acell('C2').value
    return style, background_color, theme

def read_pose_titles(worksheet):

    pose_cells = worksheet.col_values(4)[1:]  # Skip header
    return pose_cells

def insert_image_url(worksheet, row_index, image_url):

    target_row = row_index + 2 
    worksheet.update_cell(target_row, 5, image_url)

