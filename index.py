# from PIL import Image

# # Load the image
# img = Image.open("sample1.png")

# # Create new images for each darkness level
# light_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
# medium_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
# dark_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))

# # Separate the pixels based on their darkness and add them to the appropriate layer
# for y in range(img.size[1]):
#     for x in range(img.size[0]):
#         # Get the RGBA color of the pixel
#         r, g, b, a = img.getpixel((x, y))
#         # Calculate the brightness of the pixel using the formula: 0.2126*R + 0.7152*G + 0.0722*B
#         brightness = int(0.2126*r + 0.7152*g + 0.0722*b)
#         # Add the pixel to the appropriate layer based on its brightness
#         if brightness > 200:
#             light_layer.putpixel((x, y), (r, g, b, a))
#         elif brightness > 100:
#             medium_layer.putpixel((x, y), (r, g, b, a))
#         else:
#             dark_layer.putpixel((x, y), (r, g, b, a))

# # Save the output images with layers
# light_layer.save("light_layer.png")
# medium_layer.save("medium_layer.png")
# dark_layer.save("dark_layer.png")


from PIL import Image

# Load the image
img = Image.open("sample4.png")

# Create new images for each grayness scale
light_layer = Image.new("RGB", img.size, (255, 255, 255))
medium_layer = Image.new("RGB", img.size, (255, 255, 255))
dark_layer = Image.new("RGB", img.size, (255, 255, 255))

# Separate the pixels based on their grayness scale and add them to the appropriate layer
for y in range(img.size[1]):
    for x in range(img.size[0]):
        # Get the RGB color of the pixel
        r, g, b, a= img.getpixel((x, y))
        # Calculate the grayness of the pixel using the formula: 0.299*R + 0.587*G + 0.114*B
        grayness = int(0.299*r + 0.587*g + 0.114*b)
        # Add the pixel to the appropriate layer based on its grayness scale
        if grayness > 200:
            light_layer.putpixel((x, y), (r, g, b))
        elif grayness > 100:
            medium_layer.putpixel((x, y), (r, g, b))
        else:
            dark_layer.putpixel((x, y), (r, g, b))

# Save the output images with layers
light_layer.save("light_layer.png")
medium_layer.save("medium_layer.png")
dark_layer.save("dark_layer.png")