import cv2

def resize_and_threshold(input_image, output_image, new_width,new_height, threshold_value):
    # Read the input image
    image = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    # Apply binary thresholding
    _, binary_image = cv2.threshold(resized_image, threshold_value, 255, cv2.THRESH_BINARY)

    # Save the output image
    cv2.imwrite(output_image, binary_image)

    # Display the resized and thresholded images
    cv2.imshow("Resized Image", resized_image)
    cv2.imshow("Binary Thresholded Image", binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

resize_and_threshold("apple.png", "output.png", 1000,1000, 128)
