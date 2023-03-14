# import cv2
# import numpy as np

# def get_polygons(image_path):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Check if the image is loaded correctly
#     if image is None:
#         print(f"Error: Failed to load image '{image_path}'")
#         return

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Threshold the grayscale image to create a binary image
#     _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

#     # Find the contours in the binary image
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Create a mask for each polygon and save it to a separate file
#     for i, contour in enumerate(contours):
#         mask = np.zeros_like(gray)
#         cv2.drawContours(mask, [contour], 0, 255, -1)
#         cv2.imwrite(f"polygon_{i}.png", mask)

# if __name__ == "__main__":
#     get_polygons("sample1.png")


# import cv2
# import numpy as np

# def get_polygons(image_path):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Check if the image is loaded correct  ly
#     if image is None:
#         print(f"Error: Failed to load image '{image_path}'")
#         return

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Threshold the grayscale image to create a binary image
#     _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

#     # Show the binary image
#     cv2.imshow("Binary Image", thresh)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     get_polygons("sample1.png")


# import cv2
# import numpy as np

# def get_polygons(image_path):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Check if the image is loaded correctly
#     if image is None:
#         print(f"Error: Failed to load image '{image_path}'")
#         return

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Threshold the grayscale image to create a binary image
#     _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

#     # Find the contours in the binary image
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Create a mask for each polygon and save it to a separate file
#     for i, contour in enumerate(contours):
#         mask = np.zeros_like(gray)
#         cv2.drawContours(mask, [contour], 0, 255, -1)
#         cv2.imwrite(f"polygon_{i}.png", mask)

#         # Save the x and y coordinates of the contour to a text file
#         x, y, _, _ = cv2.boundingRect(contour)
#         with open(f"polygon_{i}.txt", "w") as f:
#             f.write(f"{x} {y}")

# if __name__ == "__main__":
#     get_polygons("sample1.png")


# import cv2
# import numpy as np

# def get_polygons(image_path):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Check if the image is loaded correctly
#     if image is None:
#         print(f"Error: Failed to load image '{image_path}'")
#         return

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Threshold the grayscale image to create a binary image
#     _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

#     cv2.imwrite("thresh_image.png", thresh)

#     # Find the contours in the binary image
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Create a mask for each polygon and save it to a separate file
#     for i, contour in enumerate(contours):
#         mask = np.zeros_like(gray)
#         cv2.drawContours(mask, [contour], 0, 255, -1)
#         cv2.imwrite(f"polygon_{i}.png", mask)

#         # Save the x and y coordinates of each side of the contour to a text file
#         with open(f"polygon_{i}.txt", "w") as f:
#             for point in contour:
#                 x, y = point[0]
#                 f.write(f"ctx.lineTo({x}, {y})\n")

# if __name__ == "__main__":
#     get_polygons("sample1.png")



# import cv2
# import numpy as np

# def get_polygons(image_path):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Check if the image is loaded correctly
#     if image is None:
#         print(f"Error: Failed to load image '{image_path}'")
#         return

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Threshold the grayscale image to create a binary image
#     _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

#     cv2.imwrite("thresh_image.png", thresh)

#     # Find the contours in the binary image
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     polygons = {}
#     # Create a mask for each polygon and save it to a separate file
#     for i, contour in enumerate(contours):
#         mask = np.zeros_like(gray)
#         cv2.drawContours(mask, [contour], 0, 255, -1)
#         cv2.imwrite(f"polygon_{i}.png", mask)

#         # Save the x and y coordinates of each side of the contour to a dictionary
#         polygon_points = []
#         for point in contour:
#             x, y = point[0]
#             polygon_points.append([x, y])
#         polygons[f"polygon{i}"] = polygon_points

#     # Save the polygon dictionary to a text file
#     with open("polygons.txt", "w") as f:
#         f.write(str(polygons))

# if __name__ == "__main__":
#     get_polygons("sample1.png")

# import cv2
# import numpy as np

# def get_polygons(image_path):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Check if the image is loaded correctly
#     if image is None:
#         print(f"Error: Failed to load image '{image_path}'")
#         return

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Threshold the grayscale image to create a binary image
#     _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

#     cv2.imwrite("thresh_image.png", thresh)

#     # Find the contours in the binary image
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     polygons = {}
#     objects = {}
#     # Create a mask for each polygon and save it to a separate file
#     for i, contour in enumerate(contours):
#         mask = np.zeros_like(gray)
#         cv2.drawContours(mask, [contour], 0, 255, -1)
#         cv2.imwrite(f"polygon_{i}.png", mask)

#         # Save the x and y coordinates of each side of the contour to a dictionary
#         polygon_points = []
#         for point in contour:
#             x, y = point[0]
#             polygon_points.append([x, y])
#         polygons[f"polygon{i}"] = polygon_points

#         # Mask the original image with the polygon mask and find the contours in the masked image
#         masked_image = cv2.bitwise_and(image, image, mask=mask)
#         object_contours, _ = cv2.findContours(cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         # Save the objects in the polygon to a dictionary
#         objects_in_polygon = []
#         for j, object_contour in enumerate(object_contours):
#             object_points = []
#             for point in object_contour:
#                 x, y = point[0]
#                 object_points.append([x, y])
#             objects_in_polygon.append(object_points)
#         objects[f"polygon{i}"] = objects_in_polygon

#     # Save the polygon and object dictionaries to a text file
#     with open("polygons.txt", "w") as f:
#         f.write(str(polygons))
#     with open("objects.txt", "w") as f:
#         f.write(str(objects))

# if __name__ == "__main__":
#     get_polygons("sample1.png")

# import cv2
# import numpy as np

# def get_polygons(image_path):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Check if the image is loaded correctly
#     if image is None:
#         print(f"Error: Failed to load image '{image_path}'")
#         return

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Threshold the grayscale image to create a binary image
#     _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

#     cv2.imwrite("thresh_image.png", thresh)

#     # Find the contours in the binary image
#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     polygons = {}
#     # Create a mask for each polygon and save it to a separate file
#     for i, contour in enumerate(contours):
#         mask = np.zeros_like(gray)
#         cv2.drawContours(mask, [contour], 0, 255, -1)

#         # Find the contours in the mask for each polygon
#         poly_contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         # Save the x and y coordinates of each side of the contour to a dictionary
#         polygon_points = []
#         for point in contour:
#             x, y = point[0]
#             polygon_points.append([x, y])
#         polygons[f"polygon{i}"] = polygon_points

#         # Save the x and y coordinates of each point in the contour to the polygon dictionary
#         for j, poly_contour in enumerate(poly_contours):
#             poly_points = []
#             for point in poly_contour:
#                 x, y = point[0]
#                 poly_points.append([x, y])
#             polygons[f"polygon{i}_hole{j}"] = poly_points

#         # Save the mask for each polygon and its holes to a separate file
#         cv2.imwrite(f"polygon_{i}.png", mask)
#         for j, poly_contour in enumerate(poly_contours):
#             hole_mask = np.zeros_like(gray)
#             cv2.drawContours(hole_mask, [poly_contour], 0, 255, -1)
#             cv2.imwrite(f"polygon_{i}_hole_{j}.png", hole_mask)

#     # Save the polygon dictionary to a text file
#     with open("polygons.txt", "w") as f:
#         f.write(str(polygons))

# if __name__ == "__main__":

# Python code to detect an arrow (seven-sided shape) from an image.
import cv2
import numpy as np
from PIL import Image
import json

def get_polygons(img, filename):
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold image
    ret, thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY)

    cv2.imwrite('binary.png', gray)

    # Find contours of polygons
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Create a dictionary to store the polygons
    polygons = {}

    # Extract the x y coordinates for each polygon
    for i, contour in enumerate(contours):
        # Get the x y coordinates of the current polygon
        polygon = contour.squeeze().tolist()

        # Add the polygon to the dictionary
        polygons[f'polygon{i}'] = polygon

    # Save the polygons to a TXT file
    with open(filename, 'w') as f:
        json.dump(polygons, f, indent=2)

    return polygons



# Load the image and get the polygons
img = cv2.imread('tt.png')

# Get the polygons and save to a TXT file
polygons = get_polygons(img, 'polygons.txt')



# import cv2
# import numpy as np
# from PIL import Image
# import json

# def get_polygons(img, filename):
# # Convert image to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # Threshold image using different threshold values
#     thresholds = [127, 150, 200,225,250]
#     for i, threshold in enumerate(thresholds):
#         _, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
#         cv2.imwrite(f'binary_{i}.png', thresh)

#     # Find contours of polygons
#     contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#     # Create a dictionary to store the polygons
#     polygons = {}

#     # Extract the x y coordinates for each polygon
#     for i, contour in enumerate(contours):
#         # Get the x y coordinates of the current polygon
#         polygon = contour.squeeze().tolist()

#         # Add the polygon to the dictionary
#         polygons[f'polygon{i}'] = polygon

#     # Save the polygons to a TXT file
#     with open(filename, 'w') as f:
#         json.dump(polygons, f, indent=2)

#     return polygons

# img = cv2.imread('sample1.png')

# polygons = get_polygons(img, 'polygons.txt')



