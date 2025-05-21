from sheets.sheet_handler import open_sheet, read_global_attributes, read_pose_titles, insert_image_url
from prompts.prompt_generator import generate_prompt
from image_api.huggingface_image_generator import generate_image_url
from utils.uploader import upload_to_imgur


def main():
    # Set your actual Google Sheet ID
    SHEET_ID = "1yW3GftwNEq0VdVHQfhJBX1RC-DEK9nXEHdu1ldoA07Y"
    WORKSHEET_NAME = "Sheet1"

    worksheet = open_sheet(SHEET_ID, WORKSHEET_NAME)

    # Read global prompt configuration from row 2
    style, background_color, theme = read_global_attributes(worksheet)

    # Read all yoga poses from column D
    poses = read_pose_titles(worksheet)

    for index, pose_title in enumerate(poses):
        if not pose_title.strip():
            continue  # Skip empty rows

        prompt = generate_prompt(
            content_title=pose_title,
            style=style,
            background_color=background_color,
            theme=theme
        )

        print(f"[INFO] Generating image for: {pose_title}")
        image_path = generate_image_url(prompt)

        if image_path:
            image_url = upload_to_imgur(image_path)
            if image_url:
                formula = f'=IMAGE("{image_url}", 4, 100, 100)'
                insert_image_url(worksheet, index, formula)
            else:
                insert_image_url(worksheet, index, "Upload failed")
        else:
            print(f"[WARNING] No image generated for: {pose_title}")


if __name__ == "__main__":
    main()
