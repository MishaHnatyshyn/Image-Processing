import cv2


def perform_laplacian_edge_detection(image_url):
    img = cv2.imread(image_url)

    output = cv2.Laplacian(img, -1)

    return output
