from PIL import Image, ImageDraw, ImageFont
import textwrap


class Post:
    def __init__(self) -> None:
        pass

    def createImage(self,text,width=700,height=500,lineHeight=10):
        # Create a new image with a white background
        image = Image.new('RGB', (width, height), 'white')

        # Initialize the drawing context
        draw = ImageDraw.Draw(image)

        # Define the text and font
        font_size = 30
        font = ImageFont.truetype("georgia.ttf", font_size)

        # Wrap the text into multiple lines
        max_line_length = 40  # Adjust as needed
        wrapped_text = textwrap.fill(text, width=max_line_length)

        # Calculate the bounding box for each line of text
        lines = wrapped_text.split('\n')
        line_height = draw.textbbox((0, 0), "A", font=font)[3] - draw.textbbox((0, 0), "A", font=font)[1]

        # Calculate the total height of the text block
        text_block_height = len(lines) * line_height + (len(lines) - 1) * lineHeight

        # Calculate the starting y position to center the text block
        start_y = (height - text_block_height) / 2

        # Draw each line of the wrapped text
        for i, line in enumerate(lines):
            # Calculate the width of the current line
            line_width = draw.textbbox((0, 0), line, font=font)[2] - draw.textbbox((0, 0), line, font=font)[0]
            # Calculate the x position to center the line
            start_x = (width - line_width) / 2
            # Draw the line
            draw.text((start_x, start_y + i * (line_height + lineHeight)), line, fill="black", font=font)

        image.save("target_image.png")

        return "target_image.png"