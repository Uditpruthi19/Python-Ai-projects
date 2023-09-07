from PIL import Image, ImageDraw

# Create a new image with a white background
image = Image.new('RGB', (400, 400), 'white')
draw = ImageDraw.Draw(image)

# Draw a rectangle
rectangle_coords = (100, 100, 300, 300)
rectangle_color = (255, 0, 0)  # Red color
draw.rectangle(rectangle_coords, fill=rectangle_color)

# Draw a circle
circle_coords = (200, 200, 250, 250)
circle_color = (0, 255, 0)  # Green color
draw.ellipse(circle_coords, fill=circle_color)

# Save the image
image.save('tree-736885-1280.jpg')
