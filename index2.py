# import cv2
# import numpy as np

# # Load the image
# img = cv2.imread('binary_image.png')

# # Convert the image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Threshold the grayscale image to obtain a binary mask
# _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

# # Convert the image to RGBA format
# rgba = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

# # Set the alpha channel of the image to the mask
# rgba[:, :, 3] = mask

# # Save the resulting image to a file
# cv2.imwrite('transparent_image.png', rgba)



# import cv2
# import numpy as np

# # Load the image and the background image
# img = cv2.imread('sample3.jpg')
# background = cv2.imread('pat2.jpg')

# # Compute the size of the border needed to repeat the background
# border_top = background.shape[0] // 2
# border_bottom = background.shape[0] - border_top - 1
# border_left = background.shape[1] // 2
# border_right = background.shape[1] - border_left - 1

# # Copy the edges of the image to create a border
# border_type = cv2.BORDER_DEFAULT
# img_border = cv2.copyMakeBorder(img, border_top, border_bottom, border_left, border_right, border_type)

# # Repeat the background image to fill the entire image
# background_repeat = np.tile(background, (img_border.shape[0] // background.shape[0] + 1, img_border.shape[1] // background.shape[1] + 1))
# background_repeat = background_repeat[:img_border.shape[0], :img_border.shape[1]]

# # Define a callback function for mouse events
# def mouse_callback(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # Create a mask image for flood filling
#         mask = np.zeros((img_border.shape[0] + 2, img_border.shape[1] + 2), np.uint8)
#         # Fill the region surrounding the clicked point with white color in the mask image
#         cv2.floodFill(img_border, mask, (x + border_left, y + border_top), (255, 255, 255))

#         # Combine the bordered image with the repeating background image
#         img_background = cv2.bitwise_and(background_repeat, background_repeat, mask=cv2.bitwise_not(img_border))
#         img_repeat = cv2.bitwise_or(img_border, img_background)

#         # Display the updated image
#         cv2.imshow('image', img_repeat)

# # Set the callback function for mouse events
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', mouse_callback)

# # Display the image
# cv2.imshow('image', img_border)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2

# # Load the image
# img = cv2.imread('sample1.png')

# # Convert the image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Threshold the grayscale image to obtain a binary image
# _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# # Save the binary image to a file
# cv2.imwrite('binary_image.png', thresh)


# # Load the image
# img = cv2.imread('binary_image.png')

# # Convert the image to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Threshold the grayscale image to obtain a binary mask
# _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

# # Convert the image to RGBA format
# rgba = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

# # Set the alpha channel of the image to the mask
# rgba[:, :, 3] = mask

# # Save the resulting image to a file
# cv2.imwrite('transparent_image.png', rgba)

# import cv2

# # Load the image
# image = cv2.imread('transparent_image.png')

# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Threshold the image to create a binary image
# _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# # Find the contours (regions) in the binary image
# contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Create a text file to save the coordinates
# with open('coordinates.txt', 'w') as file:

#     # Loop through the contours and save the coordinates to the text file
#     for contour in contours:
#         x, y, w, h = cv2.boundingRect(contour)
#         file.write(f'{x},{y},{x+w},{y+h}\n')
from PIL import Image

class FloodFill:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.width, self.height = self.image.size
        self.image_data = self.image.load()

    def flood_fill(self, x, y, target_color, replacement_color):
        if target_color == replacement_color:
            return

        pixels_to_check = [(x, y)]
        while pixels_to_check:
            current_pixel = pixels_to_check.pop()
            x, y = current_pixel
            if (0 <= x < self.width and 0 <= y < self.height and
                    self.image_data[x, y] == target_color):
                self.image_data[x, y] = replacement_color
                pixels_to_check.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])

    def flood_fill_from_click(self, x, y, replacement_color):
        target_color = self.image_data[x, y]
        self.flood_fill(x, y, target_color, replacement_color)

if __name__ == "__main__":
    image_path = "transparent_image.png"
    floodfill = FloodFill(image_path)

    # Example usage: floodfill a region around pixel (100, 100) with red color
    floodfill.flood_fill_from_click(100, 100, (255, 0, 0))

    # Save the modified image
    floodfill.image.save("output.png")
