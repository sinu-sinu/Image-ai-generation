# Optizon Yoga Pose Image Generator

This project automates the generation of yoga pose illustrations using the Hugging Face FLUX.1-dev model, uploads them to Imgur, and inserts the resulting image URLs into a Google Sheet.

## Features

- **Google Sheets Integration:** Reads yoga pose names and global prompt settings from a Google Sheet.
- **Prompt Generation:** Dynamically creates prompts for each pose using customizable style, background color, and theme.
- **Image Generation:** Uses Hugging Face's FLUX.1-dev model to generate images based on prompts.
- **Image Upload:** Uploads generated images to Imgur and retrieves shareable URLs.
- **Sheet Update:** Inserts image URLs/formulas back into the Google Sheet for easy viewing.

## Project Structure

```
.
├── config/
│   └── settings.py
├── data_sheets_key.json
├── image_api/
│   └── huggingface_image_generator.py
├── outputs/
├── prompts/
│   └── prompt_generator.py
├── sheets/
│   ├── google_auth.py
│   └── sheet_handler.py
├── src/
│   └── main.py
├── utils/
│   └── uploader.py
├── .env
├── requirements.txt
└── README.md
```

## Setup

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Create a `.env` file (already present in this repo) with:
   ```
   GOOGLE_SERVICE_ACCOUNT_JSON=data_sheets_key.json
   IMGUR_CLIENT_ID=your_imgur_client_id
   HF_API_KEY=your_huggingface_api_key
   ```

   - Place your Google service account JSON as `data_sheets_key.json` in the root directory.

4. **Set up Google Sheet**
   - Share your Google Sheet with the service account email found in `data_sheets_key.json`.

## Usage

Run the main script:

```sh
python src/main.py
```

- The script will read yoga poses from your Google Sheet, generate images, upload them to Imgur, and update the sheet with image formulas.

## Testing

You can test image generation with:

```sh
python test/test_stability.py
```

## Configuration

- **Google Sheet:** Update the `SHEET_ID` and `WORKSHEET_NAME` in [`src/main.py`](src/main.py) as needed.
- **Prompt Customization:** Modify prompt logic in [`prompts/prompt_generator.py`](prompts/prompt_generator.py).

## File Descriptions

- [`config/settings.py`](config/settings.py): Loads environment variables and API keys.
- [`image_api/huggingface_image_generator.py`](image_api/huggingface_image_generator.py): Handles image generation via Hugging Face API.
- [`utils/uploader.py`](utils/uploader.py): Uploads images to Imgur.
- [`sheets/sheet_handler.py`](sheets/sheet_handler.py): Reads/writes to Google Sheets.
- [`prompts/prompt_generator.py`](prompts/prompt_generator.py): Builds prompts for image generation.
- [`src/main.py`](src/main.py): Main orchestration script.

## License

This project is for educational and internal use only.

---

**Note:** Do not commit sensitive files such as `.env` or `data_sheets_key.json` to public repositories.