def generate_prompt(content_title, style=None, background_color=None, theme=None):
    """
    Generates a detailed prompt string based on input values.
    """
    parts = []

    # Style description
    if style:
        parts.append(style.strip())

    # Yoga pose / content title
    parts.append(f"Show the yoga pose '{content_title}'")

    # Background color
    if background_color:
        parts.append(f"on a background color of {background_color}")

    # Theme context
    if theme:
        parts.append(f"for the theme: {theme.strip()}")

    prompt = ". ".join(parts) + "."
    return prompt
